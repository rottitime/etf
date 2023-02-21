import marshmallow
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, render
from django.urls import reverse

from . import enums, models, schemas
from .pages import page_name_and_order


@login_required
def index_view(request):
    if request.method == "POST":
        user = request.user
        evaluation = models.Evaluation.objects.create()
        evaluation.users.add(user)
        evaluation.save()
        return redirect(
            intro_page_view,
            evaluation_id=str(evaluation.id),
        )
    return render(request, "index.html")


def make_evaluation_url(evaluation_id, page_name):
    if not page_name:
        return None
    return reverse(page_name, args=(evaluation_id,))


def get_adjacent_id_for_model(evaluation_id, id, model_name, next_or_prev="next"):
    """
    For models with evaluation as foreign key, find the adjacent object
    sorted by created_at.
    """
    model = getattr(models, model_name)
    adjacent_id = None
    direction_map = {"next": 1, "prev": -1}
    related_objects_for_eval = model.objects.filter(evaluation__id=evaluation_id).order_by("created_at")
    ids = list(related_objects_for_eval.values_list("id", flat=True))
    num_objects = len(ids)
    current_index = ids.index(id)
    adjacent_index = current_index + direction_map[next_or_prev]
    if 0 <= adjacent_index < num_objects:
        adjacent_id = ids[adjacent_index]
    return adjacent_id


@login_required
def simple_page_view(request, evaluation_id, page_data):
    evaluation = models.Evaluation.objects.get(pk=evaluation_id)
    prev_url = make_evaluation_url(evaluation_id, page_data["prev_page"])
    next_url = make_evaluation_url(evaluation_id, page_data["next_page"])
    page_name = page_data["page_name"]
    template_name = f"submissions/{page_name}.html"
    title = page_data["title"]
    form_data = {"title": title, "prev_url": prev_url, "next_url": next_url, "evaluation_id": evaluation_id}
    evaluation.page_statuses[page_name] = models.EvaluationPageStatus.DONE.name
    evaluation.save()
    return render(request, template_name, form_data)


@login_required
def evaluation_view(request, evaluation_id, page_data):
    title = page_data["title"]
    page_name = page_data["page_name"]
    next_url = make_evaluation_url(evaluation_id, page_data["next_page"])
    prev_url = make_evaluation_url(evaluation_id, page_data["prev_page"])
    template_name = f"submissions/{page_name}.html"
    evaluation = models.Evaluation.objects.get(pk=evaluation_id)
    eval_schema = schemas.EvaluationSchema(unknown=marshmallow.EXCLUDE)
    errors = {}
    topics = models.Topic.choices
    organisations = enums.Organisation.choices
    statuses = models.EvaluationStatus.choices
    if request.method == "POST":
        data = request.POST
        try:
            serialized_evaluation = eval_schema.load(data=data, partial=True)
            for field_name in serialized_evaluation:
                setattr(evaluation, field_name, serialized_evaluation[field_name])
            if "topics" in data.keys():
                topic_list = data.getlist("topics") or None
                setattr(evaluation, "topics", topic_list)
            if "organisations" in data.keys():
                organisation_list = data.getlist("organisations") or None
                setattr(evaluation, "organisations", organisation_list)
            evaluation.page_statuses[page_name] = models.EvaluationPageStatus.DONE.name
            evaluation.save()
            return redirect(next_url)
        except marshmallow.exceptions.ValidationError as err:
            errors = dict(err.messages)
    else:
        evaluation.page_statuses[page_name] = models.EvaluationPageStatus.IN_PROGRESS.name
        evaluation.save()
        data = eval_schema.dump(evaluation)
    return render(
        request,
        template_name,
        {
            "errors": errors,
            "topics": topics,
            "organisations": organisations,
            "statuses": statuses,
            "data": data,
            "next_url": next_url,
            "prev_url": prev_url,
            "title": title,
        },
    )


def add_related_object_for_eval(evaluation_id, model_name, redirect_url_name, object_name=""):
    model = getattr(models, model_name)
    evaluation = models.Evaluation.objects.get(pk=evaluation_id)
    if object_name:
        new_object = model(evaluation=evaluation, name=f"New {object_name}")
    else:
        new_object = model(evaluation=evaluation)
    new_object.save()
    response = redirect(reverse(redirect_url_name, args=(evaluation_id, new_object.id)))
    return response


