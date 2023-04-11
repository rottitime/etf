from django.conf import settings
from django.forms import ValidationError


def clean_email(email):
    email = email.lower()
    email_allowed = False
    if not email_allowed:
        domain = email.split("@")[-1]
        email_allowed = domain in settings.ALLOWED_DOMAINS
    if not email_allowed:
        raise ValidationError(
            "This email domain is not yet supported. Please contact the site admin team if you think this is incorrect."
        )
    return email
