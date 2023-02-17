import sentry_sdk
from sentry_sdk.integrations.django import DjangoIntegration

from .settings_base import (
    BASE_DIR,
    SECRET_KEY,
    STATIC_ROOT,
    STATIC_URL,
    STATICFILES_DIRS,
    env,
)

SECRET_KEY = SECRET_KEY
STATIC_URL = STATIC_URL
STATICFILES_DIRS = STATICFILES_DIRS
STATIC_ROOT = STATIC_ROOT

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = env.bool("DEBUG", default=False)

BASE_URL = env.str("BASE_URL")

ALLOWED_HOSTS = [
    "etf-develop.london.cloudapps.digital",
    "etf-sandbox.london.cloudapps.digital",
    "etf-staging.london.cloudapps.digital",
    "localhost",
    "127.0.0.1",
    "etf-testserver",
]


# Application definition

INSTALLED_APPS = [
    "etf.evaluation",
    "allauth",
    "allauth.account",
    "allauth.socialaccount",
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.sites",
    "django.contrib.staticfiles",
    "django.contrib.postgres",
]

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "whitenoise.middleware.WhiteNoiseMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

ROOT_URLCONF = "etf.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.jinja2.Jinja2",
        "DIRS": [
            BASE_DIR / "etf" / "templates",
        ],
        "OPTIONS": {
            "environment": "etf.jinja2.environment",
        },
    },
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [
            BASE_DIR / "etf" / "templates" / "allauth",
        ],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
]

WSGI_APPLICATION = "etf.wsgi.application"

DATABASES = {
    "default": {
        **env.db("DATABASE_URL"),
        **{"ATOMIC_REQUESTS": True},
    }
}

AUTHENTICATION_BACKENDS = [
    "django.contrib.auth.backends.ModelBackend",
    "allauth.account.auth_backends.AuthenticationBackend",
]

AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.MinimumLengthValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.CommonPasswordValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.NumericPasswordValidator",
    },
]

LANGUAGE_CODE = "en-us"
TIME_ZONE = "UTC"
USE_I18N = True
USE_L10N = True
USE_TZ = True

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"

SENTRY_DSN = env.str("SENTRY_DSN", default="")
SENTRY_ENVIRONMENT = env.str("SENTRY_ENVIRONMENT", default="")

sentry_sdk.init(
    dsn=SENTRY_DSN,
    integrations=[
        DjangoIntegration(),
    ],
    environment=SENTRY_ENVIRONMENT,
    send_default_pii=True,
    traces_sample_rate=0.0,
)

AUTH_USER_MODEL = "evaluation.User"

ACCOUNT_AUTHENTICATION_METHOD = "email"
ACCOUNT_EMAIL_REQUIRED = True
ACCOUNT_USER_MODEL_USERNAME_FIELD = None
ACCOUNT_USERNAME_REQUIRED = False
SITE_ID = 1
ACCOUNT_EMAIL_VERIFICATION = "none"
LOGIN_REDIRECT_URL = "index"

ALLOW_EXAMPLE_EMAILS = env.bool("ALLOW_EXAMPLE_EMAILS", default=True)

DEFAULT_ALLOWED_DOMAINS = frozenset(
    [
        "cabinet-office.x.gsi.gov.uk",
        "cabinetoffice.gov.uk",
        "crowncommercial.gov.uk",
        "csep.gov.uk",
        "cslearning.gov.uk",
        "csc.gov.uk",
        "digital.cabinet-office.gov.uk",
        "geo.gov.uk",
        "gpa.gov.uk",
        "ipa.gov.uk",
        "no10.gov.uk",
        "odandd.gov.uk",
        "xansium.com",
    ]
)

if ALLOW_EXAMPLE_EMAILS:
    ALLOWED_DOMAINS = DEFAULT_ALLOWED_DOMAINS.union({"example.com"})
else:
    ALLOWED_DOMAINS = DEFAULT_ALLOWED_DOMAINS

ACCOUNT_ADAPTER = "etf.evaluation.restrict_email_adapter.RestrictEmailAdapter"

PASSWORD_RESET_TIMEOUT = 60 * 60 * 24

# Email

EMAIL_BACKEND_TYPE = env.str("EMAIL_BACKEND_TYPE")

if EMAIL_BACKEND_TYPE == "FILE":
    EMAIL_BACKEND = "django.core.mail.backends.filebased.EmailBackend"
    EMAIL_FILE_PATH = env.str("EMAIL_FILE_PATH")
elif EMAIL_BACKEND_TYPE == "CONSOLE":
    EMAIL_BACKEND = "django.core.mail.backends.console.EmailBackend"
elif EMAIL_BACKEND_TYPE == "GOVUKNOTIFY":
    EMAIL_BACKEND = "django_gov_notify.backends.NotifyEmailBackend"
    GOVUK_NOTIFY_API_KEY = env.str("GOVUK_NOTIFY_API_KEY")
    GOVUK_NOTIFY_PLAIN_EMAIL_TEMPLATE_ID = env.str("GOVUK_NOTIFY_PLAIN_EMAIL_TEMPLATE_ID")
else:
    if EMAIL_BACKEND_TYPE not in ("FILE", "CONSOLE", "GOVUKNOTIFY"):
        raise Exception(f"Unknown EMAIL_BACKEND_TYPE of {EMAIL_BACKEND_TYPE}")

SEND_VERIFICATION_EMAIL = env.bool("SEND_VERIFICATION_EMAIL", default=False)

if DEBUG:
    ACCOUNT_RATE_LIMITS = {}
