from django.contrib import admin
from django.urls import include, path

from etf.evaluation import views

urlpatterns = [
    path("", views.index_view, name="index"),
    path("evaluation/<uuid:evaluation_id>/", views.page_view, name="pages-index"),
    path("evaluation/<uuid:evaluation_id>/<str:page_name>", views.page_view, name="pages"),
    path("admin/", admin.site.urls),
    path("accounts/", include("allauth.urls")),
    path("search/", views.search_evaluations_view, name="search"),
]
