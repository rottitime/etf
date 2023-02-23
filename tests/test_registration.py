from . import utils

USER_DATA = {"email": "mr_registration_test@example.com", "password": "1-h4t3-p455w0rd-c0mpl3xity-53tt1ng5"}


def test_emails():
    client = utils.make_testino_client()

    page = client.get("/accounts/signup/")
    form = page.get_form()
    form["email"] = USER_DATA['email']
    form["password1"] = USER_DATA['password']
    form["password2"] = USER_DATA['password']
    page = form.submit()

    assert page.has_text("This email domain is not yet supported")
