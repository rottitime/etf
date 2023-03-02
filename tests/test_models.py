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
