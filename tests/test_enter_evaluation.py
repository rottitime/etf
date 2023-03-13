from nose.tools import with_setup

from etf.evaluation import choices, enums, models

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
    test_email = "test-evaluation-data-entry@example.com"
    authenticated_user = {"email": test_email, "password": "giraffe47"}
    client = utils.make_testino_client()
    utils.register(client, **authenticated_user)
    user = models.User.objects.get(email=test_email)
    evaluation = models.Evaluation(title="Test evaluation")
    evaluation.save()
    evaluation.users.add(user)
    intro_page = client.get(f"/evaluation/{evaluation.id}/")

    # Intro page
    assert intro_page.status_code == 200, intro_page.status_code
    assert intro_page.has_text("Enter your evaluation")
    assert intro_page.has_text("Next")
    title_page = intro_page.click(contains="Next")

    # Title page
    description_page = complete_verify_simple_page(
        title_page, "Title", {"title": "Test evaluation title", "short_title": "Test evaluation"}, evaluation.id
    )

    # Description page
    issue_description_page = complete_verify_simple_page(
        description_page,
        "Description",
        {
            "brief_description": "A brief description of the evaluation",
            "topics": [choices.Topic.BREXIT.value],
            "organisations": [enums.Organisation.choices[0][0]],
        },
        evaluation.id,
    )

    # Issue description page
    studied_population_page = complete_verify_simple_page(
        issue_description_page,
        "Issue description",
        {
            "issue_description": "A brief description of the evaluation issue",
            "those_experiencing_issue": "The people who are experiencing this issue",
            "why_improvements_matter": "A statement about why the improvements matter",
            "who_improvements_matter_to": "A summary of the peoples the improvements matter to",
            "current_practice": "What the current practice is in relation to the issue",
            "issue_relevance": "How relevant is the issue to society",
        },
        evaluation.id,
    )

    # Studied population page
    participant_recruitment_page = complete_verify_simple_page(
        studied_population_page,
        "Studied population",
        {
            "studied_population": "A brief description of the target population",
            "eligibility_criteria": "The criteria the population have to meet to be included",
            "sample_size": 1000,
            "sample_size_units": "A unit of measurement",
            "sample_size_details": "Any details about the same size",
        },
        evaluation.id,
    )

    # Participant recruitment page
    evaluation_cost_page = complete_verify_simple_page(
        participant_recruitment_page,
        "Participant recruitment",
        {
            "process_for_recruitment": "A summary of the process for recruitment",
            "recruitment_schedule": "A recruitment schedule",
        },
        evaluation.id,
    )

    # Evaluation costs page
    policy_costs_page = complete_verify_multiple_object_page(
        evaluation_cost_page,
        "Evaluation costs and budget",
        "New evaluation cost",
        "An example evaluation cost",
        {
            "item_name": "An example evaluation cost",
            "description": "A description of the expense item",
            "item_cost": str(1000.0),
            "earliest_spend_date": "2022-03-07",
            "latest_spend_date": "2022-03-07",
        },
    )

    # Policy costs page
    publication_intention_page = complete_verify_simple_page(
        policy_costs_page, "Policy costs and budget", {}, evaluation.id
    )

    # Publication intention page
    documents_page = complete_verify_simple_page(publication_intention_page, "Publication intention", {}, evaluation.id)

    # Documents page
    event_dates_page = complete_verify_multiple_object_page(
        documents_page,
        "Documents",
        "New document",
        "An example document",
        {
            "title": "An example document",
            "url": "https://example.com",
            "document_types": [models.DocumentType.ANALYSIS_CODE.value],
            "description": "A description of an example document",
        },
    )

    # Event dates page
    evaluation_types_page = complete_verify_multiple_object_page(
        event_dates_page,
        "Event dates",
        "New event date",
        models.EventDateOption.INTERVENTION_END_DATE.value,
        {
            "event_date_name": models.EventDateOption.INTERVENTION_END_DATE.value,
            "date": "2022-03-07",
            "event_date_type": models.EventDateType.ACTUAL.value,
            "reasons_for_change": "A description of the reason for this change",
        },
    )

    # Evaluation types page
    impact_evaluation_design_page = complete_verify_simple_page(
        evaluation_types_page,
        "Evaluation types",
        {
            "evaluation_type": [models.EvaluationTypeOptions.ECONOMIC.value],
        },
        evaluation.id,
    )

    # Impact evaluation design page
    impact_evaluation_analysis_page = complete_verify_simple_page(
        impact_evaluation_design_page,
        "Impact evaluation design",
        {
            "impact_eval_design_name": [models.ImpactEvalDesign.REALISE_EVALUATION.value],
            "impact_eval_design_justification": "A justification for the design",
            "impact_eval_design_description": "A description of the design used",
            "impact_eval_design_features": "The main features that the design offers",
            "impact_eval_design_equity": "The equity of the design",
            "impact_eval_design_assumptions": "The assumptions made based on this design",
            "impact_eval_design_approach_limitations": "The limitations of this design approach",
        },
        evaluation.id,
    )

    # Impact evaluation analysis page
    process_evaluation_design_page = complete_verify_simple_page(
        impact_evaluation_analysis_page,
        "Impact evaluation analysis",
        {
            "impact_eval_framework": models.ImpactFramework.EQUIVALENCE.value,
            "impact_eval_basis": models.ImpactAnalysisBasis.INTENTION_TO_TREAT.value,
            "impact_eval_analysis_set": "Analysis set",
            "impact_eval_effect_measure_type": models.ImpactMeasureType.ABSOLUTE.value,
            "impact_eval_primary_effect_size_measure": "Primary effect size measure",
            "impact_eval_effect_measure_interval": models.ImpactMeasureInterval.BAYESIAN.value,
            "impact_eval_primary_effect_size_desc": "A description of the primary effect size measure",
            "impact_eval_interpretation_type": models.ImpactEvalInterpretation.EQUIVALENCE_EQUIVALENT.value,
            "impact_eval_sensitivity_analysis": "The sensitivity analysis",
            "impact_eval_subgroup_analysis": "A subgroup analysis",
            "impact_eval_missing_data_handling": "A summary of missing data handling",
            "impact_eval_fidelity": "YES",
            "impact_eval_desc_planned_analysis": "The planned analysis of the impact",
        },
        evaluation.id,
    )

    # Process evaluation design page
    process_evaluation_analysis_page = complete_verify_simple_page(
        process_evaluation_design_page, "Process evaluation design", {}, evaluation.id
    )

    # Process evaluation analysis page
    economic_design_page = complete_verify_simple_page(
        process_evaluation_analysis_page,
        "Process evaluation analysis",
        {
            "process_eval_analysis_description": "A description about the process evaluation description",
        },
        evaluation.id,
    )

    # Economic design page
    economic_analysis_page = complete_verify_simple_page(
        economic_design_page,
        "Economic evaluation design",
        {
            "economic_eval_type": models.EconomicEvaluationType.COST_BENEFIT_ANALYSIS.value,
            "perspective_costs": "The perspective costs of the evaluation",
            "perspective_benefits": "The benefits associated with the evaluation",
            "monetisation_approaches": "The approach to monetisation",
            "economic_eval_design_details": "Any details about the economic evaluation design",
        },
        evaluation.id,
    )

    # Economic analysis page
    other_design_page = complete_verify_simple_page(
        economic_analysis_page,
        "Economic evaluation design",
        {"economic_eval_analysis_description": "Description of the economic analysis"},
        evaluation.id,
    )

    # Other design page
    other_analysis_page = complete_verify_simple_page(
        other_design_page,
        "Other evaluation design",
        {
            "other_eval_design_type": "The other evaluation design type",
            "other_eval_design_details": "A description of the other design type",
        },
        evaluation.id,
    )

    # Other analysis page
    interventions_page = complete_verify_simple_page(
        other_analysis_page,
        "Other evaluation analysis",
        {
            "other_eval_analysis_description": "A description of the other analysis",
        },
        evaluation.id,
    )

    # Interventions page
    outcome_measure_page = complete_verify_multiple_object_page(
        interventions_page,
        "Interventions",
        "New intervention",
        "Intervention name",
        {
            "name": "Intervention name",
            "brief_description": "A brief description of the intervention",
            "rationale": "The rationale behind the intervention",
            "materials_used": "The materials to be used in the intervention",
            "procedures": "The procedures to be used in the intervention",
            "provider_description": "A description of the provider of the intervention",
            "modes_of_delivery": "The modes of delivery used in the intervention",
            "location": "The location to be used for the intervention",
            "frequency_of_delivery": "The frequency of delivery for the intervention",
            "tailoring": "How is the intervention tailored to suit the needs",
            "fidelity": "The fidelity of the intervention",
            "resource_requirements": "The requirements for this intervention in resource costs",
            "geographical_information": "Any geographical information relevant to this intervention",
        },
    )

    # Outcome measures page
    other_measure_page = complete_verify_multiple_object_page(
        outcome_measure_page,
        "Outcome measures",
        "New outcome measure",
        "Outcome measure name",
        {
            "name": "Outcome measure name",
            "primary_or_secondary": "PRIMARY",
            "direct_or_surrogate": "DIRECT",
            "measure_type": models.MeasureType.BINARY.value,
            "description": "The description of the outcome measure",
            "collection_process": "The collection process for this outcome measure",
            "timepoint": "The process timings of interest",
            "minimum_difference": "The minimum practically important difference",
            "relevance": "The relevance of this outcome measure",
        },
    )

    # Other measures page
    ethics_page = complete_verify_multiple_object_page(
        other_measure_page,
        "Other measures",
        "New other measure",
        "Other measure name",
        {
            "name": "Other measure name",
            "measure_type": models.MeasureType.BINARY.value,
            "description": "A description of the other measure",
            "collection_process": "The process of collection and timings",
        },
    )

    # Ethics page
    impact_evaluation_findings_page = complete_verify_simple_page(
        ethics_page,
        "Ethics",
        {
            "ethics_committee_approval": "YES",
            "ethics_committee_details": "Details about the ethical committee",
            "ethical_state_given_existing_evidence_base": "Ethical state of study given existing evidence base",
            "risks_to_participants": "The risks to participants of the evaluation",
            "risks_to_study_team": "The risks to the team carrying out the evaluation",
            "participant_involvement": "The involvement of those taking part in the evaluation",
            "participant_consent": "What consent has obtained from the participants",
            "participant_information": "Information about the participants of this evaluation",
            "participant_payment": "Any payment the participants are receiving for taking part in the evaluation",
            "confidentiality_and_personal_data": "Details about the confidentiality of participant data",
            "breaking_confidentiality": "Information on what happens if confidentiality is broken",
            "other_ethical_information": "Any other notes about ethical topics relating to this evaluation",
        },
        evaluation.id,
    )

    # Impact evaluation findings page
    economic_evaluation_findings_page = complete_verify_simple_page(
        impact_evaluation_findings_page,
        "Impact evaluation findings",
        {
            "impact_eval_comparison": "An evaluation comparison",
            "impact_eval_outcome": "The outcome of the evaluation findings",
            "impact_eval_interpretation": models.ImpactEvalInterpretation.EQUIVALENCE_EQUIVALENT.value,
            "impact_eval_point_estimate_diff": "The point estimate difference of the evaluation findings",
            "impact_eval_lower_uncertainty": "The lower uncertainty of the evaluation findings",
            "impact_eval_upper_uncertainty": "The upper uncertainty of the evaluation findings",
        },
        evaluation.id,
    )

    # Economic evaluation findings page
    process_evaluation_findings_page = complete_verify_simple_page(
        economic_evaluation_findings_page,
        "Economic evaluation findings",
        {
            "economic_eval_summary_findings": "A summary of the economic findings of the evaluation",
            "economic_eval_findings": "The findings of the evaluation",
        },
        evaluation.id,
    )

    # Process evaluation findings page
    other_evaluation_findings_page = complete_verify_simple_page(
        process_evaluation_findings_page,
        "Process evaluation findings",
        {
            "process_eval_summary_findings": "The summary process findings of the evaluation",
            "process_eval_findings": "The process findings of the evaluation",
        },
        evaluation.id,
    )

    # Other evaluation findings page
    process_and_standards_page = complete_verify_simple_page(
        other_evaluation_findings_page,
        "Other evaluation findings",
        {
            "other_eval_summary_findings": "The summary other findings of the evaluation",
            "other_eval_findings": "The other findings of the evaluation",
        },
        evaluation.id,
    )

    # Processes standards page
    link_page = complete_verify_multiple_object_page(
        process_and_standards_page,
        "Processes and standards",
        "New process or standard",
        "New example process standard",
        {
            "name": "New example process standard",
            "conformity": "FULL",
            "description": "A description of the process or standard",
        },
    )

    # Links page
    metadata_page = complete_verify_multiple_object_page(
        link_page,
        "Links to other service",
        "New link",
        "New example link",
        {
            "name_of_service": "New example link",
            "link_or_identifier": "https://example.com",
        },
    )

    # Metadata page
    status_page = complete_verify_simple_page(metadata_page, "Metadata", {}, evaluation.id)

    # Status page
    end_page = complete_verify_simple_page(
        status_page,
        "Evaluation status",
        {
            "status": models.EvaluationStatus.CIVIL_SERVICE.value,
        },
        evaluation.id,
    )

    # End page
    assert end_page.status_code == 200, end_page.status_code
    assert end_page.has_text("End")
    assert not end_page.has_text("Save and next")
    assert not end_page.has_text("Next")


