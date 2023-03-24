from re import search
from nose.tools import with_setup

from etf.evaluation import choices, models


def test_name_field():
    evaluation = models.Evaluation()
    evaluation.save()

    evaluation_cost = models.EvaluationCost(evaluation=evaluation, item_name="Flooble")
    evaluation_cost.save()

    assert evaluation_cost.get_name() == "Flooble"
    evaluation_cost.set_name("Flim flam")
    evaluation_cost.save()

    assert evaluation_cost.item_name == "Flim flam"


def setup_evaluations():
    models.Evaluation.objects.all().delete()
    types_set_1 = []
    types_set_2 = [choices.EvaluationTypeOptions.PROCESS.value, "A new type"]
    types_set_3 = [choices.EvaluationTypeOptions.PROCESS.value, choices.EvaluationTypeOptions.ECONOMIC.value]
    types_set_4 = ["A different type"]
    types_set_5 = [choices.EvaluationTypeOptions.IMPACT.value, "Other type"]
    title = "test eval type options"
    models.Evaluation(title=title, evaluation_type=types_set_1).save()
    models.Evaluation(title=title, evaluation_type=types_set_2).save()
    models.Evaluation(title=title, evaluation_type=types_set_3).save()
    models.Evaluation(title=title, evaluation_type=types_set_4).save()
    models.Evaluation(title=title, evaluation_type=types_set_5).save()


def tear_down_evaluations():
    title = "test eval type options"
    models.Evaluation.objects.filter(title=title).delete()


@with_setup(setup_evaluations, tear_down_evaluations)
def test_get_values_other_evaluation_types():
    other_values, other_qs = models.get_values_other_evaluation_types()
    assert "A new type" in other_values, other_values
    assert other_qs.count() == 3, other_qs


def setup_search_eval():
    title = "Test search evaluation"
    test_eval = models.Evaluation(
        title=title,
        brief_description="Dancing elephants",
        organisations=["uk-health-security-agency", "department-for-education"],
    )
    outcome_measure = models.OutcomeMeasure(evaluation=test_eval, name="My new outcome measure")
    outcome_measure.save()
    test_eval.save()


def teardown_search_eval():
    title = "Test search evaluation"
    models.Evaluation.filter(title=title).delete()


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
    search_text = test_eval["search_text"]
    assert "elephants" in search_text, search_text
    assert "DfE" in search_text, search_text
    assert "My new outcome measure" in search_text
    assert "Cost-benefit analysis" in search_text
