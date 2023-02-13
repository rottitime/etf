from allauth.account.adapter import DefaultAccountAdapter
from django.conf import settings
from django.forms import ValidationError


class RestrictEmailAdapter(DefaultAccountAdapter):
    def clean_email(self, email):
        domain = email.split("@")[-1]
        allowed_domains = settings.ALLOWED_DOMAINS
        if domain not in allowed_domains:
            raise ValidationError(
                "This email domain is not yet supported. Please contact the site admin team if you think this is incorrect."
            )
        return email