@login_required
def summary_related_object_page_view(request, evaluation_id, model_name, form_data):
    errors = {}
    data = {"evaluation_id": evaluation_id}
    title = form_data["title"]
    object_name = form_data["object_name"]
    object_name_plural = form_data["object_name_plural"]
    template_name = form_data["template_name"]
    prev_url_name = form_data["prev_section_url_name"]
    next_url_name = form_data["next_section_url_name"]
    page_url_name = form_data["page_url_name"]
    prev_url = reverse(prev_url_name, args=(evaluation_id,))
    next_url = reverse(next_url_name, args=(evaluation_id,))

    related_model = getattr(models, model_name)
    all_objects = related_model.objects.filter(evaluation__id=evaluation_id)
    all_objects_dictionary = {obj.name: reverse(page_url_name, args=(evaluation_id, obj.id)) for obj in all_objects}

    data["objects"] = all_objects_dictionary
    data["object_name"] = object_name
    data["object_name_plural"] = object_name_plural

    if request.method == "POST":
        return add_related_object_for_eval(evaluation_id, model_name, page_url_name, object_name)
    response = render(
        request,
        template_name,
        {"title": title, "errors": errors, "data": data, "prev_url": prev_url, "next_url": next_url},
    )
    return response


@login_required
def first_last_related_object_view(
    request, evaluation_id, model_name, summary_url_name, page_url_name, first_or_last="first"
):
    model = getattr(models, model_name)
    related_objects_for_eval = model.objects.filter(evaluation__id=evaluation_id)
    if first_or_last == "first":
        related_objects_for_eval = related_objects_for_eval.order_by("created_at")
    else:
        related_objects_for_eval = related_objects_for_eval.order_by("-created_at")
    if related_objects_for_eval:
        id = related_objects_for_eval[0].id
        response = redirect(reverse(page_url_name, args=(evaluation_id, id)))
        return response
    return redirect(reverse(summary_url_name, args=(evaluation_id,)))


@login_required
def related_object_page_view(request, evaluation_id, id, model_name, title, template_name, object_name, url_names):
    model = getattr(models, model_name)
    schema = getattr(schemas, f"{model_name}Schema")
    obj = model.objects.get(id=id)
    model_schema = schema(unknown=marshmallow.EXCLUDE)
    errors = {}
    data = {}
    next_url = reverse(url_names["next_section_url_name"], args=(evaluation_id,))
    prev_url = reverse(url_names["prev_section_url_name"], args=(evaluation_id,))
    summary_url = reverse(url_names["summary_page"], args=(evaluation_id,))
    if request.method == "POST":
        data = request.POST
        if "delete" in request.POST:
            obj.delete()
            return redirect(summary_url)
        try:
            serialized_obj = model_schema.load(data=data, partial=True)
            for field_name in serialized_obj:
                setattr(obj, field_name, serialized_obj[field_name])
            obj.save()
            if "add" in request.POST:
                return add_related_object_for_eval(
                    evaluation_id, model_name=model_name, redirect_url_name=url_names["page"]
                )
            if "return" in request.POST:
                return redirect(summary_url)
            return redirect(next_url)
        except marshmallow.exceptions.ValidationError as err:
            errors = dict(err.messages)
    else:
        data = model_schema.dump(obj)
    data["evaluation_id"] = evaluation_id
    return render(
        request,
        template_name,
        {
            "title": title,
            "errors": errors,
            "data": data,
            "next_url": next_url,
            "prev_url": prev_url,
            "object_name": object_name,
            "summary_url": summary_url,
        },
    )


def intro_page_view(request, evaluation_id):
    page_data = {"title": "Introduction", "page_name": "intro", "prev_page": None, "next_page": "title"}
    return simple_page_view(request, evaluation_id, page_data)


def evaluation_title_view(request, evaluation_id):
    page_data = {"title": "Title", "page_name": "title", "prev_page": "intro", "next_page": "description"}
    return evaluation_view(request, evaluation_id, page_data)


def evaluation_description_view(request, evaluation_id):
    page_data = {
        "title": "Description",
        "page_name": "description",
        "prev_page": "title",
        "next_page": "issue-description",
    }
    return evaluation_view(request, evaluation_id, page_data)


def evaluation_issue_description_view(request, evaluation_id):
    page_data = {
        "title": "Issue description",
        "page_name": "issue-description",
        "prev_page": "description",
        "next_page": "studied-population",
    }
    return evaluation_view(request, evaluation_id, page_data)


def evaluation_studied_population_view(request, evaluation_id):
    page_data = {
        "title": "Studied population",
        "page_name": "studied-population",
        "prev_page": "issue-description",
        "next_page": "participant-recruitment",
    }
    return evaluation_view(request, evaluation_id, page_data)


