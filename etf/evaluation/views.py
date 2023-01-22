from django import forms
from django.contrib.postgres.search import (
    SearchQuery,
    SearchRank,
    SearchVector,
)
from django.http import Http404
from django.shortcuts import redirect, render
from django.urls import reverse
from django.utils.text import slugify
from marshmallow import exceptions

from . import models, serializers

page_map = {}


def index_view(request):
    if request.method == "POST":
        user = request.user
        evaluation = models.Evaluation(user=user)
        evaluation.save()
        return redirect(page_view, evaluation_id=str(evaluation.id))
    return render(request, "index.html")


def make_url(evaluation_id, page_name):
    if not page_name:
        return None
    return reverse("pages", args=(evaluation_id, page_name))


def page_view(request, evaluation_id, page_name="intro"):
    if page_name not in page_map:
        raise Http404()

    page_name_order = tuple(page_map.keys())

    index = page_name_order.index(page_name)
    prev_page = index and page_name_order[index - 1] or None
    next_page = (index < len(page_name_order) - 1) and page_name_order[index + 1] or None
    prev_url = make_url(evaluation_id, prev_page)
    this_url = make_url(evaluation_id, page_name)
    next_url = make_url(evaluation_id, next_page)

    pages = tuple(
        {
            "slug": _p.slug,
            "url": make_url(evaluation_id, _p.slug),
            "title": _p.title,
            "completed": page_name_order.index(_p.slug) < index,
            "current": _p.slug == page_name,
        }
        for _p in page_map.values()
    )

    url_data = {
        "pages": pages,
        "evaluation_id": evaluation_id,
        "page_name": page_name,
        "index": index,
        "prev_page": prev_page,
        "next_page": next_page,
        "prev_url": prev_url,
        "this_url": this_url,
        "next_url": next_url,
    }
    return page_map[page_name].view(request, url_data)


class FormPage:
    def __init__(self, title, field_names, extra_data=None):
        self.title = title
        self.slug = slugify(title)
        self.field_names = field_names
        self.template_name = f"{self.slug}.html"
        self.extra_data = extra_data or {}
        page_map[self.slug] = self

    def view(self, request, url_data):
        evaluation_id = url_data["evaluation_id"]
        evaluation = models.Evaluation.objects.get(pk=evaluation_id)
        eval_serializer = serializers.EvaluationSchema()
        data = eval_serializer.dump(evaluation)
        errors = {}
        if request.method == "POST":
            data = request.POST
            fields = set(self.field_names).intersection(set(data.keys()))  # TODO - can we do this without field_names?
            new_eval_data = {key: data[key] for key in fields}
            try:
                serialized_evaluation = eval_serializer.load(data=new_eval_data, partial=True)
                for field_name in serialized_evaluation:
                    setattr(evaluation, field_name, serialized_evaluation[field_name])
                evaluation.save()
                return redirect(url_data["next_url"])
            except exceptions.ValidationError as err:
                data = request.POST
                errors = err
        else:
            data = eval_serializer.dump(evaluation)
            errors = {}
        # TODO - What are we actually doing with the errors?
        return render(request, self.template_name, {"errors": errors, "data": data, **url_data, **self.extra_data})


class SimplePage:
    def __init__(self, title, extra_data=None):
        self.title = title
        self.slug = slugify(title)
        self.extra_data = extra_data or {}
        page_map[self.slug] = self

    def view(self, request, url_data):
        return render(request, f"{self.slug}.html", {**url_data})


SimplePage(title="Intro")

FormPage(title="Title", field_names=("title",))

FormPage(
    title="Description",
    field_names=("description",),
)

FormPage(
    title="Issue",
    field_names=(
        "issue_description",
        "those_experiencing_issue",
        "why_improvements_matter",
        "who_improvements_matter_to",
        "current_practice",
        "issue_relevance",
    ),
)

FormPage(
    title="Dates",
    field_names=(
        "evaluation_start_date",
        "evaluation_end_date",
        "date_of_intended_publication",
        "reasons_for_delays_in_publication",
    ),
)

FormPage(
    title="Participant recruitment",
    field_names=(
        "target_population",
        "eligibility_criteria",
        "process_for_recruitment",
        "target_sample_size",
        "intended_recruitment_schedule",
        "date_of_first_recruitment",
    ),
)

FormPage(
    title="Ethics",
    field_names=(
        "ethics_committee_approval",
        "ethics_committee_details",
        "ethical_state_given_existing_evidence_base",
        "confidentiality_and_personal_data",
        "breaking_confidentiality",
        "risks_to_participants",
        "risks_to_study_team",
        "participant_involvement",
        "participant_consent",
        "participant_information",
        "participant_payment",
        "other_ethical_information",
    ),
)

SimplePage(title="End")


class EvaluationSearchForm(forms.Form):
    id = forms.UUIDField(required=False)
    title = forms.CharField(max_length=100, required=False)
    description = forms.CharField(max_length=100, required=False)
    topics = forms.MultipleChoiceField(choices=models.Topic.choices, required=False)
    organisations = forms.MultipleChoiceField(choices=models.Organisation.choices, required=False)
    is_published = forms.BooleanField(required=False)
    search_phrase = forms.CharField(max_length=100, required=True)
    mine_only = forms.BooleanField(required=False)


def search_evaluations_view(request):
    qs = models.Evaluation.objects.all()
    data = {}
    errors = {}
    if request.method == "GET":
        form = EvaluationSearchForm(request.GET)
        if form.is_valid():
            id = form.cleaned_data["id"]
            topics = form.cleaned_data["topics"]
            organisations = form.cleaned_data["organisations"]
            is_published = form.cleaned_data["is_published"]
            search_phrase = form.cleaned_data["search_phrase"]
            mine_only = form.cleaned_data["mine_only"]
            if mine_only:
                qs = qs.filter(user=request.user)
            if id:
                qs = qs.filter(id=id)
            if organisations:
                qs = qs.filter(organisation__in=organisations)
            if is_published:
                qs = qs.filter(is_published=True)
            if topics:
                topics_qs = models.Evaluation.objects.none()
                for topic in topics:
                    topic_qs = qs.filter(topics__contains=topic)
                    topics_qs = topics_qs | topic_qs
                qs = topics_qs
            if search_phrase:
                # TODO - what fields do we care about?
                most_important_fields = ["title", "description", "topics", "organisation"]
                other_fields = [
                    "issue_description",
                    "those_experiencing_issue",
                    "why_improvements_matter",
                    "who_improvements_matter_to",
                    "current_practice",
                    "issue_relevance",
                ]
                search_vector = SearchVector(most_important_fields[0], weight="A")
                for field in most_important_fields[1:]:
                    search_vector = search_vector + SearchVector(field, weight="A")
                for field in other_fields:
                    search_vector = search_vector + SearchVector(field, weight="B")
                search_query = SearchQuery(search_phrase)
                rank = SearchRank(search_vector, search_query)
                qs = qs.annotate(search=search_vector).annotate(rank=rank).filter(search=search_query).order_by("-rank")
                return render(request, "search_results.html", {"evaluations": qs, "errors": errors, "data": data})

        else:
            data = request.GET
            errors = form.errors
    return render(request, "search_form.html", {"form": form, "evaluations": qs, "errors": errors, "data": data})
