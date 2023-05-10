from . import utils

USER_DATA = {"email": "mr_interventions_test@example.com", "password": "1-h4t3-p455w0rd-c0mpl3xity-53tt1ng5"}


def test_intervention():
    client = utils.make_testino_client()
    utils.register(client, **USER_DATA)

    page = client.get("/")
    assert page.status_code == 200, page.status_code

    page = page.click(contains="Create evaluation", index=0)
    assert page.status_code == 200, page.status_code

    form = page.get_form()
    form["title"] = "Test evaluation"
    page = form.submit().follow()
    assert page.status_code == 200, page.status_code
    assert page.url.endswith("/")

    intervention_url = "/".join(page.url.split("/")[:-1] + ["interventions/"])
    page = client.get(intervention_url)

    form = page.get_form(""".intervention-add-form""")
    page = form.submit().follow()

    assert page.status_code == 200, page.status_code
    assert page.url.endswith("/interventions/")
