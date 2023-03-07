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
    assert evaluation_cost_page.has_text("Evaluation costs and budget")
    assert evaluation_cost_page.has_text("Next")
    evaluation = models.Evaluation.objects.get(pk=evaluation.id)
    assert evaluation.process_for_recruitment == "A summary of the process for recruitment"
    assert evaluation.recruitment_schedule == "A recruitment schedule"
    add_cost_evaluation_form = evaluation_cost_page.get_form("""form:not([action])""")
    added_cost_evaluation_page = add_cost_evaluation_form.submit().follow()
    assert added_cost_evaluation_page.has_text("New evaluation cost")
    adding_cost_evaluation_page = added_cost_evaluation_page.click(contains="New evaluation cost")
    assert adding_cost_evaluation_page.has_text("Evaluation costs and budget")
    assert adding_cost_evaluation_page.has_text("Item cost (£)")
    adding_cost_evaluation_form = adding_cost_evaluation_page.get_form("""form:not([action])""")
    adding_cost_evaluation_form["item_name"] = "An example item cost"
    adding_cost_evaluation_form["description"] = "A description of the expense item"
    adding_cost_evaluation_form["item_cost"] = 1000
    adding_cost_evaluation_form["earliest_spend_date"] = "2022-03-07"
    adding_cost_evaluation_form["latest_spend_date"] = "2022-03-07"
    evaluation_cost_page = adding_cost_evaluation_form.submit(extra={"return": ""}).follow()
    assert evaluation_cost_page.has_text("An example item cost")
    deleting_cost_evaluation_page = evaluation_cost_page.click(contains="An example item cost")
    deleting_cost_evaluation_form = deleting_cost_evaluation_page.get_form("""form:not([action])""")
    assert deleting_cost_evaluation_form["item_name"] == "An example item cost"
    evaluation_cost_page = deleting_cost_evaluation_form.submit(extra={"delete": ""}).follow()
    assert evaluation_cost_page.has_text("Evaluation costs and budget")
    assert not evaluation_cost_page.has_text("An example item cost")
    assert not evaluation_cost_page.has_text("New evaluation cost")
    policy_costs_page = evaluation_cost_page.click(contains="Next")

    # Policy costs and budget page
    assert policy_costs_page.status_code == 200, policy_costs_page.status_code
    assert policy_costs_page.has_text("Policy costs and budget")
    assert policy_costs_page.has_text("Save and next")
    policy_costs_form = policy_costs_page.get_form("""form:not([action])""")
    publication_intention_page = policy_costs_form.submit().follow()

    # Publication intention page
    assert publication_intention_page.status_code == 200, publication_intention_page.status_code
    assert publication_intention_page.has_text("Publication intention")
    assert publication_intention_page.has_text("Save and next")
    publication_intention_form = publication_intention_page.get_form("""form:not([action])""")
    documents_page = publication_intention_form.submit().follow()

    # Documents page
    assert documents_page.status_code == 200, documents_page.status_code
    assert documents_page.has_text("Documents")
    assert documents_page.has_text("Next")
    add_document_form = documents_page.get_form("""form:not([action])""")
    added_document_page = add_document_form.submit().follow()
    assert added_document_page.has_text("New document")
    adding_document_page = added_document_page.click(contains="New document")
    assert adding_document_page.has_text("Link to document")
    assert adding_document_page.has_text("Document type")
    adding_document_form = adding_document_page.get_form("""form:not([action])""")
    adding_document_form["title"] = "An example document"
    adding_document_form["url"] = "https://example.com"
    adding_document_form["document_types"] = [models.DocumentType.ANALYSIS_CODE.value]
    adding_document_form["description"] = "A description of an example document"
    document_page = adding_document_form.submit(extra={"return": ""}).follow()
    assert document_page.has_text("An example document")
    deleting_document_page = document_page.click(contains="An example document")
    deleting_document_page = deleting_document_page.get_form("""form:not([action])""")
    assert deleting_document_page["title"] == "An example document"
    document_page = deleting_document_page.submit(extra={"delete": ""}).follow()
    assert document_page.has_text("Documents")
    assert not document_page.has_text("An example document")
    assert not document_page.has_text("New document")
    event_dates_page = document_page.click(contains="Next")

    # Event dates page
    assert event_dates_page.status_code == 200, event_dates_page.status_code
    assert event_dates_page.has_text("Event dates")
    assert event_dates_page.has_text("Next")
    add_event_dates_form = event_dates_page.get_form("""form:not([action])""")
    added_event_dates_page = add_event_dates_form.submit().follow()
    assert added_event_dates_page.has_text("New event date")
    adding_event_dates_page = added_event_dates_page.click(contains="New event date")
    assert adding_event_dates_page.has_text("Event name")
    assert adding_event_dates_page.has_text("Intended or actual date")
    adding_event_dates_form = adding_event_dates_page.get_form("""form:not([action])""")
    adding_event_dates_form["event_date_name"] = models.EventDateOption.INTERVENTION_END_DATE.value
    adding_event_dates_form["date"] = "2022-03-07"
    adding_event_dates_form["event_date_type"] = models.EventDateType.ACTUAL.value
    adding_event_dates_form["reasons_for_change"] = "A description of the reason for this change"
    event_dates_page = adding_event_dates_form.submit(extra={"return": ""}).follow()
    assert event_dates_page.has_text(models.EventDateOption.INTERVENTION_END_DATE.name)
    deleting_event_dates_page = event_dates_page.click(contains=models.EventDateOption.INTERVENTION_END_DATE.name)
    deleting_event_dates_page = deleting_event_dates_page.get_form("""form:not([action])""")
    assert deleting_event_dates_page["event_date_name"] == models.EventDateOption.INTERVENTION_END_DATE.value
    event_dates_page = deleting_event_dates_page.submit(extra={"delete": ""}).follow()
    assert event_dates_page.has_text("Event dates")
    assert not event_dates_page.has_text(models.EventDateOption.INTERVENTION_END_DATE.name)
    assert not event_dates_page.has_text("New event date")
    evaluation_types_page = event_dates_page.click(contains="Next")

    # Evaluation types page
    assert evaluation_types_page.status_code == 200, evaluation_types_page.status_code
    assert evaluation_types_page.has_text("Evaluation types")
    assert evaluation_types_page.has_text("Save and next")
    evaluation_types_form = evaluation_types_page.get_form("""form:not([action])""")
    evaluation_types_form["evaluation_type"] = [models.EvaluationTypeOptions.ECONOMIC.value]
    impact_evaluation_design_page = evaluation_types_form.submit().follow()

    # Impact evaluation design page
    assert impact_evaluation_design_page.status_code == 200, impact_evaluation_design_page.status_code
    assert impact_evaluation_design_page.has_text("Impact evaluation design")
    assert impact_evaluation_design_page.has_text("Save and next")
    evaluation = models.Evaluation.objects.get(pk=evaluation.id)
    assert evaluation.evaluation_type == [models.EvaluationTypeOptions.ECONOMIC.value]
    impact_evaluation_design_form = impact_evaluation_design_page.get_form("""form:not([action])""")
    impact_evaluation_design_form["impact_eval_design_name"] = [models.ImpactEvalDesign.REALISE_EVALUATION.value]
    impact_evaluation_design_form["impact_eval_design_justification"] = "A justification for the design"
    impact_evaluation_design_form["impact_eval_design_description"] = "A description of the design used"
    impact_evaluation_design_form["impact_eval_design_features"] = "The main features that the design offers"
    impact_evaluation_design_form["impact_eval_design_equity"] = "The equity of the design"
    impact_evaluation_design_form["impact_eval_design_assumptions"] = "The assumptions made based on this design"
    impact_evaluation_design_form["impact_eval_design_approach_limitations"] = "The limitations of this design approach"
    impact_evaluation_analysis_page = impact_evaluation_design_form.submit().follow()

    # Impact analysis page
    assert impact_evaluation_analysis_page.status_code == 200, impact_evaluation_analysis_page.status_code
    assert impact_evaluation_analysis_page.has_text("Impact evaluation analysis")
    assert impact_evaluation_analysis_page.has_text("Save and next")
    evaluation = models.Evaluation.objects.get(pk=evaluation.id)
    assert evaluation.impact_eval_design_name == [models.ImpactEvalDesign.REALISE_EVALUATION.value]
    assert evaluation.impact_eval_design_justification == "A justification for the design"
    assert evaluation.impact_eval_design_description == "A description of the design used"
    assert evaluation.impact_eval_design_features == "The main features that the design offers"
    assert evaluation.impact_eval_design_equity == "The equity of the design"
    assert evaluation.impact_eval_design_assumptions == "The assumptions made based on this design"
    assert evaluation.impact_eval_design_approach_limitations == "The limitations of this design approach"
    impact_evaluation_analysis_form = impact_evaluation_analysis_page.get_form("""form:not([action])""")
    impact_evaluation_analysis_form["impact_eval_framework"] = models.ImpactFramework.EQUIVALENCE.value
    impact_evaluation_analysis_form["impact_eval_basis"] = models.ImpactAnalysisBasis.INTENTION_TO_TREAT.value
    impact_evaluation_analysis_form["impact_eval_analysis_set"] = "Analysis set"
    impact_evaluation_analysis_form["impact_eval_effect_measure_type"] = models.ImpactMeasureType.ABSOLUTE.value
    impact_evaluation_analysis_form["impact_eval_primary_effect_size_measure"] = "Primary effect size measure"
    impact_evaluation_analysis_form["impact_eval_effect_measure_interval"] = models.ImpactMeasureInterval.BAYESIAN.value
    impact_evaluation_analysis_form["impact_eval_primary_effect_size_desc"] = "A description of the primary effect size measure"
    impact_evaluation_analysis_form["impact_eval_interpretation_type"] = models.ImpactEvalInterpretation.EQUIVALENCE_EQUIVALENT.value
    impact_evaluation_analysis_form["impact_eval_sensitivity_analysis"] = "The sensitivity analysis"
    impact_evaluation_analysis_form["impact_eval_subgroup_analysis"] = "A subgroup analysis"
    impact_evaluation_analysis_form["impact_eval_missing_data_handling"] = "A summary of missing data handling"
    impact_evaluation_analysis_form["impact_eval_fidelity"] = "YES"
    impact_evaluation_analysis_form["impact_eval_desc_planned_analysis"] = "The planned analysis of the impact"
    process_evaluation_design_page = impact_evaluation_analysis_form.submit().follow()

    # Process evaluation design page
    assert process_evaluation_design_page.status_code == 200, process_evaluation_design_page.status_code
    assert process_evaluation_design_page.has_text("Process evaluation design")
    assert process_evaluation_design_page.has_text("Save and next")
    evaluation = models.Evaluation.objects.get(pk=evaluation.id)
    assert evaluation.impact_eval_framework == models.ImpactFramework.EQUIVALENCE.value
    assert evaluation.impact_eval_basis == models.ImpactAnalysisBasis.INTENTION_TO_TREAT.value
    assert evaluation.impact_eval_analysis_set == "Analysis set"
    assert evaluation.impact_eval_effect_measure_type == models.ImpactMeasureType.ABSOLUTE.value
    assert evaluation.impact_eval_primary_effect_size_measure == "Primary effect size measure"
    assert evaluation.impact_eval_effect_measure_interval == models.ImpactMeasureInterval.BAYESIAN.value
    assert evaluation.impact_eval_primary_effect_size_desc == "A description of the primary effect size measure"
    assert evaluation.impact_eval_interpretation_type == models.ImpactEvalInterpretation.EQUIVALENCE_EQUIVALENT.value
    assert evaluation.impact_eval_sensitivity_analysis == "The sensitivity analysis"
    assert evaluation.impact_eval_subgroup_analysis == "A subgroup analysis"
    assert evaluation.impact_eval_missing_data_handling == "A summary of missing data handling"
    assert evaluation.impact_eval_fidelity == "YES"
    assert evaluation.impact_eval_desc_planned_analysis == "The planned analysis of the impact"
    process_evaluation_design_form = process_evaluation_design_page.get_form("""form:not([action])""")
    process_evaluation_analysis_page = process_evaluation_design_form.submit().follow()

    # Process evaluation analysis page
    assert process_evaluation_analysis_page.status_code == 200, process_evaluation_analysis_page.status_code
    assert process_evaluation_analysis_page.has_text("Process evaluation analysis")
    assert process_evaluation_analysis_page.has_text("Save and next")
    process_evaluation_analysis_form = process_evaluation_analysis_page.get_form("""form:not([action])""")
    process_evaluation_analysis_form["process_eval_analysis_description"] = "A description about the process evaluation description"
    economic_design_page = process_evaluation_analysis_form.submit().follow()

    # Economic design page
    assert economic_design_page.status_code == 200, economic_design_page.status_code
    assert economic_design_page.has_text("Economic evaluation design")
    assert economic_design_page.has_text("Save and next")
    evaluation = models.Evaluation.objects.get(pk=evaluation.id)
    assert evaluation.process_eval_analysis_description == "A description about the process evaluation description"
    economic_design_form = economic_design_page.get_form("""form:not([action])""")
    economic_design_form["economic_eval_type"] = models.EconomicEvaluationType.COST_BENEFIT_ANALYSIS.value
    economic_design_form["perspective_costs"] = "The perspective costs of the evaluation"
    economic_design_form["perspective_benefits"] = "The benefits associated with the evaluation"
    economic_design_form["monetisation_approaches"] = "The approach to monetisation"
    economic_design_form["economic_eval_design_details"] = "Any details about the economic evaluation design"
    economic_analysis_page = economic_design_form.submit().follow()

    # Economic analysis page
    assert economic_analysis_page.status_code == 200, economic_analysis_page.status_code
    assert economic_analysis_page.has_text("Economic evaluation analysis")
    assert economic_analysis_page.has_text("Save and next")
    evaluation = models.Evaluation.objects.get(pk=evaluation.id)
    assert evaluation.economic_eval_type == models.EconomicEvaluationType.COST_BENEFIT_ANALYSIS.value
    assert evaluation.perspective_costs == "The perspective costs of the evaluation"
    assert evaluation.perspective_benefits == "The benefits associated with the evaluation"
    assert evaluation.monetisation_approaches == "The approach to monetisation"
    assert evaluation.economic_eval_design_details == "Any details about the economic evaluation design"
    economic_analysis_form = economic_analysis_page.get_form("""form:not([action])""")
    economic_analysis_form["economic_eval_analysis_description"] = "Description of the economic analysis"
    other_design_page = economic_analysis_form.submit().follow()

    # Other design page
    assert other_design_page.status_code == 200, other_design_page.status_code
    assert other_design_page.has_text("Economic evaluation analysis")
    assert other_design_page.has_text("Save and next")
    evaluation = models.Evaluation.objects.get(pk=evaluation.id)
    assert evaluation.economic_eval_analysis_description == "Description of the economic analysis"
    other_design_form = other_design_page.get_form("""form:not([action])""")
    other_design_form["other_eval_design_type"] = "The other evaluation design type"
    other_design_form["other_eval_design_details"] = "A description of the other design type"
    other_analysis_page = other_design_form.submit().follow()

    # Other analysis page
    assert other_analysis_page.status_code == 200, other_analysis_page.status_code
    assert other_analysis_page.has_text("Economic evaluation analysis")
    assert other_analysis_page.has_text("Save and next")
    evaluation = models.Evaluation.objects.get(pk=evaluation.id)
    assert evaluation.other_eval_design_type == "The other evaluation design type"
    assert evaluation.other_eval_design_details == "A description of the other design type"
    other_analysis_form = other_analysis_page.get_form("""form:not([action])""")
    other_analysis_form["other_eval_analysis_description"] = "A description of the other analysis"
    interventions_page = other_analysis_form.submit().follow()

    # Interventions page
    assert interventions_page.status_code == 200, interventions_page.status_code
    assert interventions_page.has_text("Interventions")
    assert interventions_page.has_text("Next")
    add_interventions_form = interventions_page.get_form("""form:not([action])""")
    added_intervention_page = add_interventions_form.submit().follow()
    assert added_intervention_page.has_text("New intervention")
    
    adding_event_dates_page = added_event_dates_page.click(contains="New event date")
    assert adding_event_dates_page.has_text("Event name")
    assert adding_event_dates_page.has_text("Intended or actual date")
    adding_event_dates_form = adding_event_dates_page.get_form("""form:not([action])""")
    adding_event_dates_form["event_date_name"] = models.EventDateOption.INTERVENTION_END_DATE.value
    adding_event_dates_form["date"] = "2022-03-07"
    adding_event_dates_form["event_date_type"] = models.EventDateType.ACTUAL.value
    adding_event_dates_form["reasons_for_change"] = "A description of the reason for this change"
    event_dates_page = adding_event_dates_form.submit(extra={"return": ""}).follow()
    assert event_dates_page.has_text(models.EventDateOption.INTERVENTION_END_DATE.name)
    deleting_event_dates_page = event_dates_page.click(contains=models.EventDateOption.INTERVENTION_END_DATE.name)
    deleting_event_dates_page = deleting_event_dates_page.get_form("""form:not([action])""")
    assert deleting_event_dates_page["event_date_name"] == models.EventDateOption.INTERVENTION_END_DATE.value
    event_dates_page = deleting_event_dates_page.submit(extra={"delete": ""}).follow()
    assert event_dates_page.has_text("Event dates")
    assert not event_dates_page.has_text(models.EventDateOption.INTERVENTION_END_DATE.name)
    assert not event_dates_page.has_text("New event date")
    evaluation_types_page = event_dates_page.click(contains="Next")

