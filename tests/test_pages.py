import functools

import httpx

import etf.wsgi
from etf.evaluation.fakers import add_users

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
        user_gen = add_users(1)
        print('Added user')
        user = list(user_gen)[0]
        print('Got user')
        with httpx.Client(app=etf.wsgi.application, base_url=TEST_SERVER_URL, follow_redirects=True) as client:
            r = client.get("/accounts/login/")
            print(r.cookies)
            print(r.headers)
            csrf = r.cookies["csrftoken"]
            print(csrf)
            data = {'login': user.email, 'password': 'P455W0rd'}
            headers = {'X-CSRFToken': csrf}
            client.post("/accounts/login/", data=data, headers=headers)  # Fails here
            print('logged_in')
            return func(client, *args, **kwargs)

    return _inner


@with_client
def test_add_evaluation(client):
    response = client.get("/")
    assert response.status_code == 302


@with_client
def test_get_my_evaluations(client):
    response = client.get("/my-evaluations/")
    assert response.status_code == 302


@with_client
def test_get_login(client):
    response = client.get("/accounts/login/")
    assert response.status_code == 200


@with_authenticated_client
def test_get_search_logged_in(client):
    response = client.get("/my-evaluations/")
    print(response.status_code)
    assert response.status_code == 200