def evaluation_participant_recruitment(request, evaluation_id):
    page_data = {
        "title": "Participant recruitment",
        "page_name": "participant-recruitment",
        "prev_page": "studied-population",
        "next_page": "evaluation-costs",
    }
    return evaluation_view(request, evaluation_id, page_data)


def evaluation_costs_view(request, evaluation_id):
    page_data = {
        "title": "Evaluation costs and budget",
        "page_name": "evaluation-costs",
        "prev_page": "participant-recruitment",
        "next_page": "policy-costs",
    }
    return evaluation_view(request, evaluation_id, page_data)


def evaluation_policy_costs_view(request, evaluation_id):
    page_data = {
        "title": "Policy costs and budget",
        "page_name": "policy-costs",
        "prev_page": "evaluation-costs",
        "next_page": "publication-intention",
    }
    return evaluation_view(request, evaluation_id, page_data)


def evaluation_publication_intention_view(request, evaluation_id):
    page_data = {
        "title": "Publication intention",
        "page_name": "publication-intention",
        "prev_page": "policy-costs",
        "next_page": "documents",
    }
    return evaluation_view(request, evaluation_id, page_data)


def evaluation_documents_view(request, evaluation_id):
    page_data = {
        "title": "Documents",
        "page_name": "documents",
        "prev_page": "publication-intention",
        "next_page": "event-dates",
    }
    return evaluation_view(request, evaluation_id, page_data)


def evaluation_event_dates_view(request, evaluation_id):
    page_data = {
        "title": "Event dates",
        "page_name": "event-dates",
        "prev_page": "documents",
        "next_page": "evaluation-types",
    }
    return evaluation_view(request, evaluation_id, page_data)


def evaluation_types_view(request, evaluation_id):
    page_data = {
        "title": "Evaluation types",
        "page_name": "evaluation-types",
        "prev_page": "event-dates",
        "next_page": "impact-design",
    }
    return evaluation_view(request, evaluation_id, page_data)


def evaluation_impact_eval_design_view(request, evaluation_id):
    page_data = {
        "title": "Impact evaluation design",
        "page_name": "impact-design",
        "prev_page": "evaluation-types",
        "next_page": "impact-analysis",
    }
    return evaluation_view(request, evaluation_id, page_data)


def evaluation_impact_eval_analysis_view(request, evaluation_id):
    page_data = {
        "title": "Impact evaluation analysis",
        "page_name": "impact-analysis",
        "prev_page": "impact-design",
        "next_page": "process-design",
    }
    return evaluation_view(request, evaluation_id, page_data)


def evaluation_process_eval_design_view(request, evaluation_id):
    page_data = {
        "title": "Process evaluation design",
        "page_name": "process-design",
        "prev_page": "impact-analysis",
        "next_page": "process-analysis",
    }
    return evaluation_view(request, evaluation_id, page_data)


def evaluation_process_eval_analysis_view(request, evaluation_id):
    page_data = {
        "title": "Process evaluation analysis",
        "page_name": "process-analysis",
        "prev_page": "process-design",
        "next_page": "economic-design",
    }
    return evaluation_view(request, evaluation_id, page_data)


def evaluation_economic_eval_design_view(request, evaluation_id):
    page_data = {
        "title": "Economic evaluation design",
        "page_name": "economic-design",
        "prev_page": "process-analysis",
        "next_page": "economic-analysis",
    }
    return evaluation_view(request, evaluation_id, page_data)


def evaluation_economic_eval_analysis_view(request, evaluation_id):
    page_data = {
        "title": "Economic evaluation analysis",
        "page_name": "economic-analysis",
        "prev_page": "economic-design",
        "next_page": "other-design",
    }
    return evaluation_view(request, evaluation_id, page_data)


def evaluation_other_eval_design_view(request, evaluation_id):
    page_data = {
        "title": "Other evaluation design",
        "page_name": "other-design",
        "prev_page": "economic-analysis",
        "next_page": "other-analysis",
    }
    return evaluation_view(request, evaluation_id, page_data)


def evaluation_other_eval_analysis_view(request, evaluation_id):
    page_data = {
        "title": "Other evaluation analysis",
        "page_name": "other-analysis",
        "prev_page": "other-design",
        "next_page": "interventions-summary",
    }
    return evaluation_view(request, evaluation_id, page_data)


def evaluation_ethics_view(request, evaluation_id):
    page_data = {
        "title": "Ethics",
        "page_name": "ethics",
        "prev_page": "other-measures-summary",
        "next_page": "impact-findings",
    }
    return evaluation_view(request, evaluation_id, page_data)


