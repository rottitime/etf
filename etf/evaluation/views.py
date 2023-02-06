import marshmallow
from django import forms
from django.contrib.auth.decorators import login_required
from django.contrib.postgres.search import (
    SearchQuery,
    SearchRank,
    SearchVector,
)
from django.db.models import Q
from django.http import Http404
from django.shortcuts import redirect, render
from django.urls import reverse
from django.utils.text import slugify

from . import models, schemas

page_map = {}


@login_required
def index_view(request):
    if request.method == "POST":
        user = request.user
        evaluation = models.Evaluation.objects.create()
        evaluation.users.set([user])
        evaluation.save()
        return redirect(page_view, evaluation_id=str(evaluation.id))
    return render(request, "index.html")


def make_url(evaluation_id, page_name):
    if not page_name:
        return None
    return reverse("pages", args=(evaluation_id, page_name))


@login_required
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
        "legend_visible": True,
    }
    return page_map[page_name].view(request, url_data)


class FormPage:
    def __init__(self, title, extra_data=None):
        self.title = title
        self.slug = slugify(title)
        self.template_name = f"{self.slug}.html"
        self.extra_data = extra_data or {}
        page_map[self.slug] = self

    def view(self, request, url_data):
        evaluation_id = url_data["evaluation_id"]
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
                return redirect(url_data["next_url"])
            except marshmallow.exceptions.ValidationError as err:
                errors = dict(err.messages)
        else:
            data = eval_schema.dump(evaluation)
        return render(
            request,
            self.template_name,
            {
                "errors": errors,
                "topics": topics,
                "organisations": organisations,
                "statuses": statuses,
                "data": data,
                **url_data,
                **self.extra_data,
            },
        )


class SimplePage:
    def __init__(self, title, extra_data=None):
        self.title = title
        self.slug = slugify(title)
        self.extra_data = extra_data or {}
        page_map[self.slug] = self

    def view(self, request, url_data):
        return render(request, f"{self.slug}.html", {**url_data})


SimplePage(title="Intro")

FormPage(title="Title")

FormPage(title="Description")

FormPage(title="Issue")

FormPage(title="Dates")

FormPage(title="Participant recruitment")

FormPage(title="Ethics")

FormPage(title="Status")

SimplePage(title="End")


class EvaluationSearchForm(forms.Form):
    id = forms.UUIDField(required=False)
    title = forms.CharField(max_length=100, required=False)
    description = forms.CharField(max_length=100, required=False)
    topics = forms.MultipleChoiceField(choices=models.Topic.choices, required=False)
    organisations = forms.MultipleChoiceField(choices=models.Organisation.choices, required=False)
    status = forms.ChoiceField(choices=(("", "-----"), *models.EvaluationStatus.choices), required=False)
    search_phrase = forms.CharField(max_length=100, required=False)
    mine_only = forms.BooleanField(required=False)
    is_search = forms.CharField(max_length=6, required=True)


@login_required
def search_evaluations_view(request):
    qs = models.Evaluation.objects.all()
    data = {}
    errors = {}
    if request.method == "GET":
        form = EvaluationSearchForm(request.GET)
        if form.is_valid() and form.cleaned_data["is_search"]:
            topics = form.cleaned_data["topics"]
            organisations = form.cleaned_data["organisations"]
            status = form.cleaned_data["status"]
            search_phrase = form.cleaned_data["search_phrase"]
            mine_only = form.cleaned_data["mine_only"]
            if mine_only:
                qs = qs.filter(users__in=[request.user])
            if organisations:
                organisations_qs = models.Evaluation.objects.none()
                for organisation in organisations:
                    organisation_qs = qs.filter(organisations__contains=organisation)
                    organisations_qs = organisations_qs | organisation_qs
                qs = organisations_qs
            if not status:
                qs = qs.filter(
                    Q(status=models.EvaluationStatus.DRAFT.value, user=request.user)
                    | Q(status__in=[models.EvaluationStatus.PUBLIC.value, models.EvaluationStatus.CIVIL_SERVICE.value])
                )
            else:
                if status == models.EvaluationStatus.DRAFT:
                    qs = qs.filter(status=status)
                    qs = qs.filter(user=request.user)
                # TODO: make civil service and public filter more sophisticated once roles are in
                if status == models.EvaluationStatus.PUBLIC:
                    qs = qs.filter(status=status)
                if status == models.EvaluationStatus.CIVIL_SERVICE:
                    qs = qs.filter(status=status)
            if topics:
                topics_qs = models.Evaluation.objects.none()
                for topic in topics:
                    topic_qs = qs.filter(topics__contains=topic)
                    topics_qs = topics_qs | topic_qs
                qs = topics_qs
            if search_phrase:
                # TODO - what fields do we care about?
                most_important_fields = ["id", "title", "description", "topics", "organisations"]
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
            return render(request, "search-results.html", {"evaluations": qs, "errors": errors, "data": data})

        else:
            data = request.GET
            errors = form.errors
    return render(request, "search-form.html", {"form": form, "evaluations": qs, "errors": errors, "data": data})


@login_required
def my_evaluations_view(request):
    data = {}
    errors = {}
    if request.method == "GET":
        qs = models.Evaluation.objects.filter(users__in=[request.user])
        data = request.GET
    return render(request, "my-evaluations.html", {"evaluations": qs, "errors": errors, "data": data})
