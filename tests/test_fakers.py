from etf.evaluation.fakers import (
    add_evals_to_users,
    add_users,
    make_evaluation,
)


def test_add_users():
    users = add_users(5)
    assert len(list(users)) == 5


def test_add_evaluations():
    user_gen = add_users(1)
    user = list(user_gen)[0]
    evaluation = make_evaluation(user)
    assert evaluation["user"] == user


def test_add_evaluations_to_user():
    user_gen = add_users(1)
    user = list(user_gen)[0]
    add_evals_to_users(user, allow_empty=False)
    assert 1 <= len(user.evaluations.all()) <= 3
