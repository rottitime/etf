from etf.evaluation.fakers import add_users


def test_add_users():
    users = add_users(5)
    assert len(list(users)) == 5
