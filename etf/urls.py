from django.contrib import admin
from django.urls import include, path

from etf.evaluation import views

api_urlpatterns = [
    path(
        "evaluation-contributors/<uuid:evaluation_id>/",
        views.EvaluationContributor,
        name="evaluation-contributors",
    ),
    path(
        "evaluation-contributors/<uuid:evaluation_id>/<str:email_to_remove>/",
        views.EvaluationContributor,
        name="evaluation-contributors",
    ),
    path(
        "evaluation-contributor-add/<uuid:evaluation_id>/",
        views.evaluation_contributor_add_view,
        name="evaluation-contributor-add",
    ),
    path(
        "evaluation-contributor-remove/<uuid:evaluation_id>/",
        views.evaluation_contributor_remove_view,
        name="evaluation-contributor-remove",
    ),
    path(
        "evaluation-contributor-remove/<uuid:evaluation_id>/<str:email_to_remove>/",
        views.evaluation_contributor_remove_view,
        name="evaluation-contributor-remove",
    ),
]

urlpatterns = [
    path("", views.index_view, name="index"),
    path("accounts/signup/", views.CustomSignupView.as_view(), name="account_signup"),
    path("evaluation/<uuid:evaluation_id>/", views.page_view, name="pages-index"),
    path("evaluation/<uuid:evaluation_id>/<str:page_name>", views.page_view, name="pages"),
    path("evaluation/<uuid:evaluation_id>/outcome-measures/<int:outcome_id>", views.page_view, name="outcome-measures"),
    path("evaluation/<uuid:evaluation_id>/outcome-measures", views.page_view),
    #    path("evaluation/<uuid:evaluation_id>/outcome-measures/<int:outcome_id>/delete"),
    path("evaluation/<uuid:evaluation_id>/", views.intro_page_view, name="intro"),
    path("evaluation/<uuid:evaluation_id>/title", views.evaluation_title_view, name="title"),
    path("evaluation/<uuid:evaluation_id>/description", views.evaluation_description_view, name="description"),
    path(
        "evaluation/<uuid:evaluation_id>/outcome-measures",
        views.initial_outcome_measure_page_view,
        name="outcome-measures",
    ),
    path(
        "evaluation/<uuid:evaluation_id>/outcome-measures/add",
        views.add_outcome_measure_page_view,
        name="outcome-measure-add",
    ),
    path(
        "evaluation/<uuid:evaluation_id>/outcome-measures/<int:outcome_measure_id>",
        views.outcome_measure_page_view,
        name="outcome-measure-page",
    ),
    path("evaluation/<uuid:evaluation_id>/end", views.end_page_view, name="end"),
    path("admin/", admin.site.urls),
    path("accounts/", include("allauth.urls")),
    path("search/", views.search_evaluations_view, name="search"),
    path("my-evaluations/", views.my_evaluations_view, name="my-evaluations"),
    path("evaluation-summary/<uuid:evaluation_id>/", views.evaluation_summary_view, name="evaluation-summary"),
] + api_urlpatterns
