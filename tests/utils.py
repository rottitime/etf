import functools
import os
import pathlib

import httpx
import testino

import etf.wsgi
from etf import settings
from etf.evaluation import choices
from etf.evaluation.models import Evaluation, User

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
        user.verified = True
        user.save()
        with httpx.Client(app=etf.wsgi.application, base_url=TEST_SERVER_URL, follow_redirects=True) as client:
            response = client.get("/accounts/login/")
            csrf = response.cookies["csrftoken"]
            data = {"login": user.email, "password": "P455W0rd"}
            headers = {"X-CSRFToken": csrf}
            client.post("/accounts/login/", data=data, headers=headers)
            return func(client, *args, **kwargs)

    return _inner


def with_authenticated_external_client(func):
    @functools.wraps(func)
    def _inner(*args, **kwargs):
        user, _ = User.objects.get_or_create(email="jemima.puddleduck@example.org")
        user.set_password("P455W0rd")
        user.verified = True
        user.is_external_user = True
        user.save()
        with httpx.Client(app=etf.wsgi.application, base_url=TEST_SERVER_URL, follow_redirects=True) as client:
            response = client.get("/accounts/login/")
            csrf = response.cookies["csrftoken"]
            data = {"login": user.email, "password": "P455W0rd"}
            headers = {"X-CSRFToken": csrf}
            client.post("/accounts/login/", data=data, headers=headers)
            return func(client, *args, **kwargs)

    return _inner


def make_testino_client():
    client = testino.WSGIAgent(etf.wsgi.application, TEST_SERVER_URL)
    return client


def register(client, email, password):
    page = client.get("/accounts/signup/")
    form = page.get_form()
    form["email"] = email
    form["password1"] = password
    form["password2"] = password
    page = form.submit().follow()
    assert page.has_text(f"Successfully signed in as {email}")


def _get_latest_email_text():
    email_dir = pathlib.Path(settings.EMAIL_FILE_PATH)
    latest_email_path = max(email_dir.iterdir(), key=os.path.getmtime)
    content = latest_email_path.read_text()
    return content


def _get_latest_email_url():
    text = _get_latest_email_text()
    lines = text.splitlines()
    url_lines = tuple(word for line in lines for word in line.split() if word.startswith("http://localhost:8010/"))
    assert len(url_lines) == 1
    email_url = url_lines[0].strip()
    whole_url = email_url.strip(",")
    url = f"/{whole_url.split('http://localhost:8010/')[-1]}".replace("?", "?")
    return url


def create_fake_evaluations():
    # For testing "example.com" is counted as "Civil Service", "example.org" is not
    peter_rabbit, _ = User.objects.update_or_create(email="peter.rabbit2@example.com")
    mrs_tiggywinkle, _ = User.objects.update_or_create(email="mrs.tiggywinkle@example.org")
    draft_1 = Evaluation(title="Draft evaluation 1", status=choices.EvaluationStatus.DRAFT)
    draft_1.save()
    draft_2 = Evaluation(title="Draft evaluation 2", status=choices.EvaluationStatus.DRAFT)
    draft_2.save()
    draft_2.users.add(peter_rabbit)
    draft_2.users.add(mrs_tiggywinkle)
    draft_2.save()
    cs_1 = Evaluation(title="Civil Service evaluation 1", status=choices.EvaluationStatus.CIVIL_SERVICE)
    cs_1.save()
    cs_2 = Evaluation(title="Civil Service evaluation 2", status=choices.EvaluationStatus.CIVIL_SERVICE)
    cs_2.save()
    cs_2.users.add(peter_rabbit)
    cs_2.users.add(mrs_tiggywinkle)
    cs_2.save()
    public_1 = Evaluation(title="Public evaluation 1", status=choices.EvaluationStatus.PUBLIC)
    public_1.save()
    public_2 = Evaluation(title="Public evaluation 2", status=choices.EvaluationStatus.PUBLIC)
    public_2.save()
    public_2.users.add(peter_rabbit)
    public_2.save()


def remove_fake_evaluations():
    fake_evaluation_titles = [
        "Draft evaluation 1",
        "Draft evaluation 2",
        "Civil Service evaluation 1",
        "Civil Service evaluation 2",
        "Public evaluation 1",
        "Public evaluation 2",
    ]
    Evaluation.objects.filter(title__in=fake_evaluation_titles).delete()
    User.objects.filter(email__in=["mrs.tiggywinkle@example.com", "peter.rabbit2@example."]).delete()
