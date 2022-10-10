from django import forms
from django.http import Http404
from django.shortcuts import redirect, render
from django.urls import reverse
from django.forms.models import model_to_dict

from . import models

page_order = (
    "intro",
    "name",
    "exemption",
    "establishment",
    "end",
)

view_map = {}


def register(name):
    def _inner(func):
        view_map[name] = func
        return func

    return _inner


def index_view(request):
    if request.method == "POST":
        user = request.user
        application = models.Application(user=user)
        application.save()
        return redirect(page_view, application_id=application.id)
    return render(request, "index.pug")


def page_view(request, application_id, page_name="intro"):
    if page_name not in page_order:
        raise Http404()

    index = page_order.index(page_name)
    prev_page = index and page_order[index - 1] or None
    next_page = (index < len(page_order) - 1) and page_order[index + 1] or None
    prev_url = prev_page and reverse("pages", args=(application_id, prev_page,))
    this_url = reverse("pages", args=(application_id, page_name,))
    next_url = next_page and reverse("pages", args=(application_id, next_page,))

    url_data = {
        "application_id": application_id,
        "page_name": page_name,
        "index": index,
        "prev_page": prev_page,
        "next_page": next_page,
        "prev_url": prev_url,
        "this_url": this_url,
        "next_url": next_url,
    }
    return view_map[page_name](request, url_data)


@register("intro")
def intro_view(request, url_data):
    return render(request, "intro.pug", {**url_data})


def _create_form_page_response(request, url_data, form_class, template_name, extra_data=None):
    if not extra_data:
        extra_data = {}
    application_id = request.session["application_id"]
    application = models.Application.objects.get(pk=application_id)
    if request.method == "POST":
        form = form_class(request.POST, instance=application)
        if form.is_valid():
            form.save()
            return redirect(url_data["next_url"])
        else:
            data = request.POST
            errors = form.errors
    else:
        data = model_to_dict(application)
        errors = {}
    return render(
        request, template_name, {"errors": errors, "data": data, **url_data, **extra_data}
    )


class NameForm(forms.ModelForm):
    class Meta:
        model = models.Application
        fields = ["name"]


@register("name")
def name_view(request, url_data):
    _create_form_page_response(request, url_data, form_class=NameForm, template_name="name.pug")


class ExemptionAdminForm(forms.ModelForm):
    class Meta:
        model = models.Application
        fields = ["hrbp", "grade", "title"]



@register("exemption")
def exemption_view(request, url_data):
    _create_form_page_response(request, url_data, form_class=ExemptionAdminForm, template_name="exemption.pug")


class EstablishmentForm(forms.ModelForm):
    class Meta:
        model = models.Application
        fields = ["establishment"]


@register("establishment")
def establishment_view(request, url_data):
    _create_form_page_response(request, url_data, form_class=EstablishmentForm, template_name="establishment.pug", extra_data={"grades": models.Grades.options})


@register("end")
def end_view(request, url_data):
    return render(request, "end.pug", {**url_data})
