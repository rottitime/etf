from django.urls import reverse
from nose import with_setup

from etf import urls
from etf.evaluation import models

from . import utils


# TODO - do this better
NAMES_TO_IGNORE = [
    "intervention-page",
    "outcome-measure-page",
    "other-measure-page",
    "processes-standard-page",
    "evaluation-cost-page",
    "document-page",
    "link-page",
    "event-date-page",
    "grant-page",
    "evaluation-contributor-remove",
    "create-evaluation",
    "evaluation-overview",
]

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


def get_url_for_evaluation(client, url_pattern, evaluation_id):
    name = url_pattern.name
    if name in NAMES_TO_IGNORE:
        return
    url = reverse(url_pattern.name, args=(evaluation_id,))
    response = client.get(url)
    return response


@with_setup(utils.create_fake_evaluations, utils.remove_fake_evaluations)
@utils.with_authenticated_client
def test_edit_evaluations(client):
    evaluation_not_editable = models.Evaluation.objects.filter(title="Draft evaluation 1").first()
    evaluation_editable = models.Evaluation.objects.filter(title="Draft evaluation 2").first()
    # for url_pattern in EDIT_OR_VIEW_EVALUATION_URL_PATTERNS:
    #     response = get_url_for_evaluation(client, url_pattern, evaluation_editable.id)
    #     if response:
    #         assert response.status_code == 200
    for url_pattern in EDIT_OR_VIEW_EVALUATION_URL_PATTERNS:
        response = get_url_for_evaluation(client, url_pattern, evaluation_not_editable.id)
        if response:
            assert response.status_code == 404
