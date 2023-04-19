from etf.evaluation import fields, models

from . import utils


@utils.with_authenticated_client
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


@utils.with_authenticated_client
def test_evaluation_permissions(client):
    # Setup evaluation
    test_email = "test-evaluation-permissions@example.com"
    user, _ = models.User.objects.get_or_create(email=test_email)
    evaluation = models.Evaluation.objects.create(title="Test evaluation")
    evaluation.save()
    user.evaluations.add(evaluation)
    user.save()

    urls = (
        f"/evaluation/{evaluation.id}/",
        f"evaluation/{evaluation.id}/title/",
        f"evaluation/{evaluation.id}/description/",
        f"evaluation/{evaluation.id}/issue-description/",
        f"evaluation/{evaluation.id}/studied-population/",
        f"evaluation/{evaluation.id}/participant-recruitment/",
        f"evaluation/{evaluation.id}/policy-costs/",
        f"evaluation/{evaluation.id}/publication-intention/",
        f"evaluation/{evaluation.id}/evaluation-types/",
        f"evaluation/{evaluation.id}/impact-design/",
        f"evaluation/{evaluation.id}/impact-analysis/",
        f"evaluation/{evaluation.id}/process-design/",
        f"evaluation/{evaluation.id}/process-analysis/",
        f"evaluation/{evaluation.id}/economic-design/",
        f"evaluation/{evaluation.id}/economic-analysis/",
        f"evaluation/{evaluation.id}/other-design/",
        f"evaluation/{evaluation.id}/other-analysis/",
        f"evaluation/{evaluation.id}/ethics/",
        f"evaluation/{evaluation.id}/impact-findings/",
        f"evaluation/{evaluation.id}/economic-findings/",
        f"evaluation/{evaluation.id}/process-findings/",
        f"evaluation/{evaluation.id}/other-findings/",
        f"evaluation/{evaluation.id}/metadata/",
        f"evaluation/{evaluation.id}/status/",
        f"evaluation/{evaluation.id}/end/",
    )

    for url in urls:
        response = client.get(url)
        assert response.status_code == 404
