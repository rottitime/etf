from pkg_resources import evaluate_marker
from nose.tools import with_setup

from etf.evaluation import models
from etf.evaluation.views import get_adjacent_outcome_measure_id

from .utils import with_authenticated_client


def setup_eval():
    user = models.User.objects.get(email="peter.rabbit@example.com")
    evaluation = models.Evaluation(user=user, title="An Evaluation")
    evaluation.save()
    for i in range(3):
        name = f"Outcome measure {i}"
        outcome_measure = models.OutcomeMeasure(name=name, evaluation=evaluation)
        outcome_measure.save()


def teardown_eval():
    user = models.User.objects.get(email="peter.rabbit@example.com")
    user.delete()


@with_authenticated_client
@with_setup(setup_eval, teardown_eval)
def test_evaluation_urls(client):
    user = models.User.objects.get(email="peter.rabbit@example.com")
    evaluation = user.evaluations.all()[0]
    urls_to_test = [
        f"evaluation/{evaluation.id}/",
        f"evaluation/{evaluation.id}/title",
        f"evaluation/{evaluation.id}/description",
        f"evaluation/{evaluation.id}/end",
    ]
    for url in urls_to_test:
        response = client.get(url)
        assert response.status_code == 200


@with_authenticated_client
@with_setup(setup_eval, teardown_eval)
def test_evaluation_urls(client):
    user = models.User.objects.get(email="peter.rabbit@example.com")
    evaluation = user.evaluations.all()[0]
    outcome_measure = models.OutcomeMeasure.objects.filter(evaluation=evaluation).first()
    urls_to_test = [
        f"evaluation/{evaluation.id}/outcome-measures",
        f"evaluation/{evaluation.id}/outcome-measures/last",
        f"evaluation/{evaluation.id}/outcome-measures/first",
        f"evaluation/{evaluation.id}/outcome-measures/add",
        f"evaluation/{evaluation.id}/outcome-measures/{outcome_measure.id}",
        f"evaluation/{evaluation.id}/outcome-measures/{outcome_measure.id}/delete",
    ]
    for url in urls_to_test:
        response = client.get(url)
        assert response.status_code == 200
