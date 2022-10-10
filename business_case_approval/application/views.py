from django import forms
from django.forms.models import model_to_dict
from django.http import Http404
from django.shortcuts import redirect, render
from django.urls import reverse

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


def make_url(application_id, page_name):
    if not page_name:
        return None
    return reverse("pages", args=(application_id, page_name))


def page_view(request, application_id, page_name="intro"):
    if page_name not in page_order:
        raise Http404()

    index = page_order.index(page_name)
    prev_page = index and page_order[index - 1] or None
    next_page = (index < len(page_order) - 1) and page_order[index + 1] or None
    prev_url = make_url(prev_page)
    this_url = make_url(page_name)
    next_url = make_url(next_page)

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


def _create_form_page_response(request, url_data, form_class, template_name, extra_data=None):
    if not extra_data:
        extra_data = {}
    application_id = url_data["application_id"]
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
    return render(request, template_name, {"errors": errors, "data": data, **url_data, **extra_data})


def create_form_view(name, field_names, extra_data=None):
    if not extra_data:
        extra_data = {}

    class _Form(forms.ModelForm):
        class Meta:
            model = models.Application
            fields = field_names

    @register(name)
    def _view(request, url_data):
        return _create_form_page_response(
            request, url_data, form_class=_Form, template_name=f"{name}.pug", extra_data=extra_data
        )


def create_simple_view(name, extra_data=None):
    @register(name)
    def _view(request, url_data):
        return render(request, f"{name}.pug", {**url_data})


create_simple_view("intro")
create_form_view("name", ("name",))
create_form_view("exemption", ("hrbp", "grade", "title"), extra_data={"grades": models.Grades.options})
create_form_view("establishment", ("establishment",))
create_simple_view("end")
