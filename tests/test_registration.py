from nose import with_setup

from etf import settings as etf_settings
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


@with_setup(lambda: setattr(etf_settings, 'SEND_VERIFICATION_EMAIL', True),
            lambda: setattr(etf_settings, 'SEND_VERIFICATION_EMAIL', False))
def test_verify_email():
    client = utils.make_testino_client()

    page = client.get("/accounts/signup/")
    assert page.has_text("Register")
    form = page.get_form()
    form["email"] = "test-verification@example.com"
    form["password1"] = VALID_USER_PASSWORD1
    form["password2"] = VALID_USER_PASSWORD1

    signed_up_page = form.submit()
    assert signed_up_page.has_text("Sign up complete")
    assert signed_up_page.has_text("A verification email has been sent to your email address.")

    verify_url = utils._get_latest_email_url()

    verify_page = client.get(verify_url)

    assert verify_page.has_text("Your account has been successfully verified.")

    login_page = client.get("/accounts/login/")

    form = login_page.get_form()
    form["login"] = "test-verification@example.com"
    form["password"] = VALID_USER_PASSWORD1

    home_page = form.submit().follow()

    assert home_page.has_text("Create evaluation")
