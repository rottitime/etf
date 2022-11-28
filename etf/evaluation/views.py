from django import forms
from django.forms.models import model_to_dict
from django.http import Http404
from django.shortcuts import redirect, render
from django.urls import reverse

from . import models

view_map = {}


def register(name):
    def _inner(func):
        view_map[name] = func
        return func

    return _inner


def index_view(request):
    if request.method == "POST":
        user = request.user
        evaluation = models.Evaluation(user=user)
        evaluation.save()
        return redirect(page_view, evaluation_id=str(evaluation.id))
    return render(request, "index.pug")


def make_url(evaluation_id, page_name):
    if not page_name:
        return None
    return reverse("pages", args=(evaluation_id, page_name))


def page_view(request, evaluation_id, page_name="intro"):
    if page_name not in view_map:
        raise Http404()

    page_order = tuple(view_map.keys())

    index = page_order.index(page_name)
    prev_page = index and page_order[index - 1] or None
    next_page = (index < len(page_order) - 1) and page_order[index + 1] or None
    prev_url = make_url(evaluation_id, prev_page)
    this_url = make_url(evaluation_id, page_name)
    next_url = make_url(evaluation_id, next_page)

    pages = tuple(
        {
            'name': _pn,
            'url': make_url(evaluation_id, _pn),
            'title': _pn.capitalize(),
            'completed': page_order.index(_pn) < index
        } for _pn in page_order)

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
    return view_map[page_name](request, url_data)


def _create_form_page_response(request, url_data, form_class, template_name, extra_data=None):
    if not extra_data:
        extra_data = {}
    evaluation_id = url_data["evaluation_id"]
    evaluation = models.Evaluation.objects.get(pk=evaluation_id)
    if request.method == "POST":
        form = form_class(request.POST, instance=evaluation)
        if form.is_valid():
            form.save()
            return redirect(url_data["next_url"])
        else:
            data = request.POST
            errors = form.errors
    else:
        data = model_to_dict(evaluation)
        errors = {}
    return render(request, template_name, {"errors": errors, "data": data, **url_data, **extra_data})


def create_form_view(slug, field_names, extra_data=None):
    if not extra_data:
        extra_data = {}

    class _Form(forms.ModelForm):
        class Meta:
            model = models.Evaluation
            fields = field_names

    @register(slug)
    def _view(request, url_data):
        return _create_form_page_response(
            request, url_data, form_class=_Form, template_name=f"{slug}.pug", extra_data=extra_data
        )


def create_simple_view(slug, extra_data=None):
    @register(slug)
    def _view(request, url_data):
        return render(request, f"{slug}.pug", {**url_data})


create_simple_view(slug="intro")

create_form_view(slug="title", field_names=("title",))

create_form_view(
    slug="description",
    field_names=("description", "issue_description"),
)

create_form_view(
    slug="issue",
    field_names=(
        "issue_description",
        "those_experiencing_issue",
        "why_improvements_matter",
        "who_improvements_matter_to",
        "current_practice",
        "issue_relevance",
    ),
)

create_form_view(slug="doi", field_names=("doi",))

create_form_view(
    slug="dates",
    field_names=(
        "evaluation_start_date",
        "evaluation_end_date",
        "date_of_intended_publication",
        "reasons_for_delays_in_publication",
    ),
)

create_form_view(slug="rap", field_names=("rap_planned", "rap_planned_detail", "rap_outcome", "rap_outcome_detail"))

create_form_view(
    slug="participant_recruitment",
    field_names=(
        "target_population",
        "eligibility_criteria",
        "process_for_recruitment",
        "target_sample_size",
        "intended_recruitment_schedule",
        "date_of_first_recruitment",
    ),
)

create_form_view(
    slug="ethics",
    field_names=(
        "ethics_committee_approval",
        "ethics_committee_details",
        "ethical_state_given_existing_evidence_base",
    ),
)

create_form_view(
    slug="risks",
    field_names=(
        "risks_to_participants",
        "risks_to_study_team",
    ),
)

create_form_view(
    slug="participants",
    field_names=(
        "participant_involvement",
        "participant_consent",
        "participant_information",
        "participant_payment",
    ),
)

create_form_view(slug="confidentiality", field_names=("confidentiality_and_personal_data", "breaking_confidentiality"))

create_form_view(slug="other-ethical", field_names=("other_ethical_information",))

create_simple_view(slug="end")
