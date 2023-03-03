from etf.evaluation import models

from . import utils

VALID_USER_EMAIL = "test@example.com"
VALID_USER_PASSWORD1 = "elephant99"
VALID_USER_PASSWORD2 = "giraffe47"


def enter_form_data(email, password1, password2, follow=False):
    client = utils.make_testino_client()

    page = client.get("/accounts/signup/")
    form = page.get_form()
    form["email"] = email
    form["password1"] = password1
    form["password2"] = password2

    if follow:
        page = form.submit().follow()
    else:
        page = form.submit()
    return page


def test_invalid_password_too_short():
    page = enter_form_data(VALID_USER_EMAIL, "abc123!", "abc123!")

    assert page.has_text("This password is too short. It must contain at least 8 characters.")
    assert page.has_text("This password is too common.")


def test_invalid_password_all_numeric():
    page = enter_form_data(VALID_USER_EMAIL, "1234567890", "1234567890")

    assert page.has_text("This password is entirely numeric.")


def test_invalid_password_too_common():
    page = enter_form_data(VALID_USER_EMAIL, "asdfghjkl", "asdfghjkl")

    assert page.has_text("This password is too common.")


def test_invalid_password_does_not_match():
    page = enter_form_data(VALID_USER_EMAIL, VALID_USER_PASSWORD1, VALID_USER_PASSWORD2)

    assert page.has_text("You must type the same password each time.")


def test_email_is_valid():
    page = enter_form_data(VALID_USER_EMAIL, VALID_USER_PASSWORD1, VALID_USER_PASSWORD1, True)

    assert page.has_text(f"Successfully signed in as {VALID_USER_EMAIL}.")


def test_email_is_invalid_domain_extension():
    page = enter_form_data("jane.doe@example.org", VALID_USER_PASSWORD1, VALID_USER_PASSWORD1)

    assert page.has_text(
        "This email domain is not yet supported. Please contact the site admin team if you think this is incorrect."
    )


def test_email_is_invalid_no_extension():
    page = enter_form_data("jane.doe@example", VALID_USER_PASSWORD1, VALID_USER_PASSWORD1)

    assert page.has_text("Enter a valid email address.")


def test_email_is_invalid_only_domain():
    page = enter_form_data("@example.org", VALID_USER_PASSWORD1, VALID_USER_PASSWORD1)

    assert page.has_text("Enter a valid email address.")


def test_email_is_invalid_no_domain():
    page = enter_form_data("john.doe@", VALID_USER_PASSWORD1, VALID_USER_PASSWORD1)

    assert page.has_text("Enter a valid email address.")


def test_user_already_registered():
    user, _ = models.User.objects.get_or_create(email=VALID_USER_EMAIL)
    user.save()

    page = enter_form_data(VALID_USER_EMAIL, VALID_USER_PASSWORD1, VALID_USER_PASSWORD1)

    assert page.has_text("Registration was unsuccessful, please try again.")
