from random import randint
import marshmallow
from allauth.account.views import SignupView
from django import forms
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.postgres.search import (
    SearchQuery,
    SearchRank,
    SearchVector,
)
from django.core.exceptions import ValidationError
from django.db.models import Q
from django.http import Http404, HttpResponseNotAllowed
from django.shortcuts import redirect, render
from django.urls import reverse
from django.utils.text import slugify
from django.views.decorators.http import require_http_methods

from . import models, schemas
from etf import evaluation


class MethodDispatcher:
    def __new__(cls, request, *args, **kwargs):
        view = super().__new__(cls)
        method_name = request.method.lower()
        method = getattr(view, method_name, None)
        if method:
            return method(request, *args, **kwargs)
        else:
            return HttpResponseNotAllowed(request)


class CustomSignupView(SignupView):
    def dispatch(self, request, *args, **kwargs):
        if request.method == "POST":
            if models.User.objects.filter(email=request.POST.get("email")).exists():
                messages.error(request, "A user with this email already exists, please try again.")
                return render(request, self.template_name)
            form = self.get_form()
            if not form.is_valid():
                for field, error in form.errors.items():
                    messages.error(request, error)
                return render(request, self.template_name, {"form": form})
            if form.is_valid():
                try:
                    self.form_valid(form)
                except ValidationError as e:
                    messages.error(request, str(e))
                    return render(request, self.template_name, {"form": form})
        response = super().dispatch(request, *args, **kwargs)
        return response


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


def make_url(evaluation_id, page_name):
    if not page_name:
        return None
    return reverse(page_name, args=(evaluation_id,))


def make_outcome_measure_url(evaluation_id, outcome_measure_id):
    return reverse("outcome-measures", args=(evaluation_id, outcome_measure_id))


def get_adjacent_outcome_measure_id(evaluation_id, outcome_measure_id, next=True):
    adjacent_id = None
    outcomes_for_eval = models.OutcomeMeasure.objects.filter(evaluation__id=evaluation_id).order_by("id")
    outcomes_ids = outcomes_for_eval.values_list("id", flat=True)
    current_index = outcomes_ids.index(outcome_measure_id)

    if next:
        next_index = current_index + 1
        if next_index < len(outcomes_ids):
            adjacent_id = outcomes_ids[next_index]
    else:
        prev_index = current_index + 1
        if prev_index >= 0:
            adjacent_id = outcomes_ids[prev_index]
    return adjacent_id


# def get_next_page_url(evaluation_id, page_name, outcome_measure_id=None):
#     # TODO - sort this out!
#     next_outcome_measure_id = get_next_outcome_measure(evaluation_id, outcome_measure_id)
#     if page_name == "outcome-measures":
#         if next_outcome_measure_id:
#             next_page_url = make_outcome_measure_url(evaluation_id, next_outcome_measure_id)
#         else:
#             next_page_url = make_url(evaluation_id, "status")  # TODO - this is the page afterwards
#     elif page_name == "ethics":  # TODO - ethics is the page before
#         next_page_url = make_outcome_measure_url(evaluation_id, next_outcome_measure_id)


# @login_required
# def page_view(request, evaluation_id, page_name="intro"):
#     # print("page map")
#     # print(page_map)
#     # if page_name not in page_map:
#     #     raise Http404()

#     # page_name_order = tuple(page_map.keys())

#     # index = page_name_order.index(page_name)
#     # prev_page = index and page_name_order[index - 1] or None
#     # next_page = (index < len(page_name_order) - 1) and page_name_order[index + 1] or None
#     # prev_url = make_url(evaluation_id, prev_page)
#     # this_url = make_url(evaluation_id, page_name)
#     # next_url = make_url(evaluation_id, next_page)

#     # pages = tuple(
#     #     {
#     #         "slug": _p.slug,
#     #         "url": make_url(evaluation_id, _p.slug),
#     #         "title": _p.title,
#     #         "completed": page_name_order.index(_p.slug) < index,
#     #         "current": _p.slug == page_name,
#     #     }
#     #     for _p in page_map.values()
#     # )

#     # url_data = {
#     #     "pages": pages,
#     #     "evaluation_id": evaluation_id,
#     #     "page_name": page_name,
#     #     "index": index,
#     #     "prev_page": prev_page,
#     #     "next_page": next_page,
#     #     "prev_url": prev_url,
#     #     "this_url": this_url,
#     #     "next_url": next_url,
#     #     "legend_visible": True,
#     # }
#     print(page_map)
#     # print(url_data)
#     # if page_name != "outcome-measures":
#     #     return page_map[page_name].view(request, url_data)
#     # else:
#     #     return

#     return page_map[page_name].view(request, evaluation_id)


class BasePage:
    def __init__(self, title, slug, url_data={}):
        self.title = title
        self.slug = slug
        self.url_data = url_data
        self.template_name = f"{self.slug}.html"

    #  TODO: Add redirect if user isn't allowed to see evaluation

    page_name_order = tuple(page_map.keys())

