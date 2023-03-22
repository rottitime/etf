from django.contrib import admin
from django.urls import include, path

from etf.evaluation import (
    authentication_views,
    download_views,
    submission_views,
    views,
)

urlpatterns = [
    path("", submission_views.index_view, name="index"),
    path("admin/", admin.site.urls),
    path("accounts/verify/", authentication_views.CustomVerifyUserEmail, name="verify-email"),
    path("accounts/password-reset/", authentication_views.PasswordReset, name="password-reset"),
    path("accounts/change-password/reset/", authentication_views.PasswordChange, name="password-set"),
    path("accounts/login/", authentication_views.CustomLoginView, name="account_login"),
    path("accounts/signup/", authentication_views.CustomSignupView.as_view(), name="account_signup"),
    path("accounts/verify/resend/", authentication_views.CustomResendVerificationView, name="resend-verify-email"),
    path("accounts/", include("allauth.urls")),
    path("search/", views.search_evaluations_view, name="search"),
    path("test/", views.search_evaluations_view, name="test"),
    path("evaluation-search/", views.EvaluationSearchView, name="evaluation-search"),
    path("my-evaluations/", views.my_evaluations_view, name="my-evaluations"),
    path("evaluation-summary/<uuid:evaluation_id>/", views.evaluation_summary_view, name="evaluation-summary"),
    path(
        "evaluation/<uuid:evaluation_id>/overview/",
        submission_views.evaluation_overview_view,
        name="evaluation-overview",
    ),
    path("data-download/", download_views.download_page_view, name="data-download"),
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
    path("evaluation/<uuid:evaluation_id>/title/", submission_views.evaluation_title_view, name="title"),
    path(
        "evaluation/<uuid:evaluation_id>/description/", submission_views.evaluation_description_view, name="description"
    ),
    path(
        "evaluation/<uuid:evaluation_id>/issue-description/",
        submission_views.evaluation_issue_description_view,
        name="issue-description",
    ),
    path(
        "evaluation/<uuid:evaluation_id>/studied-population/",
        submission_views.evaluation_studied_population_view,
        name="studied-population",
    ),
    path(
        "evaluation/<uuid:evaluation_id>/participant-recruitment/",
        submission_views.evaluation_participant_recruitment,
        name="participant-recruitment",
    ),
    path(
        "evaluation/<uuid:evaluation_id>/policy-costs/",
        submission_views.evaluation_policy_costs_view,
        name="policy-costs",
    ),
    path(
        "evaluation/<uuid:evaluation_id>/publication-intention/",
        submission_views.evaluation_publication_intention_view,
        name="publication-intention",
    ),
    path(
        "evaluation/<uuid:evaluation_id>/evaluation-types/",
        submission_views.evaluation_types_view,
        name="evaluation-types",
    ),
    path(
        "evaluation/<uuid:evaluation_id>/impact-design/",
        submission_views.evaluation_impact_eval_design_view,
        name="impact-design",
    ),
    path(
        "evaluation/<uuid:evaluation_id>/impact-analysis/",
        submission_views.evaluation_impact_eval_analysis_view,
        name="impact-analysis",
    ),
    path(
        "evaluation/<uuid:evaluation_id>/process-design/",
        submission_views.evaluation_process_eval_design_view,
        name="process-design",
    ),
    path(
        "evaluation/<uuid:evaluation_id>/process-analysis/",
        submission_views.evaluation_process_eval_analysis_view,
        name="process-analysis",
    ),
    path(
        "evaluation/<uuid:evaluation_id>/economic-design/",
        submission_views.evaluation_economic_eval_design_view,
        name="economic-design",
    ),
    path(
        "evaluation/<uuid:evaluation_id>/economic-analysis/",
        submission_views.evaluation_economic_eval_analysis_view,
        name="economic-analysis",
    ),
    path(
        "evaluation/<uuid:evaluation_id>/other-design/",
        submission_views.evaluation_other_eval_design_view,
        name="other-design",
    ),
    path(
        "evaluation/<uuid:evaluation_id>/other-analysis/",
        submission_views.evaluation_other_eval_analysis_view,
        name="other-analysis",
    ),
    path(
        "evaluation/<uuid:evaluation_id>/ethics/",
        submission_views.evaluation_ethics_view,
        name="ethics",
    ),
    path(
        "evaluation/<uuid:evaluation_id>/impact-findings/",
        submission_views.evaluation_impact_findings_view,
        name="impact-findings",
    ),
    path(
        "evaluation/<uuid:evaluation_id>/economic-findings/",
        submission_views.evaluation_economic_findings_view,
        name="economic-findings",
    ),
    path(
        "evaluation/<uuid:evaluation_id>/process-findings/",
        submission_views.evaluation_process_findings_view,
        name="process-findings",
    ),
    path(
        "evaluation/<uuid:evaluation_id>/other-findings/",
        submission_views.evaluation_other_findings_view,
        name="other-findings",
    ),
    path(
        "evaluation/<uuid:evaluation_id>/metadata/",
        submission_views.evaluation_metadata_view,
        name="metadata",
    ),
    path(
        "evaluation/<uuid:evaluation_id>/status/",
        submission_views.evaluation_status_view,
        name="status",
    ),
    path("evaluation/<uuid:evaluation_id>/end/", submission_views.end_page_view, name="end"),
]

