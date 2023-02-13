import datetime

import furl as furl
import pytz
from django.conf import settings
from django.contrib.auth.tokens import PasswordResetTokenGenerator
from django.core.mail import send_mail
from django.template.loader import render_to_string


def _strip_microseconds(dt):
    if not dt:
        return ""
    return dt.replace(microsecond=0, tzinfo=None)


class PasswordResetTokenGenerator(PasswordResetTokenGenerator):
    def _make_hash_value(self, user, timestamp):
        login_timestamp = _strip_microseconds(user.last_login)
        email = user.email or ""
        token_timestamp = _strip_microseconds(user.last_token_sent_at)
        return f"{user.pk}{user.password}{login_timestamp}{timestamp}{email}{token_timestamp}"


PASSWORD_RESET_TOKEN_GENERATOR = PasswordResetTokenGenerator()


EMAIL_MAPPING = {
    "password-reset": {
        "from_address": "support-etf@cabinetoffice.gov.uk",
        "subject": "Evaluation Registry: password reset",
        "template_name": "email/password-reset.txt",
        "url_path": "/accounts/signin/forgotten-password/reset",
        "token_generator": PASSWORD_RESET_TOKEN_GENERATOR,
    },
}


def _send_token_email(user, subject, template_name, from_address, url_path, token_generator):
    user.last_token_sent_at = datetime.datetime.now(tz=pytz.UTC)
    user.save()
    token = token_generator.make_token(user)
    api_host_url = settings.HOST_URL.strip("/")
    web_host_url = settings.HOST_MAP[api_host_url]
    url = str(furl.furl(url=web_host_url, path=url_path, query_params={"code": token, "user_id": str(user.id)}))
    context = dict(user=user, url=url)
    body = render_to_string(template_name, context)
    response = send_mail(
        subject=subject,
        message=body,
        from_email=from_address,
        recipient_list=[user.email],
    )
    return response


def _send_normal_email(subject, template_name, from_address, to_address, context):
    body = render_to_string(template_name, context)
    response = send_mail(
        subject=subject,
        message=body,
        from_email=from_address,
        recipient_list=[to_address],
    )
    return response


def send_password_reset_email(user):
    data = EMAIL_MAPPING["password-reset"]
    return _send_token_email(user, **data)
