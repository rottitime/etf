from django.contrib import admin
from django.urls import include, path

from etf.evaluation import submission_views, views

urlpatterns = [
    path("", submission_views.index_view, name="index"),
    path("admin/", admin.site.urls),
    path("accounts/", include("allauth.urls")),
    path("search/", views.search_evaluations_view, name="search"),
    path("accounts/password-reset/", views.PasswordReset, name="password-reset"),
    path("accounts/change-password/reset/", views.PasswordChange, name="password-set"),
    path("my-evaluations/", views.my_evaluations_view, name="my-evaluations"),
    path("evaluation-summary/<uuid:evaluation_id>/", views.evaluation_summary_view, name="evaluation-summary"),
    path(
        "evaluation/<uuid:evaluation_id>/overview",
        submission_views.evaluation_overview_view,
        name="evaluation-overview",
    ),
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
    path(
        "evaluation/<uuid:evaluation_id>/event-dates",
        submission_views.evaluation_event_dates_view,
        name="event-dates",
    ),
    path(
        "evaluation/<uuid:evaluation_id>/evaluation-types",
        submission_views.evaluation_types_view,
        name="evaluation-types",
    ),
    path(
        "evaluation/<uuid:evaluation_id>/impact-design",
        submission_views.evaluation_impact_eval_design_view,
        name="impact-design",
    ),
    path(
        "evaluation/<uuid:evaluation_id>/impact-analysis",
        submission_views.evaluation_impact_eval_analysis_view,
        name="impact-analysis",
    ),
    path(
        "evaluation/<uuid:evaluation_id>/process-design",
        submission_views.evaluation_process_eval_design_view,
        name="process-design",
    ),
    path(
        "evaluation/<uuid:evaluation_id>/process-analysis",
        submission_views.evaluation_process_eval_analysis_view,
        name="process-analysis",
    ),
    path(
        "evaluation/<uuid:evaluation_id>/economic-design",
        submission_views.evaluation_economic_eval_design_view,
        name="economic-design",
    ),
    path(
        "evaluation/<uuid:evaluation_id>/economic-analysis",
        submission_views.evaluation_economic_eval_analysis_view,
        name="economic-analysis",
    ),
    path(
        "evaluation/<uuid:evaluation_id>/other-design",
        submission_views.evaluation_other_eval_design_view,
        name="other-design",
    ),
    path(
        "evaluation/<uuid:evaluation_id>/other-analysis",
        submission_views.evaluation_other_eval_analysis_view,
        name="other-analysis",
    ),
    path(
        "evaluation/<uuid:evaluation_id>/other-measures",
        submission_views.evaluation_other_measures_view,
        name="other-measures",
    ),
    path(
        "evaluation/<uuid:evaluation_id>/ethics",
        submission_views.evaluation_ethics_view,
        name="ethics",
    ),
    path(
        "evaluation/<uuid:evaluation_id>/impact-findings",
        submission_views.evaluation_impact_findings_view,
        name="impact-findings",
    ),
    path(
        "evaluation/<uuid:evaluation_id>/economic-findings",
        submission_views.evaluation_economic_findings_view,
        name="economic-findings",
    ),
    path(
        "evaluation/<uuid:evaluation_id>/process-findings",
        submission_views.evaluation_process_findings_view,
        name="process-findings",
    ),
    path(
        "evaluation/<uuid:evaluation_id>/other-findings",
        submission_views.evaluation_other_findings_view,
        name="other-findings",
    ),
    path(
        "evaluation/<uuid:evaluation_id>/links",
        submission_views.evaluation_links_view,
        name="links",
    ),
    path(
        "evaluation/<uuid:evaluation_id>/metadata",
        submission_views.evaluation_metadata_view,
        name="metadata",
    ),
    path(
        "evaluation/<uuid:evaluation_id>/status",
        submission_views.evaluation_status_view,
        name="status",
    ),
    path("evaluation/<uuid:evaluation_id>/end", submission_views.end_page_view, name="end"),
]

intervention_urlpatterns = [
    path(
        "evaluation/<uuid:evaluation_id>/interventions/",
        submission_views.initial_interventions_page_view,
        name="interventions",
    ),
    path(
        "evaluation/<uuid:evaluation_id>/interventions/first/",
        submission_views.first_intervention_page_view,
        name="intervention-first",
    ),
    path(
        "evaluation/<uuid:evaluation_id>/interventions/last/",
        submission_views.last_intervention_page_view,
        name="intervention-last",
    ),
    path(
        "evaluation/<uuid:evaluation_id>/intervention/<int:intervention_id>/",
        submission_views.intervention_page_view,
        name="intervention-page",
    ),
    path(
        "evaluation/<uuid:evaluation_id>/interventions/<int:intervention_id>/delete/",
        submission_views.delete_intervention_page_view,
        name="intervention-delete",
    ),
]

outcome_measure_urlpatterns = [
    path(
        "evaluation/<uuid:evaluation_id>/outcome-measures",
        submission_views.initial_outcome_measure_page_view,
        name="outcome-measures",
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
]


other_measure_urlpatterns = [
    path(
        "evaluation/<uuid:evaluation_id>/other-measures/",
        submission_views.initial_other_measure_page_view,
        name="other-measures",
    ),
    path(
        "evaluation/<uuid:evaluation_id>/other-measures/first/",
        submission_views.first_other_measure_page_view,
        name="other-measure-first",
    ),
    path(
        "evaluation/<uuid:evaluation_id>/other-measures/last/",
        submission_views.last_other_measure_page_view,
        name="other-measure-last",
    ),
    path(
        "evaluation/<uuid:evaluation_id>/other-measures/<int:other_measure_id>/",
        submission_views.other_measure_page_view,
        name="other-measure-page",
    ),
    path(
        "evaluation/<uuid:evaluation_id>/other-measures/<int:other_measure_id>/delete/",
        submission_views.delete_other_measure_page_view,
        name="other-measure-delete",
    ),
]


processes_standards_urlpatterns = [
    path(
        "evaluation/<uuid:evaluation_id>/processes-standards/",
        submission_views.initial_processes_standards_page_view,
        name="processes-standards-initial",
    ),
    path(
        "evaluation/<uuid:evaluation_id>/processes-standards/first/",
        submission_views.first_process_standard_page_view,
        name="process-standard-first",
    ),
    path(
        "evaluation/<uuid:evaluation_id>/processes-standards/last/",
        submission_views.last_process_standard_page_view,
        name="process-standard-last",
    ),
    path(
        "evaluation/<uuid:evaluation_id>/processes-standards/<int:process_standard_id>/",
        submission_views.process_standard_page_view,
        name="process-standard-page",
    ),
    path(
        "evaluation/<uuid:evaluation_id>/processes-standards/<int:process_standard_id>/delete/",
        submission_views.delete_process_standard_page_view,
        name="process-standard-delete",
    ),
]


urlpatterns = (
    urlpatterns
    + api_urlpatterns
    + evaluation_entry_urlpatterns
    + outcome_measure_urlpatterns
    + intervention_urlpatterns
    + processes_standards_urlpatterns
)

handler404 = "etf.evaluation.views.view_404"