def evaluation_impact_findings_view(request, evaluation_id):
    page_data = {
        "title": "Impact evaluation findings",
        "page_name": "impact-findings",
        "prev_page": "ethics",
        "next_page": "economic-findings",
    }
    return evaluation_view(request, evaluation_id, page_data)


def evaluation_economic_findings_view(request, evaluation_id):
    page_data = {
        "title": "Economic evaluation findings",
        "page_name": "economic-findings",
        "prev_page": "impact-findings",
        "next_page": "process-findings",
    }
    return evaluation_view(request, evaluation_id, page_data)


def evaluation_process_findings_view(request, evaluation_id):
    page_data = {
        "title": "Process evaluation findings",
        "page_name": "process-findings",
        "prev_page": "economic-findings",
        "next_page": "other-findings",
    }
    return evaluation_view(request, evaluation_id, page_data)


def evaluation_other_findings_view(request, evaluation_id):
    page_data = {
        "title": "Other evaluation findings",
        "page_name": "other-findings",
        "prev_page": "process-findings",
        "next_page": "processes-standards-summary",
    }
    return evaluation_view(request, evaluation_id, page_data)


def evaluation_links_view(request, evaluation_id):
    page_data = {
        "title": "Links and IDs",
        "page_name": "links",
        "prev_page": "processes-standards-summary",
        "next_page": "metadata",
    }
    return evaluation_view(request, evaluation_id, page_data)


def evaluation_metadata_view(request, evaluation_id):
    page_data = {
        "title": "Metadata",
        "page_name": "metadata",
        "prev_page": "links",
        "next_page": "status",
    }
    return evaluation_view(request, evaluation_id, page_data)


def evaluation_status_view(request, evaluation_id):
    page_data = {"title": "Evaluation visibility", "page_name": "status", "prev_page": "metadata", "next_page": "end"}
    return evaluation_view(request, evaluation_id, page_data)


def end_page_view(request, evaluation_id):
    page_data = {"title": "End", "page_name": "end", "prev_page": "status", "next_page": None}
    return simple_page_view(request, evaluation_id, page_data)


def summary_interventions_page_view(request, evaluation_id):
    form_data = {
        "title": "Interventions",
        "template_name": "submissions/interventions.html",
        "prev_section_url_name": "other-analysis",
        "next_section_url_name": "outcome-measures-summary",
        "page_url_name": "intervention-page",
        "object_name": "intervention",
        "object_name_plural": "interventions",
    }
    model_name = "Intervention"
    return summary_related_object_page_view(request, evaluation_id, model_name, form_data)


def intervention_page_view(request, evaluation_id, intervention_id):
    model_name = "Intervention"
    title = "Interventions"
    template_name = "submissions/intervention-page.html"
    object_name = "intervention"
    url_names = {
        "page": "intervention-page",
        "prev_section_url_name": "other-analysis",
        "next_section_url_name": "outcome-measures-summary",
        "summary_page": "interventions-summary",
        "delete": "intervention-delete",
    }
    response = related_object_page_view(
        request,
        evaluation_id=evaluation_id,
        id=intervention_id,
        model_name=model_name,
        title=title,
        template_name=template_name,
        object_name=object_name,
        url_names=url_names,
    )
    return response


<<<<<<< HEAD
def delete_intervention_page_view(request, evaluation_id, intervention_id):
    model_name = "Intervention"
    summary_url_name = "interventions-summary"
    page_url_name = "intervention-page"
    evaluation_id, id, model_name, summary_url_name, page_url_name
    response = delete_related_object_view(
        request,
        evaluation_id=evaluation_id,
        id=intervention_id,
        model_name=model_name,
        summary_url_name=summary_url_name,
        page_url_name=page_url_name,
    )
    return response


<<<<<<< HEAD
def initial_outcome_measure_page_view(request, evaluation_id):
    evaluation = models.Evaluation.objects.get(pk=evaluation_id)
=======
=======
>>>>>>> 40dd14d (Delete unused delete views)
def summary_outcome_measure_page_view(request, evaluation_id):
>>>>>>> dad9f4d (refactoring)
    form_data = {
        "title": "Outcome measures",
        "template_name": "submissions/outcome-measures.html",
        "prev_section_url_name": "interventions-summary",
        "next_section_url_name": "other-measures-summary",
        "page_url_name": "outcome-measure-page",
        "object_name": "outcome measure",
        "object_name_plural": "outcome measures",
    }
    model_name = "OutcomeMeasure"