# class EvaluationFormPage(BasePage):
#     def view(self, request, evaluation_id):
#         next_url = make_url(evaluation_id, self.url_data["next_page"])
#         print("next_url")
#         print(next_url)
#         prev_url = make_url(evaluation_id, self.url_data["prev_page"])
def simple_page_view(request, evaluation_id, title, slug, prev_page, next_page):
    prev_url = make_url(evaluation_id, prev_page)
    next_url = make_url(evaluation_id, next_page)
    template_name = f"{slug}.html"
    return render(request, template_name, {"title": title, "prev_url": prev_url, "next_url": next_url})


def initial_outcome_measure_page_view(request, evaluation_id):
    evaluation = models.Evaluation.objects.get(pk=evaluation_id)
    outcomes_for_eval = models.OutcomeMeasure.objects.filter(evaluation=evaluation).order_by("id")
    errors = {}
    data = {}
    next_url = reverse("end", args=(evaluation_id,))
    if outcomes_for_eval:
        first_id = outcomes_for_eval[0].id
        return reverse("outcome-measure-page", args=(evaluation_id, first_id))
    else:
        if request.method == "POST":
            if "add" in request.POST:
                return reverse("outcome-measure-add", args=(evaluation_id,))
            else:
                return reverse("end", args=(evaluation_id,))
    return render(request, "outcome-measures.html", {"errors": errors, "data": data, "next_url": next_url})


def add_outcome_measure_page_view(request, evaluation_id):
    evaluation = models.Evaluation.objects.get(pk=evaluation_id)
    outcome = models.OutcomeMeasure(evaluation=evaluation)
    outcome.save()
    return reverse("outcome-measure-page", args=(evaluation_id, outcome.id))


def outcome_measure_page_view(request, evaluation_id, outcome_measure_id):
    outcome = models.OutcomeMeasure.objects.filter(evaluation__id=evaluation_id).get(id=outcome_measure_id)
    outcome_schema = schemas.OutcomeMeasureSchema(unknown=marshmallow.EXCLUDE)
    errors = {}
    data = {}
    show_add = False
    next_outcome_id = get_adjacent_outcome_measure_id(evaluation_id, outcome_measure_id, next=True)
    prev_outcome_id = get_adjacent_outcome_measure_id(evaluation_id, outcome_measure_id, next=False)
    if next_outcome_id:
        next_url = reverse("outcome-measure-page", args=(evaluation_id, next_outcome_id))
        show_add = True
    else:
        next_url = reverse("end", args=(evaluation_id,))
    if prev_outcome_id:
        prev_url = reverse("outcome-measure-page", args=(evaluation_id, prev_outcome_id))
    else:
        prev_url = reverse("description", args=(evaluation_id,))
    if request.method == "POST":
        if "add" in request.POST:
            return reverse("outcome-measure-add", args=(evaluation_id,))
        else:
            try:
                serialized_outcome = outcome_schema.load(data=data, partial=True)
                for field_name in serialized_outcome:
                    setattr(outcome, field_name, serialized_outcome[field_name])
                outcome.save()
                return redirect(next_url, args=(evaluation_id,))
            except marshmallow.exceptions.ValidationError as err:
                errors = dict(err.messages)
    return render(
        request,
        "outcome-measures-individual.html",
        {"errors": errors, "data": data, "next_url": next_url, "prev_url": prev_url, "show_add": show_add},
    )


def evaluation_view(request, evaluation_id, title, slug, prev_page, next_page):
    next_url = make_url(evaluation_id, next_page)
    prev_url = make_url(evaluation_id, prev_page)
    template_name = f"{slug}.html"

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


def evaluation_title_view(request, evaluation_id):
    return evaluation_view(
        request, evaluation_id, title="Title", slug="title", prev_page="intro", next_page="description"
    )


<<<<<<< HEAD
class EvaluationFormPage(BasePage):
    def view(self, request, url_data):
        evaluation_id = url_data["evaluation_id"]
        evaluation = models.Evaluation.objects.get(pk=evaluation_id)
        eval_schema = schemas.EvaluationSchema(unknown=marshmallow.EXCLUDE)
        errors = {}
        topics = models.Topic.choices
        organisations = models.Organisation.choices
        statuses = models.EvaluationStatus.choices
        users = evaluation.users.values()
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
                "contributors": users,
                "data": data,
                **url_data,
                **self.extra_data,
            },
        )
=======
def evaluation_description_view(request, evaluation_id):
    return evaluation_view(
        request, evaluation_id, title="Description", slug="description", prev_page="title", next_page="end"
    )
>>>>>>> 111b733 (unpick the views for evaluation pages)


