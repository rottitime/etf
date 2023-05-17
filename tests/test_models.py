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
        economic_type="COST_BENEFIT_ANALYSIS",
    )
    test_eval.save()
    outcome_measure = models.OutcomeMeasure(evaluation=test_eval, name="My new outcome measure")
    outcome_measure.save()
    search_text = test_eval.search_text
    assert "elephants" in search_text, search_text
    assert "DfE" in search_text, search_text
    assert "My new outcome measure" in search_text, search_text
    assert "Cost-benefit analysis" in search_text, search_text


def test_user_save():
    new_email1 = "New_User1@example.org"
    new_email2 = "New_User2@Example.com"
    new_user1, _ = models.User.objects.update_or_create(email=new_email1)
    new_user2, _ = models.User.objects.update_or_create(email=new_email2)
    assert new_user1.email == "new_user1@example.org", new_user1.email
    assert new_user1.is_external_user, new_user1.is_external_user
    assert new_user2.email == "new_user2@example.com", new_user2.email
    assert not new_user2.is_external_user, new_user2.is_external_user
