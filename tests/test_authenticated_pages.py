import functools

import httpx

import etf.wsgi
from etf.evaluation.fakers import add_users

TEST_SERVER_URL = "http://etf-testserver:8010/"


def with_authenticated_client(func):
    @functools.wraps(func)
    def _inner(*args, **kwargs):
        user_gen = add_users(1)
        user = list(user_gen)[0]
        with httpx.Client(app=etf.wsgi.application, base_url=TEST_SERVER_URL, follow_redirects=True) as client:
            response = client.get("/accounts/login/")
            csrf = response.cookies["csrftoken"]
            data = {"login": user.email, "password": "P455W0rd"}
            headers = {"X-CSRFToken": csrf}
            client.post("/accounts/login/", data=data, headers=headers)
            return func(client, *args, **kwargs)

    return _inner


@with_authenticated_client
def test_get_search_logged_in(client):
    response = client.get("/my-evaluations/")
    assert response.status_code == 200