# class OutcomeMeasureFormPage(BasePage):
#     def view(self, request, url_data, outcome_measure_id=None):
#         evaluation_id = url_data["evaluation_id"]
#         evaluation = models.Evaluation.objects.get(pk=evaluation_id)
#         outcome_schema = schemas.OutcomeMeasureSchema(unknown=marshmallow.EXCLUDE)
#         outcomes_for_eval = models.OutcomeMeasure.objects.filter(evaluation=evaluation)
#         # outcome = models.OutcomeMeasure(evaluation=evaluation)
#         if outcome_measure_id:
#             outcome = outcomes_for_eval.get(id=outcome_measure_id)
#         else:
#             outcome = models.OutcomeMeasure(evaluation=evaluation)
#         next_outcome_id = None  # or the next one in the list
#         data = outcome_schema.dump(outcome)
#         errors = {}
#         if request.method == "POST":
#             data = request.POST
#             # id_to_delete = request.POST.get("delete")

#             try:
#                 serialized_outcome = outcome_schema.load(data=data, partial=True)
#                 # TODO - if there's no data, then don't save?
#                 for field_name in serialized_outcome:
#                     setattr(outcome, field_name, serialized_outcome[field_name])
#                 outcome.save()
#                 return redirect(url_data["next_url"])
#             except marshmallow.exceptions.ValidationError as err:
#                 errors = dict(err.messages)

#         else:
#             outcome_measures = outcome_schema.dump(outcomes_for_eval, many=True)
#         return render(
#             request,
#             self.template_name,
#             {"errors": errors, "data": data, "outcome_measures": outcome_measures, **url_data, **self.extra_data},
#         )


<<<<<<< HEAD
FormPage(title="Contributors")

FormPage(title="Issue")
EvaluationFormPage(title="Dates")
=======
def intro_page_view(request, evaluation_id):
    return simple_page_view(
        request, evaluation_id, title="Introduction", slug="intro", prev_page=None, next_page="title"
    )
>>>>>>> 111b733 (unpick the views for evaluation pages)


def end_page_view(request, evaluation_id):
    return simple_page_view(request, evaluation_id, title="End", slug="end", prev_page="description", next_page=None)


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
                    Q(status=models.EvaluationStatus.DRAFT.value, users__in=[request.user])
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


@login_required
@require_http_methods(["GET", "POST", "DELETE"])
class EvaluationContributor(MethodDispatcher):
    def get(self, request, evaluation_id):
        return render(request, "add-contributor.html", {"evaluation_id": evaluation_id})

    def post(self, request, evaluation_id):
        evaluation = models.Evaluation.objects.get(pk=evaluation_id)
        email = request.POST.get("add-user-email")
        user = models.User.objects.get(email=email)
        evaluation.users.add(user)
        evaluation.save()
        users = evaluation.users.values()
        return render(request, "contributor-rows.html", {"contributors": users, "evaluation_id": evaluation_id})

    def delete(self, request, evaluation_id, email_to_remove=None):
        evaluation = models.Evaluation.objects.get(pk=evaluation_id)
        user_to_remove = models.User.objects.get(email=email_to_remove)
        evaluation.users.remove(user_to_remove)
        evaluation.save()
        users = evaluation.users.values()
        if user_to_remove == request.user:
            response = render(
                request,
                "contributor-rows.html",
                {"redirect": True, "contributors": users, "evaluation_id": evaluation_id},
            )
            response["HX-Redirect"] = reverse("index")
            return response
        return render(request, "contributor-rows.html", {"contributors": users, "evaluation_id": evaluation_id})


@login_required
@require_http_methods(["POST"])
def evaluation_contributor_add_view(request, evaluation_id):
    evaluation = models.Evaluation.objects.get(pk=evaluation_id)
    email = request.POST.get("add-user-email")
    user = models.User.objects.get(email=email)
    evaluation.users.add(user)
    evaluation.save()
    return redirect(page_view, evaluation_id=evaluation_id, page_name="contributors")


@login_required
@require_http_methods(["POST", "GET"])
def evaluation_contributor_remove_view(request, evaluation_id, email_to_remove=None):
    evaluation = models.Evaluation.objects.get(pk=evaluation_id)
    if request.method == "GET":
        return render(request, "remove-contributor.html", {"evaluation_id": evaluation_id, "email": email_to_remove})
    elif request.method == "POST":
        email = request.POST.get("remove-user-email")
        user = models.User.objects.get(email=email)
        evaluation.users.remove(user)
        evaluation.save()
        if user == request.user:
            return redirect(reverse("index"))
        return redirect(page_view, evaluation_id=evaluation_id, page_name="contributors")


@login_required
def evaluation_summary_view(request, evaluation_id):
    evaluation = models.Evaluation.objects.get(pk=evaluation_id)
    user_can_edit = evaluation.users__contains(request.user)
    return render(request, "evaluation-summary.html", {"data": evaluation, "user_can_edit": user_can_edit})
