from etf.evaluation import fields, models

from . import utils
from .utils import with_authenticated_client


@with_authenticated_client
def test_get_pages_logged_in(client):
    urls_to_test = ["/search/", "/my-evaluations/"]
    for url in urls_to_test:
        response = client.get(url)
        assert response.status_code == 200


def test_malformed_markdown():
    fields.description_help_text[
        "brief_description"
    ] = "Please provide</head> one or two sentences to describe</b> the evaluation."
    authenticated_user = {"email": "test-markdown@example.com", "password": "giraffe47"}
    client = utils.make_testino_client()
    utils.register(client, **authenticated_user)
    user = models.User.objects.get(email="test-markdown@example.com")
    evaluation = models.Evaluation(title="An Evaluation with markdown helptext")
    evaluation.save()
    evaluation.users.add(user)
    fields.description_help_text[
        "brief_description"
    ] = "Please provide one or two sentences to describe the evaluation."
    response = client.get(f"evaluation/{evaluation.id}/description/")
    assert response.has_text("Please provide one or two sentences to describe the evaluation.")
