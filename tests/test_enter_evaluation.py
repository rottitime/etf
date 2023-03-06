from nose.tools import with_setup

from etf.evaluation import models
from . import utils


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
    other_measure = models.OtherMeasure(name="Other measure 1", evaluation=evaluation)
    other_measure.save()
    intervention = models.Intervention(name="Intervention 1", evaluation=evaluation)
    intervention.save()
    for i in range(2):
        name = f"Process {i}"
        process = models.ProcessStandard(name=name, evaluation=evaluation)
        process.save()


def teardown_eval():
    user = models.User.objects.get(email="peter.rabbit@example.com")
    user.delete()


@utils.with_authenticated_client
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


@utils.with_authenticated_client
@with_setup(setup_eval, teardown_eval)
def test_outcome_measure_urls(client):
    user = models.User.objects.get(email="peter.rabbit@example.com")
    evaluation = user.evaluations.all()[0]
    outcome_measure = models.OutcomeMeasure.objects.filter(evaluation=evaluation).first()
    urls_to_test = [
        f"evaluation/{evaluation.id}/outcome-measures/",
        f"evaluation/{evaluation.id}/outcome-measures/{outcome_measure.id}/",
    ]
    for url in urls_to_test:
        response = client.get(url)
        assert response.status_code == 200


@utils.with_authenticated_client
@with_setup(setup_eval, teardown_eval)
def test_other_measure_urls(client):
    user = models.User.objects.get(email="peter.rabbit@example.com")
    evaluation = user.evaluations.all()[0]
    other_measure = models.OtherMeasure.objects.filter(evaluation=evaluation).first()
    urls_to_test = [
        f"evaluation/{evaluation.id}/other-measures/",
        f"evaluation/{evaluation.id}/other-measures/{other_measure.id}/",
    ]
    for url in urls_to_test:
        response = client.get(url)
        assert response.status_code == 200


@utils.with_authenticated_client
@with_setup(setup_eval, teardown_eval)
def test_intervention_measure_urls(client):
    user = models.User.objects.get(email="peter.rabbit@example.com")
    evaluation = user.evaluations.all()[0]
    intervention = models.Intervention.objects.filter(evaluation=evaluation).first()
    urls_to_test = [
        f"evaluation/{evaluation.id}/interventions/",
        f"evaluation/{evaluation.id}/interventions/{intervention.id}/",
    ]
    for url in urls_to_test:
        response = client.get(url)
        assert response.status_code == 200


@utils.with_authenticated_client
@with_setup(setup_eval, teardown_eval)
def test_processes_standards_measure_urls(client):
    user = models.User.objects.get(email="peter.rabbit@example.com")
    evaluation = user.evaluations.all()[0]
    process = models.ProcessStandard.objects.filter(evaluation=evaluation).first()
    urls_to_test = [
        f"evaluation/{evaluation.id}/processes-standards/",
        f"evaluation/{evaluation.id}/processes-standards/{process.id}/",
    ]
    for url in urls_to_test:
        response = client.get(url)
        assert response.status_code == 200


def test_step_through_evaluation():
    authenticated_user = {"email": "mr_evaluation_test@example.com", "password": "1-h4t3-p455w0rd-c0mpl3xity-53tt1ng5"}
    client = utils.make_testino_client()
    utils.register(client, **authenticated_user)
    page = client.get("/")
    print(page)
    assert page.status_code == 200, page.status_code
    form = page.get_form("""form[action="/"]""")
    page = form.submit().follow()
    assert page.has_text("Enter your evaluation")
    assert page.status_code == 200, page.status_code
