"""
Create fake evaluations for testing.
"""

import datetime
import random

import faker

from . import models

fake = faker.Faker()


def make_random_date(range_start=-3 * 365, range_end=3 * 365):
    num_days = random.randint(range_start, range_end)
    date = datetime.date.today() + datetime.timedelta(days=num_days)
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


def generate_organisations():
    num_organisations = random.randint(0, 4)
    set_organisations = set()
    for i in range(num_organisations):
        set_organisations.add(random.choice(models.Organisation.values))
    return list(set_organisations)


def make_evaluation():
    topics = generate_topics()
    organisations = generate_organisations()
    data = dict(
        title=fake.sentence(),
        brief_description=fake.text(),
        topics=topics,
        status=random.choice(models.EvaluationStatus.values),
        organisations=organisations,
        issue_description=fake.text(),
        those_experiencing_issue=fake.text(),
        why_improvements_matter=fake.text(),
        who_improvements_matter_to=fake.text(),
        current_practice=fake.text(),
        issue_relevance=fake.text(),
        eligibility_criteria=fake.text(),
        process_for_recruitment=fake.text(),
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


def add_evals_to_users(user, allow_empty=True):
    num_evals = random.randint(0 if allow_empty is True else 1, 3)
    for j in range(num_evals):
        eval_data = make_evaluation()
        evaluation = models.Evaluation.objects.create(**eval_data)
        evaluation.users.set([user])
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
