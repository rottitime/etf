from django.contrib import admin
from django.urls import include, path

from etf.evaluation import views

api_urlpatterns = [
    path("evaluation-contributors/<uuid:evaluation_id>/", views.evaluation_contributors_view, name="evaluation-contributors"),
    path("evaluation-contributor-add/<uuid:evaluation_id>/", views.evaluation_contributor_add_view, name="evaluation-contributor-add"),
    path("evaluation-contributor-remove/<uuid:evaluation_id>/<str:remove_email>/", views.evaluation_contributors_view, name="evaluation-contributors")
]

urlpatterns = [
    path("", views.index_view, name="index"),
    path("evaluation/<uuid:evaluation_id>/", views.page_view, name="pages-index"),
    path("evaluation/<uuid:evaluation_id>/<str:page_name>", views.page_view, name="pages"),
    path("admin/", admin.site.urls),
    path("accounts/", include("allauth.urls")),
    path("search/", views.search_evaluations_view, name="search"),
    path("my-evaluations/", views.my_evaluations_view, name="my-evaluations"),
] + api_urlpatterns
