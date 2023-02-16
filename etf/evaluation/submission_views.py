import marshmallow
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, render
from django.urls import reverse

from . import models, schemas


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


def get_adjacent_outcome_measure_id(evaluation_id, outcome_measure_id, next_or_prev="next"):
    adjacent_id = None
    direction_map = {"next": 1, "prev": -1}
    outcomes_for_eval = models.OutcomeMeasure.objects.filter(evaluation__id=evaluation_id).order_by("id")
    outcomes_ids = list(outcomes_for_eval.values_list("id", flat=True))
    num_outcomes = len(outcomes_ids)
    current_index = outcomes_ids.index(outcome_measure_id)
    adjacent_index = current_index + direction_map[next_or_prev]
    if 0 <= adjacent_index < num_outcomes:
        adjacent_id = outcomes_ids[adjacent_index]
    return adjacent_id


@login_required
def simple_page_view(request, evaluation_id, page_data):
    prev_url = make_evaluation_url(evaluation_id, page_data["prev_page"])
    next_url = make_evaluation_url(evaluation_id, page_data["next_page"])
    page_name = page_data["page_name"]
    template_name = f"submissions/{page_name}.html"
    title = page_data["title"]
    form_data = {"title": title, "prev_url": prev_url, "next_url": next_url}
    return render(request, template_name, form_data)


def add_outcome_measure(evaluation_id):
    evaluation = models.Evaluation.objects.get(pk=evaluation_id)
    outcome = models.OutcomeMeasure(evaluation=evaluation)
    outcome.save()
    return redirect(reverse("outcome-measure-page", args=(evaluation_id, outcome.id)))


@login_required
def initial_outcome_measure_page_view(request, evaluation_id):
    errors = {}
    data = {}
    prev_url = reverse("interventions", args=(evaluation_id,))
    next_url = reverse("other-measures", args=(evaluation_id,))
    if request.method == "POST":
        if "add" in request.POST:
            return add_outcome_measure(evaluation_id)
        return redirect(next_url)
    return render(
        request,
        "submissions/outcome-measures.html",
        {"title": "Outcome measures", "errors": errors, "data": data, "prev_url": prev_url, "next_url": next_url},
    )


@login_required
def first_last_outcome_measure_view(request, evaluation_id, first_or_last="first"):
    outcomes_for_eval = models.OutcomeMeasure.objects.filter(evaluation__id=evaluation_id)
    if first_or_last == "first":
        outcomes_for_eval = outcomes_for_eval.order_by("id")
    else:
        outcomes_for_eval = outcomes_for_eval.order_by("-id")
    if outcomes_for_eval:
        outcome_id = outcomes_for_eval[0].id
        return redirect(reverse("outcome-measure-page", args=(evaluation_id, outcome_id)))
    else:
        return redirect(reverse("outcome-measures", args=(evaluation_id,)))


@login_required
def first_outcome_measure_page_view(request, evaluation_id):
    return first_last_outcome_measure_view(request, evaluation_id, first_or_last="first")


@login_required
def last_outcome_measure_page_view(request, evaluation_id):
    return first_last_outcome_measure_view(request, evaluation_id, first_or_last="last")


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
    organisations = models.Organisation.choices
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
            evaluation.save()
            return redirect(next_url)
        except marshmallow.exceptions.ValidationError as err:
            errors = dict(err.messages)
    else:
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


@login_required
def outcome_measure_page_view(request, evaluation_id, outcome_measure_id):
    outcome = models.OutcomeMeasure.objects.get(id=outcome_measure_id)
    outcome_schema = schemas.OutcomeMeasureSchema(unknown=marshmallow.EXCLUDE)
    errors = {}
    data = {}
    show_add = False
    next_outcome_id = get_adjacent_outcome_measure_id(evaluation_id, outcome_measure_id, next_or_prev="next")
    prev_outcome_id = get_adjacent_outcome_measure_id(evaluation_id, outcome_measure_id, next_or_prev="prev")
    if next_outcome_id:
        next_url = reverse("outcome-measure-page", args=(evaluation_id, next_outcome_id))
    else:
        next_url = reverse("other-measures", args=(evaluation_id,))
        show_add = True
    if prev_outcome_id:
        prev_url = reverse("outcome-measure-page", args=(evaluation_id, prev_outcome_id))
    else:
        prev_url = reverse("interventions", args=(evaluation_id,))
    if request.method == "POST":
        data = request.POST
        try:
            if "delete" in request.POST:
                delete_url = reverse("outcome-measure-delete", args=(evaluation_id, outcome_measure_id))
                return redirect(delete_url)
            serialized_outcome = outcome_schema.load(data=data, partial=True)
            for field_name in serialized_outcome:
                setattr(outcome, field_name, serialized_outcome[field_name])
            outcome.save()
            if "add" in request.POST:
                return add_outcome_measure(evaluation_id)
            return redirect(next_url)
        except marshmallow.exceptions.ValidationError as err:
            errors = dict(err.messages)
    else:
        data = outcome_schema.dump(outcome)
    return render(
        request,
        "submissions/outcome-measure-page.html",
        {
            "title": "Outcome measures",
            "errors": errors,
            "data": data,
            "next_url": next_url,
            "prev_url": prev_url,
            "show_add": show_add,
        },
    )


def delete_outcome_measure_page_view(request, evaluation_id, outcome_measure_id):
    outcome = models.OutcomeMeasure.objects.filter(evaluation__id=evaluation_id).get(id=outcome_measure_id)
    prev_id = get_adjacent_outcome_measure_id(evaluation_id, outcome_measure_id, next_or_prev="prev")
    outcome.delete()
    if prev_id:
        next_url = reverse("outcome-measure-page", args=(evaluation_id, prev_id))
    else:
        next_url = reverse("outcome-measures", args=(evaluation_id,))
    return redirect(next_url)


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
        "next_page": "interventions",
    }
    return evaluation_view(request, evaluation_id, page_data)


# TODO - likely to be more like outcome measures ie many interventions
def evaluation_intervention_view(request, evaluation_id):
    page_data = {
        "title": "Interventions",
        "page_name": "interventions",
        "prev_page": "other-analysis",
        "next_page": "outcome-measure-first",
    }
    return evaluation_view(request, evaluation_id, page_data)


# TODO - likely to be more like outcome measures ie many interventions
def evaluation_other_measures_view(request, evaluation_id):
    page_data = {
        "title": "Other measure",
        "page_name": "other-measures",
        "prev_page": "outcome-measure-last",
        "next_page": "ethics",
    }
    return evaluation_view(request, evaluation_id, page_data)


def evaluation_ethics_view(request, evaluation_id):
    page_data = {
        "title": "Ethics",
        "page_name": "ethics",
        "prev_page": "other-measures",
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
        "next_page": "process-standards",
    }
    return evaluation_view(request, evaluation_id, page_data)


# TODO - there may be many of these
def evaluation_process_standards_view(request, evaluation_id):
    page_data = {
        "title": "Processes and standards",
        "page_name": "process-standards",
        "prev_page": "other-findings",
        "next_page": "links",
    }
    return evaluation_view(request, evaluation_id, page_data)


def evaluation_links_view(request, evaluation_id):
    page_data = {
        "title": "Links and IDs",
        "page_name": "links",
        "prev_page": "process-standards",
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
    page_data = {"title": "Status", "page_name": "status", "prev_page": "metadata", "next_page": "end"}
    return evaluation_view(request, evaluation_id, page_data)


def end_page_view(request, evaluation_id):
    page_data = {"title": "End", "page_name": "end", "prev_page": "status", "next_page": None}
    return simple_page_view(request, evaluation_id, page_data)
