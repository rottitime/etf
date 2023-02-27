"""
Create fake evaluations for testing.
"""

import datetime
import random

import faker

from . import enums, models
from .pages import get_default_page_statuses

fake = faker.Faker()


def make_random_date(range_start=-3 * 365, range_end=3 * 365):
    num_days = random.randint(range_start, range_end)
    date = datetime.date.today() + datetime.timedelta(days=num_days)
    return date


def random_days_later(start_date, range_start, range_end):
    delta = datetime.timedelta(random.randint(range_start, range_end))
    random_date = start_date + delta
    return random_date


def make_random_yes_no():
    yes_or_no = random.randint(0, 1)
    if yes_or_no == 0:
        return "NO"
    else:
        return "YES"


def make_fake_user():
    first_name = fake.first_name()
    last_name = fake.last_name()
    data = dict(
        first_name=first_name,
        last_name=first_name,
        email=f"{first_name}.{last_name}@example.com".lower(),
        is_active=True,
    )
    return data


def generate_topics():
    num_topics = random.randint(0, 4)
    set_topics = set()
    for i in range(num_topics):
        set_topics.add(random.choice(models.Topic.values))
    return list(set_topics)


def generate_organisations():
    num_organisations = random.randint(0, 4)
    set_organisations = set()
    for i in range(num_organisations):
        set_organisations.add(random.choice(enums.Organisation.values))
    return list(set_organisations)


def generate_evaluation_types():
    num_types = random.randint(0, 2)
    set_types = set()
    for i in range(num_types):
        set_types.add(random.choice(models.EvaluationTypeOptions.values))
    return list(set_types)


def make_evaluation():
    topics = generate_topics()
    organisations = generate_organisations()
    evaluation_type = generate_evaluation_types()
    data = dict(
        title=fake.text(256),
        short_title=fake.text(64),
        brief_description=fake.text(),
        topics=topics,
        organisations=organisations,
        status=random.choice(models.EvaluationStatus.values),
        doi=fake.text(64),
        page_statuses=get_default_page_statuses(),
        issue_description=fake.text(),
        those_experiencing_issue=fake.text(),
        why_improvements_matter=fake.text(),
        who_improvements_matter_to=fake.text(),
        current_practice=fake.text(),
        issue_relevance=fake.text(),
        evaluation_type=evaluation_type,
        studied_population=fake.text(),
        eligibility_criteria=fake.text(),
        sample_size=fake.pyint(),
        sample_size_units=fake.text(5),
        sample_size_details=fake.text(),
        process_for_recruitment=fake.sentence(),
        recruitment_schedule=fake.sentence(),
        ethics_committee_approval=make_random_yes_no(),
        ethics_committee_details=fake.text(),
        ethical_state_given_existing_evidence_base=fake.text(),
        risks_to_participants=fake.text(),
        risks_to_study_team=fake.text(),
        participant_involvement=fake.text(),
        participant_information=fake.text(),
        participant_consent=fake.text(),
        participant_payment=fake.text(),
        confidentiality_and_personal_data=fake.text(),
        breaking_confidentiality=fake.text(),
        other_ethical_information=fake.text(),
        impact_eval_design_name=fake.words(),
        impact_eval_design_justification=fake.text(),
        impact_eval_design_description=fake.text(),
        impact_eval_design_features=fake.text(),
        impact_eval_design_equity=fake.text(),
        impact_eval_design_assumptions=fake.text(),
        impact_eval_design_approach_limitations=fake.text(),
        impact_eval_analysis_set=fake.text(),
        impact_eval_primary_effect_size_measure=fake.text(),
        impact_eval_primary_effect_size_desc=fake.text(),
        impact_eval_sensitivity_analysis=fake.text(),
        impact_eval_subgroup_analysis=fake.text(),
        impact_eval_missing_data_handling=fake.text(),
        impact_eval_desc_planned_analysis=fake.text(),
        process_eval_methods=fake.text(256),
        process_eval_analysis_description=fake.text(),
        economic_eval_type=fake.text(256),
        perspective_costs=fake.text(),
        perspective_benefits=fake.text(),
        monetisation_approaches=fake.text(),
        economic_eval_design_details=fake.text(),
        economic_eval_analysis_description=fake.text(),
        other_eval_design_type=fake.text(),
        other_eval_design_details=fake.text(),
        other_eval_analysis_description=fake.text(),
        impact_eval_comparison=fake.text(),
        impact_eval_outcome=fake.text(),
        impact_eval_point_estimate_diff=fake.text(),
        impact_eval_lower_uncertainty=fake.text(),
        impact_eval_upper_uncertainty=fake.text(),
        economic_eval_summary_findings=fake.text(),
        economic_eval_findings=fake.text(),
        process_eval_summary_findings=fake.text(),
        process_eval_findings=fake.text(),
        other_eval_summary_findings=fake.text(),
        other_eval_findings=fake.text(),
        # TODO - add other fields
    )
    return data


def add_evals_to_users(user, allow_empty=True):
    num_evals = random.randint(0 if allow_empty is True else 1, 3)
    for j in range(num_evals):
        eval_data = make_evaluation()
        evaluation = models.Evaluation.objects.create(**eval_data)
        evaluation.users.set([user])
        evaluation.save()
        # TODO - add other models to evaluation


def add_users(number):
    for i in range(number):
        user_data = make_fake_user()
        while models.User.objects.filter(email=user_data["email"]).exists():
            user_data = make_fake_user()
        user = models.User(**user_data)
        user.set_password("P455W0rd")
        user.save()
        add_evals_to_users(user)
        yield user