intervention_urlpatterns = [
    path(
        "evaluation/<uuid:evaluation_id>/interventions/",
        submission_views.summary_interventions_page_view,
        name="interventions",
    ),
    path(
        "evaluation/<uuid:evaluation_id>/interventions/<uuid:intervention_id>/",
        submission_views.intervention_page_view,
        name="intervention-page",
    ),
]


outcome_measure_urlpatterns = [
    path(
        "evaluation/<uuid:evaluation_id>/outcome-measures/",
        submission_views.summary_outcome_measure_page_view,
        name="outcome-measures",
    ),
    path(
        "evaluation/<uuid:evaluation_id>/outcome-measures/<uuid:outcome_measure_id>/",
        submission_views.outcome_measure_page_view,
        name="outcome-measure-page",
    ),
]


other_measure_urlpatterns = [
    path(
        "evaluation/<uuid:evaluation_id>/other-measures/",
        submission_views.summary_other_measure_page_view,
        name="other-measures",
    ),
    path(
        "evaluation/<uuid:evaluation_id>/other-measures/<uuid:other_measure_id>/",
        submission_views.other_measure_page_view,
        name="other-measure-page",
    ),
]


processes_standards_urlpatterns = [
    path(
        "evaluation/<uuid:evaluation_id>/processes-standards/",
        submission_views.summary_processes_standards_page_view,
        name="processes-standards",
    ),
    path(
        "evaluation/<uuid:evaluation_id>/processes-standards/<uuid:process_standard_id>/",
        submission_views.process_standard_page_view,
        name="processes-standard-page",
    ),
]

evaluation_costs_urlpatterns = [
    path(
        "evaluation/<uuid:evaluation_id>/evaluation-costs/",
        submission_views.summary_evaluation_costs_page_view,
        name="evaluation-costs",
    ),
    path(
        "evaluation/<uuid:evaluation_id>/evaluation-costs/<uuid:evaluation_cost_id>/",
        submission_views.evaluation_cost_page_view,
        name="evaluation-cost-page",
    ),
]


documents_urlpatterns = [
    path(
        "evaluation/<uuid:evaluation_id>/documents/",
        submission_views.summary_documents_page_view,
        name="documents",
    ),
    path(
        "evaluation/<uuid:evaluation_id>/documents/<uuid:document_id>/",
        submission_views.document_page_view,
        name="document-page",
    ),
]

links_urlpatterns = [
    path(
        "evaluation/<uuid:evaluation_id>/links/",
        submission_views.summary_links_page_view,
        name="links",
    ),
    path(
        "evaluation/<uuid:evaluation_id>/links/<uuid:link_id>/",
        submission_views.links_page_view,
        name="link-page",
    ),
]


event_date_urlpatterns = [
    path(
        "evaluation/<uuid:evaluation_id>/event-dates/",
        submission_views.summary_event_dates_page_view,
        name="event-dates",
    ),
    path(
        "evaluation/<uuid:evaluation_id>/event-dates/<uuid:event_date_id>/",
        submission_views.event_date_page_view,
        name="event-date-page",
    ),
]


urlpatterns = (
    urlpatterns
    + api_urlpatterns
    + evaluation_entry_urlpatterns
    + intervention_urlpatterns
    + outcome_measure_urlpatterns
    + other_measure_urlpatterns
    + processes_standards_urlpatterns
    + evaluation_costs_urlpatterns
    + documents_urlpatterns
    + links_urlpatterns
    + event_date_urlpatterns
)

handler404 = "etf.evaluation.views.view_404"
