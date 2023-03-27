from nose.tools import with_setup

from etf.evaluation import models


def test_name_field():
    evaluation = models.Evaluation()
    evaluation.save()

    evaluation_cost = models.EvaluationCost(evaluation=evaluation, item_name="Flooble")
    evaluation_cost.save()

    assert evaluation_cost.get_name() == "Flooble"
    evaluation_cost.set_name("Flim flam")
    evaluation_cost.save()

    assert evaluation_cost.item_name == "Flim flam"


def setup_search_eval():
    title = "Test search evaluation"
    test_eval = models.Evaluation(
        title=title,
        brief_description="Dancing elephants",
        organisations=["uk-health-security-agency", "department-for-education"],
    )
    test_eval.save()
    outcome_measure = models.OutcomeMeasure(evaluation=test_eval, name="My new outcome measure")
    outcome_measure.save()
    test_eval.save()


def teardown_search_eval():
    title = "Test search evaluation"
    models.Evaluation.objects.filter(title=title).delete()


@with_setup(setup_search_eval, teardown_search_eval)
def test_search_text():
    test_eval = models.Evaluation(
        title="Test search eval",
        brief_description="Dancing elephants",
        organisations=["uk-health-security-agency", "department-for-education"],
        economic_eval_type="COST_BENEFIT_ANALYSIS",
    )
    test_eval.save()
    outcome_measure = models.OutcomeMeasure(evaluation=test_eval, name="My new outcome measure")
    outcome_measure.save()
    test_eval.save()  # TODO - need to change save for related objects
    search_text = test_eval.search_text
    assert "elephants" in search_text, search_text
    assert "DfE" in search_text, search_text
    assert "My new outcome measure" in search_text, search_text
    assert "Cost-benefit analysis" in search_text, search_text
