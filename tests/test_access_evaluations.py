from django.urls import reverse
from nose import with_setup

from etf import urls
from etf.evaluation import models

from . import utils


# Explicitly excluding URLs, to ensure that we don't miss out new URLs
EDIT_OR_VIEW_EVALUATION_URL_PATTERNS = (
    set(urls.urlpatterns)
    - set(urls.initial_urlpatterns)
    - set(urls.account_urlpatterns)
    - set(urls.feedback_and_help_urlpatterns)
    - set(urls.debug_urlpatterns)
)

VIEW_EVALUATION_URL_PATTERNS = (
    set(urls.urlpatterns)
    - set(urls.initial_urlpatterns)
    - set(urls.account_urlpatterns)
    - set(urls.feedback_and_help_urlpatterns)
    - set(urls.evaluation_edit_patterns)
    - set(urls.debug_urlpatterns)
)


# Non-standard URLs - explicitly write tests
NAMES_TO_IGNORE = [
    "evaluation-contributor-remove",
    "create-evaluation",
    "evaluation-overview",
]


RELATED_OBJECTS = {
    "intervention-page": "Intervention",
    "outcome-measure-page": "OutcomeMeasure",
    "other-measure-page": "OtherMeasure",
    "processes-standard-page": "ProcessStandard",
    "evaluation-cost-page": "EvaluationCost",
    "document-page": "Document",
    "link-page": "LinkOtherService",
    "event-date-page": "EventDate",
    "grant-page": "Grant",
}


def get_url_for_evaluation_and_related_object(client, url_name, evaluation_id, related_id=None):
    if (url_name in NAMES_TO_IGNORE) or (url_name in RELATED_OBJECTS.keys()):
        return
    if related_id:
        url = reverse(url_name, args=(evaluation_id, related_id))
    else:
        url = reverse(url_name, args=(evaluation_id,))
    response = client.get(url)
    return response


@with_setup(utils.create_fake_evaluations, utils.remove_fake_evaluations)
@utils.with_authenticated_client
def test_edit_or_view_evaluations(client):
    evaluation_not_editable = models.Evaluation.objects.filter(title="Draft evaluation 1").first()
    for url_pattern in EDIT_OR_VIEW_EVALUATION_URL_PATTERNS:
        response = get_url_for_evaluation_and_related_object(client, url_pattern.name, evaluation_not_editable.id)
        if response:
            assert response.status_code == 404, response.status_code


# TODO - test edit only

# TODO - test can view but not edit some


@with_setup(utils.create_fake_evaluations, utils.remove_fake_evaluations)
@utils.with_authenticated_client
def test_edit_or_view_related_objects(client):
    evaluation_not_editable = models.Evaluation.objects.filter(title="Draft evaluation 1").first()
    for url_name, model_name in RELATED_OBJECTS.items():
        model = getattr(models, model_name)
        new_obj = model(evaluation=evaluation_not_editable)
        new_obj.save()
        related_id = new_obj.id
        response = get_url_for_evaluation_and_related_object(client, url_name, evaluation_not_editable.id, related_id)
        if response:
            assert response.status_code == 404, response.status_code
