"""
Create fake evaluations for testing.
"""

import datetime
import random

import faker

from . import models

fake = faker.Faker()


def make_random_date(interval_start=3 * 365, interval_end=3 * 365):
    num_days = random.randint(interval_start, interval_end)
    date = datetime.date.today() - datetime.timedelta(days=num_days)
    return date


def random_days_later(start_date, range_start, range_end):
    delta = datetime.timedelta(random.randint(range_start, range_end))
    random_date = start_date + delta
    return random_date


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


def make_evaluation(user):
    evaluation_start_date = make_random_date()
    evaluation_end_date = random_days_later(evaluation_start_date, 100, 2 * 365)
    date_of_intended_publication = random_days_later(evaluation_end_date, 50, 365)
    date_of_first_recruitment = random_days_later(evaluation_start_date, 10, 50)
    topics = generate_topics()
    data = dict(
        user=user,
        title=fake.sentence(),
        description=fake.text(),
        topics=topics,
        organisation=random.choice(models.Organisation.values),
        issue_description=fake.text(),
        those_experiencing_issue=fake.text(),
        why_improvements_matter=fake.text(),
        who_improvements_matter_to=fake.text(),
        current_practice=fake.text(),
        issue_relevance=fake.text(),
        doi=fake.pystr(20),  # TODO - fake DOI better
        evaluation_start_date=evaluation_start_date,
        evaluation_end_date=evaluation_end_date,
        date_of_intended_publication=date_of_intended_publication,
        reasons_for_delays_in_publication=fake.text(),
        rap_planned=random.choice(models.YesNoPartial.values),
        rap_planned_detail=fake.text(),
        rap_outcome=random.choice(models.YesNoPartial.values),
        rap_outcome_detail=fake.text(),
        target_population=fake.text(),
        eligibility_criteria=fake.text(),
        process_for_recruitment=fake.text(),
        target_sample_size=fake.text(),
        intended_recruitment_schedule=fake.text(),
        date_of_first_recruitment=date_of_first_recruitment,
        # TODO - add other fields
    )
    return data


def make_evaluation_type(evaluation):
    evaluation = evaluation
    type = random.choice(models.EvaluationTypeOptions.values)
    if type == "Other":
        other_description = fake.text()
    else:
        other_description = ""
    data = dict(evaluation=evaluation, type=type, other_description=other_description)
    return data


def add_evals_to_users(user):
    num_evals = random.randint(0, 3)
    for j in range(num_evals):
        eval_data = make_evaluation(user)
        evaluation = models.Evaluation(**eval_data)
        evaluation.save()
        for k in range(random.randint(0, 3)):
            eval_type_data = make_evaluation_type(evaluation)
            eval_type = models.EvaluationType(**eval_type_data)
            eval_type.save()
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
