import functools

import httpx

import etf.wsgi
from etf.evaluation.models import User

TEST_SERVER_URL = "http://etf-testserver:8010/"


def with_client(func):
    @functools.wraps(func)
    def _inner(*args, **kwargs):
        with httpx.Client(app=etf.wsgi.application, base_url=TEST_SERVER_URL) as client:
            return func(client, *args, **kwargs)

    return _inner


def with_authenticated_client(func):
    @functools.wraps(func)
    def _inner(*args, **kwargs):
        user, _ = User.objects.get_or_create(email="peter.rabbit@example.com")
        user.set_password("P455W0rd")
        with httpx.Client(app=etf.wsgi.application, base_url=TEST_SERVER_URL, follow_redirects=True) as client:
            response = client.get("/accounts/login/")
            csrf = response.cookies["csrftoken"]
            data = {"login": user.email, "password": "P455W0rd"}
            headers = {"X-CSRFToken": csrf}
            client.post("/accounts/login/", data=data, headers=headers)
            return func(client, *args, **kwargs)

    return _inner
