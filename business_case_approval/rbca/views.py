from django import forms
from django.http import Http404
from django.shortcuts import redirect, render
from django.urls import reverse

from . import models

page_order = (
    "index",
    "name",
    "exemption",
)

view_map = {}


def register(name):
    def _inner(func):
        view_map[name] = func
        return func

    return _inner


def page_view(request, page_name="index"):
    if page_name not in page_order:
        raise Http404()

    index = page_order.index(page_name)
    prev_page = index and page_order[index - 1] or None
    next_page = (index < len(page_order) - 1) and page_order[index + 1] or None
    prev_url = prev_page and reverse("pages", args=(prev_page,))
    this_url = reverse("pages", args=(page_name,))
    next_url = next_page and reverse("pages", args=(next_page,))

    url_data = {
        "index": index,
        "prev_page": prev_page,
        "next_page": next_page,
        "prev_url": prev_url,
        "this_url": this_url,
        "next_url": next_url,
    }
    return view_map[page_name](request, url_data)


@register("index")
def index_view(request, url_data):
    return render(request, "index.html", {**url_data})


class NameForm(forms.ModelForm):
    class Meta:
        model = models.Application
        fields = ["name"]


@register("name")
def name_view(request, url_data):
    user = request.user
    if request.method == "POST":
        form = NameForm(request.POST)
        if form.is_valid():
            application = models.Application(user=user, name=request.POST["name"])
            application.save()
            request.session["application_id"] = application.id
            return redirect(url_data["next_url"])
        else:
            data = request.POST
            errors = form.errors
    else:
        data = {}
        errors = {}
    return render(request, "name.html", {"errors": errors, "data": data, **url_data})


class ExemptionAdminForm(forms.ModelForm):
    class Meta:
        model = models.Application
        fields = ["hrbp", "grade", "title"]


@register("exemption")
def exemption_view(request, url_data):
    if request.method == "POST":
        application_id = request.session["application_id"]
        application = models.Application.get(application_id)
        form = ExemptionAdminForm(request.POST, instance=application)
        if form.is_valid():
            form.save()
            return redirect(url_data["next_url"])
        else:
            data = request.POST
            errors = form.errors
    else:
        data = {}
        errors = {}
    return render(
        request, "exemption.html", {"grades": models.Grades.options, "errors": errors, "data": data, **url_data}
    )
