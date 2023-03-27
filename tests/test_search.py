from etf.evaluation import interface, models
from . import utils

USER_DATA = {"email": "mr_search_test@example.com", "password": "1-h4t3-p455w0rd-c0mpl3xity-53tt1ng5"}


def test_search():
    client = utils.make_testino_client()
    utils.register(client, **USER_DATA)

    page = client.get("/")
    assert page.status_code == 200, page.status_code
    assert page.has_text("My evaluations")

    user = models.User.objects.get(email=USER_DATA["email"])

    print(user.id)

    evaluation = interface.facade.evaluation.create(user_id=user.id)
    interface.facade.evaluation.update(user_id=user.id, evaluation_id=evaluation["id"], data={"title": "test"})

    search_page = client.get("/search/")

    search_form = search_page.get_form()

    search_form["search_text"] = evaluation["title"]

    results = search_form.submit().follow()

    assert results.has_text(evaluation["title"])
