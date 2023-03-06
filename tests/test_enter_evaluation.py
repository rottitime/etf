from nose.tools import with_setup

from etf.evaluation import models, enums
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
    # Setup evaluation
    authenticated_user = {"email": "test-evaluation-data-entry@example.com", "password": "giraffe47"}
    client = utils.make_testino_client()
    utils.register(client, **authenticated_user)
    evaluation = models.Evaluation()
    evaluation.save()
    intro_page = client.get(f"/evaluation/{evaluation.id}/")

    # Intro page
    assert intro_page.status_code == 200, intro_page.status_code
    assert intro_page.has_text("Enter your evaluation")
    assert intro_page.has_text("Next")
    # selector = testino.XPath('//a[contains(text(), "Next")]')
    # Add once figured out how to circumvent `one` having a warning
    # page.one(selector)
    title_page = intro_page.click(contains="Next")

    # Title page
    assert title_page.status_code == 200, title_page.status_code
    assert title_page.has_text("Title")
    title_form = title_page.get_form("""form:not([action])""")
    title_form["title"] = "Test evaluation title"
    title_form["short_title"] = "Test evaluation"
    description_page = title_form.submit().follow()

    # Description page
    assert description_page.status_code == 200, description_page.status_code
    assert description_page.has_text("Description")
    assert description_page.has_text("Save and next")
    evaluation = models.Evaluation.objects.get(pk=evaluation.id)
    assert evaluation.title == "Test evaluation title"
    assert evaluation.short_title == "Test evaluation"
    description_form = description_page.get_form("""form:not([action])""")
    description_form["brief_description"] = "A brief description of the evaluation"
    description_form["topics"] = [models.Topic.BREXIT.value]
    description_form["organisations"] = [enums.Organisation.choices[0][0]]
    issue_description_page = description_form.submit().follow()

    # Issue description page
    assert issue_description_page.status_code == 200, issue_description_page.status_code
    assert issue_description_page.has_text("Issue description")
    assert issue_description_page.has_text("Save and next")
    evaluation = models.Evaluation.objects.get(pk=evaluation.id)
    assert evaluation.brief_description == "A brief description of the evaluation"
    assert evaluation.topics == [models.Topic.BREXIT.value]
    assert evaluation.organisations == [enums.Organisation.choices[0][0]]
    issue_description_form = issue_description_page.get_form("""form:not([action])""")
    issue_description_form["issue_description"] = "A brief description of the evaluation issue"
    issue_description_form["those_experiencing_issue"] = "The people who are experiencing this issue"
    issue_description_form["why_improvements_matter"] = "A statement about why the improvements matter"
    issue_description_form["who_improvements_matter_to"] = "A summary of the peoples the improvements matter to"
    issue_description_form["current_practice"] = "What the current practice is in relation to the issue"
    issue_description_form["issue_relevance"] = "How relevant is the issue to society"
    studied_population_page = issue_description_form.submit().follow()

    # Studied population page
    assert studied_population_page.status_code == 200, studied_population_page.status_code
    assert studied_population_page.has_text("Issue description")
    assert studied_population_page.has_text("Save and next")
    evaluation = models.Evaluation.objects.get(pk=evaluation.id)
    assert evaluation.issue_description == "A brief description of the evaluation issue"
    assert evaluation.those_experiencing_issue == "The people who are experiencing this issue"
    assert evaluation.why_improvements_matter == "A statement about why the improvements matter"
    assert evaluation.who_improvements_matter_to == "A summary of the peoples the improvements matter to"
    assert evaluation.current_practice == "What the current practice is in relation to the issue"
    assert evaluation.issue_relevance == "How relevant is the issue to society"
    studied_population_form = studied_population_page.get_form("""form:not([action])""")
    studied_population_form["studied_population"] = "A brief description of the target population"
    studied_population_form["eligibility_criteria"] = "The criteria the population have to meet to be included"
    studied_population_form["sample_size"] = 1000
    studied_population_form["sample_size_units"] = "A unit of measurement"
    studied_population_form["sample_size_details"] = "Any details about the same size"
    participant_recruitment_page = studied_population_form.submit().follow()

    # Studied population page
    assert participant_recruitment_page.status_code == 200, participant_recruitment_page.status_code
    assert participant_recruitment_page.has_text("Participant recruitment")
    assert participant_recruitment_page.has_text("Save and next")
    evaluation = models.Evaluation.objects.get(pk=evaluation.id)
    assert evaluation.studied_population == "A brief description of the target population"
    assert evaluation.eligibility_criteria == "The criteria the population have to meet to be included"
    assert evaluation.sample_size == 1000
    assert evaluation.sample_size_units == "A unit of measurement"
    assert evaluation.sample_size_details == "Any details about the same size"
    participant_recruitment_form = participant_recruitment_page.get_form("""form:not([action])""")
    participant_recruitment_form["process_for_recruitment"] = "A summary of the process for recruitment"
    participant_recruitment_form["recruitment_schedule"] = "A recruitment schedule"
    evaluation_cost_page = participant_recruitment_form.submit().follow()

    # Evaluation cost page
    assert evaluation_cost_page.status_code == 200, evaluation_cost_page.status_code
    assert evaluation_cost_page.has_text("Evaluation costs")
    assert evaluation_cost_page.has_text("Save and next")
    evaluation = models.Evaluation.objects.get(pk=evaluation.id)
    assert evaluation.process_for_recruitment == "A summary of the process for recruitment"
    assert evaluation.recruitment_schedule == "A recruitment schedule"
