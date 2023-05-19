from django.conf import settings
from django.forms import ValidationError



def clean_email(email):
    email = email.lower()
    domain = email.split("@")[-1]
    email_allowed = domain in settings.ALLOWED_CIVIL_SERVICE_DOMAINS
    if not email_allowed:
        raise ValidationError (f"This email domain is not yet supported. Please contact the site admin team if you think this is incorrect <a href='mailto:{settings.FEEDBACK_EMAIL}'>{settings.FEEDBACK_EMAIL}</a>")
    return email