<<<<<<< HEAD
    evaluation.page_statuses["outcome-measures"] = models.EvaluationPageStatus.IN_PROGRESS.name
    return initial_related_object_page_view(request, evaluation_id, model_name, form_data)
=======
    return summary_related_object_page_view(request, evaluation_id, model_name, form_data)
>>>>>>> dad9f4d (refactoring)


def outcome_measure_page_view(request, evaluation_id, outcome_measure_id):
    model_name = "OutcomeMeasure"
    title = "Outcome measures"
    template_name = "submissions/outcome-measure-page.html"

    object_name = "outcome measure"
    url_names = {
        "page": "outcome-measure-page",
        "prev_section_url_name": "interventions-summary",
        "next_section_url_name": "other-measures-summary",
        "summary_page": "outcome-measures-summary",
        "delete": "outcome-measure-delete",
    }
    response = related_object_page_view(
        request,
        evaluation_id=evaluation_id,
        id=outcome_measure_id,
        model_name=model_name,
        title=title,
        template_name=template_name,
        object_name=object_name,
        url_names=url_names,
    )
    return response


<<<<<<< HEAD
def delete_outcome_measure_page_view(request, evaluation_id, outcome_measure_id):
    model_name = "OutcomeMeasure"
    summary_url_name = "outcome-measures-summary"
    page_url_name = "outcome-measure-page"
    evaluation_id, id, model_name, summary_url_name, page_url_name
    response = delete_related_object_view(
        request,
        evaluation_id=evaluation_id,
        id=outcome_measure_id,
        model_name=model_name,
        summary_url_name=summary_url_name,
        page_url_name=page_url_name,
    )
    return response


<<<<<<< HEAD
def evaluation_overview_view(request, evaluation_id):
    evaluation = models.Evaluation.objects.get(pk=evaluation_id)
    statuses = evaluation.page_statuses
    data = {
        "statuses": statuses,
        "page_order": page_name_and_order,
        "evaluation_id": evaluation_id,
    }
    errors = {}

    return render(request, "submissions/overview.html", {"errors": errors, "data": data})


def initial_other_measure_page_view(request, evaluation_id):
=======
=======
>>>>>>> 40dd14d (Delete unused delete views)
def summary_other_measure_page_view(request, evaluation_id):
>>>>>>> dad9f4d (refactoring)
    form_data = {
        "title": "Other measures",
        "template_name": "submissions/other-measures.html",
        "prev_section_url_name": "outcome-measures-summary",
        "next_section_url_name": "ethics",
        "page_url_name": "other-measure-page",
        "object_name": "other measure",
        "object_name_plural": "other measures",
    }
    model_name = "OtherMeasure"
    return summary_related_object_page_view(request, evaluation_id, model_name, form_data)


def other_measure_page_view(request, evaluation_id, other_measure_id):
    model_name = "OtherMeasure"
    title = "Other measures"
    template_name = "submissions/other-measure-page.html"
    object_name = "other measure"
    url_names = {
        "page": "other-measure-page",
        "prev_section_url_name": "outcome-measures-summary",
        "next_section_url_name": "ethics",
        "summary_page": "other-measures-summary",
        "delete": "other-measure-delete",
    }
    response = related_object_page_view(
        request,
        evaluation_id=evaluation_id,
        id=other_measure_id,
        model_name=model_name,
        title=title,
        template_name=template_name,
        object_name=object_name,
        url_names=url_names,
    )
    return response


def summary_processes_standards_page_view(request, evaluation_id):
    form_data = {
        "title": "Processes and standards",
        "template_name": "submissions/processes-standards.html",
        "prev_section_url_name": "other-findings",
        "next_section_url_name": "links",
        "page_url_name": "process-standard-page",
        "object_name": "process or standard",
        "object_name_plural": "processes and standards",
    }
    model_name = "ProcessStandard"
    return summary_related_object_page_view(request, evaluation_id, model_name, form_data)


def process_standard_page_view(request, evaluation_id, process_standard_id):
    model_name = "ProcessStandard"
    title = "Processes and standards"
    template_name = "submissions/process-standard-page.html"
    object_name = "process or standard"
    url_names = {
        "page": "process-standard-page",
        "prev_section_url_name": "other-findings",
        "next_section_url_name": "links",
        "summary_page": "processes-standards-summary",
        "delete": "process-standard-delete",
    }
    response = related_object_page_view(
        request,
        evaluation_id=evaluation_id,
        id=process_standard_id,
        model_name=model_name,
        title=title,
        template_name=template_name,
        object_name=object_name,
        url_names=url_names,
    )
    return response
