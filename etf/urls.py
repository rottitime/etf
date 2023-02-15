from django.contrib import admin
from django.urls import include, path

from etf.evaluation import views, submission_views

urlpatterns = [
    path("", submission_views.index_view, name="index"),
    path("admin/", admin.site.urls),
    path("accounts/", include("allauth.urls")),
    path("search/", views.search_evaluations_view, name="search"),
    path("my-evaluations/", views.my_evaluations_view, name="my-evaluations"),
    path("evaluation-summary/<uuid:evaluation_id>/", views.evaluation_summary_view, name="evaluation-summary"),
    path("accounts/signup/", views.CustomSignupView.as_view(), name="account_signup"),
]

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

evaluation_entry_urlpatterns = [
    path("evaluation/<uuid:evaluation_id>/", submission_views.intro_page_view, name="intro"),
    path("evaluation/<uuid:evaluation_id>/title", submission_views.evaluation_title_view, name="title"),
    path(
        "evaluation/<uuid:evaluation_id>/description", submission_views.evaluation_description_view, name="description"
    ),
    path(
        "evaluation/<uuid:evaluation_id>/issue-description",
        submission_views.evaluation_issue_description_view,
        name="issue-description",
    ),
    path(
        "evaluation/<uuid:evaluation_id>/studied-population",
        submission_views.evaluation_studied_population_view,
        name="studied-population",
    ),
    path(
        "evaluation/<uuid:evaluation_id>/participant-recruitment",
        submission_views.evaluation_participant_recruitment,
        name="participant-recruitment",
    ),
    path(
        "evaluation/<uuid:evaluation_id>/evaluation-costs",
        submission_views.evaluation_costs_view,
        name="evaluation-costs",
    ),
    path(
        "evaluation/<uuid:evaluation_id>/policy-costs",
        submission_views.evaluation_policy_costs_view,
        name="policy-costs",
    ),
    path(
        "evaluation/<uuid:evaluation_id>/publication-intention",
        submission_views.evaluation_publication_intention_view,
        name="publication-intention",
    ),
    path(
        "evaluation/<uuid:evaluation_id>/documents",
        submission_views.evaluation_documents_view,
        name="documents",
    ),
    path("evaluation/<uuid:evaluation_id>/end", submission_views.end_page_view, name="end"),
]

outcome_measure_urlpatterns = [
    path(
        "evaluation/<uuid:evaluation_id>/outcome-measures",
        submission_views.initial_outcome_measure_page_view,
        name="outcome-measures",
    ),
    path(
        "evaluation/<uuid:evaluation_id>/outcome-measures/last",
        submission_views.last_outcome_measure_page_view,
        name="outcome-measure-last",
    ),
    path(
        "evaluation/<uuid:evaluation_id>/outcome-measures/first",
        submission_views.first_outcome_measure_page_view,
        name="outcome-measure-first",
    ),
    path(
        "evaluation/<uuid:evaluation_id>/outcome-measures/last",
        submission_views.last_outcome_measure_page_view,
        name="outcome-measure-last",
    ),
    path(
        "evaluation/<uuid:evaluation_id>/outcome-measures/<int:outcome_measure_id>",
        submission_views.outcome_measure_page_view,
        name="outcome-measure-page",
    ),
    path(
        "evaluation/<uuid:evaluation_id>/outcome-measures/<int:outcome_measure_id>/delete",
        submission_views.delete_outcome_measure_page_view,
        name="outcome-measure-delete",
    ),
    path("evaluation/<uuid:evaluation_id>/end", submission_views.end_page_view, name="end"),
]

urlpatterns = urlpatterns + api_urlpatterns + evaluation_entry_urlpatterns + outcome_measure_urlpatterns
