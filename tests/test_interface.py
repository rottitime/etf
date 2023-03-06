from etf.evaluation import interface, models

USER_DATA = {"email": "mr_interface_test@example.com", "password": "1-h4t3-p455w0rd-c0mpl3xity-53tt1ng5"}


def test_evaluation_created():
    user, _ = models.User.objects.get_or_create(email=USER_DATA["email"])
    result = interface.facade.evaluation.create(user_id=user.id)
    expected = [{"email": "mr_interface_test@example.com"}]
    assert result["users"] == expected
