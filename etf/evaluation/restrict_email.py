from django.conf import settings
from django.forms import ValidationError

from etf.allowed_domains import CIVIL_SERVICE_DOMAINS


def is_civil_service_email(email):
    allowed = False
    email = email.lower()
    email_split = email.split("@")
    if email_split[-1] in CIVIL_SERVICE_DOMAINS:
        allowed = True
    return allowed


def clean_email(email):
    email = email.lower()
    domain = email.split("@")[-1]
    email_allowed = domain in settings.ALLOWED_DOMAINS
    if not email_allowed:
        raise ValidationError(
            "This email domain is not yet supported. Please contact the site admin team if you think this is incorrect."
        )
    return email
