from django import forms
from django.contrib.auth import login
from django.forms.models import model_to_dict
from django.http import Http404
from django.shortcuts import redirect, render
from django.urls import reverse

page_order = (
    "index",
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
