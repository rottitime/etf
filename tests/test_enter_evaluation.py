from nose.tools import with_setup

from etf.evaluation import models
from etf.evaluation.submission_views import get_adjacent_id_for_model

from .utils import with_authenticated_client


def setup_eval():
    user, _ = models.User.objects.get_or_create(email="peter.rabbit@example.com")
    user.save()
    evaluation = models.Evaluation(title="An Evaluation")
    evaluation.save()
    evaluation.users.add(user)
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
def test_outcome_measure_urls(client):
    user = models.User.objects.get(email="peter.rabbit@example.com")
    evaluation = user.evaluations.all()[0]
    outcome_measure = models.OutcomeMeasure.objects.filter(evaluation=evaluation).first()
    urls_to_test = [
        f"evaluation/{evaluation.id}/outcome-measures",
        f"evaluation/{evaluation.id}/outcome-measures/last",
        f"evaluation/{evaluation.id}/outcome-measures/first",
        f"evaluation/{evaluation.id}/outcome-measures/{outcome_measure.id}",
        f"evaluation/{evaluation.id}/outcome-measures/{outcome_measure.id}/delete",
    ]
    for url in urls_to_test:
        response = client.get(url)
        assert response.status_code == 200


@with_setup(setup_eval, teardown_eval)
def test_get_adjacent_id_for_model():
    user = models.User.objects.get(email="peter.rabbit@example.com")
    evaluation = user.evaluations.all().first()
    outcome_measures = evaluation.outcome_measures.all().order_by("created_at")
    outcome_ids = list(outcome_measures.values_list("id", flat=True))
    outcome_id = get_adjacent_id_for_model(
        evaluation.id, outcome_ids[1], model_name="OutcomeMeasure", next_or_prev="next"
    )
    assert outcome_id == outcome_ids[2]
    outcome_id = get_adjacent_id_for_model(
        evaluation.id, outcome_ids[1], model_name="OutcomeMeasure", next_or_prev="prev"
    )
    assert outcome_id == outcome_ids[0]
    outcome_id = get_adjacent_id_for_model(
        evaluation.id, outcome_ids[2], model_name="OutcomeMeasure", next_or_prev="next"
    )
    assert not outcome_id
    outcome_id = get_adjacent_id_for_model(
        evaluation.id, outcome_ids[0], model_name="OutcomeMeasure", next_or_prev="prev"
    )
    assert not outcome_id
