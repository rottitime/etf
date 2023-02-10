import environ
from allauth.account.adapter import DefaultAccountAdapter
from django.forms import ValidationError

env = environ.Env()


class RestrictEmailAdapter(DefaultAccountAdapter):
    def clean_email(self, email):
        allowed_domains = ["cabinetoffice.gov.uk"]
        domain = email.split("@")[-1]
        allow_example_domain = env.bool("ALLOW_EXAMPLE_EMAILS", default=False)
        if allow_example_domain:
            allowed_domains.append("example.com")
        if domain not in allowed_domains:
            raise ValidationError(
                "This email domain is not yet supported. Please contact the site admin team if you think this is incorrect."
            )
        return email