def complete_verify_simple_page(page, title, fields, evaluation_id):
    assert page.status_code == 200, page.status_code
    assert page.has_text(title)
    assert page.has_text("Save and next")
    form = page.get_form("""form:not([action])""")
    for field in fields:
        form[field] = fields[field]
    next_page = form.submit().follow()
    evaluation = models.Evaluation.objects.get(pk=evaluation_id)
    for field in fields:
        assert evaluation.__getattribute__(field) == fields[field]
    return next_page


def complete_verify_multiple_object_page(page, title, new_item_name, added_item_name, fields):
    assert page.status_code == 200, page.status_code
    assert page.has_text(title)
    assert page.has_text("Next")
    add_item_form = page.get_form("""form:not([action])""")
    object_added_to_records_page = add_item_form.submit().follow()
    assert object_added_to_records_page.has_text(new_item_name)
    editing_new_object_page = object_added_to_records_page.click(contains=new_item_name)
    adding_new_item_form = editing_new_object_page.get_form("""form:not([action])""")
    for field in fields:
        adding_new_item_form[field] = fields[field]
    object_added_summary_page = adding_new_item_form.submit(extra={"return": ""}).follow()
    assert object_added_summary_page.has_text(added_item_name)
    deleting_object_page = object_added_summary_page.click(contains=added_item_name)
    deleting_object_form = deleting_object_page.get_form("""form:not([action])""")
    for field in fields:
        if isinstance(fields[field], list):
            assert deleting_object_form[field].__eq__(fields[field])
        else:
            assert deleting_object_form[field] == fields[field]
    object_deleted_summary_page = deleting_object_form.submit(extra={"delete": ""}).follow()
    assert object_deleted_summary_page.has_text(title)
    assert not object_deleted_summary_page.has_text(new_item_name)
    assert not object_deleted_summary_page.has_text(added_item_name)
    return object_deleted_summary_page.click(contains="Next")
