import testino

from etf.wsgi import application

TEST_SERVER_URL = "http://etf-testserver/"

USER_DATA = {"email": "mr_search_test@example.com", "password": "1-h4t3-p455w0rd-c0mpl3xity-53tt1ng5"}


def register(client, email, password):
    page = client.get("/accounts/signup/")
    form = page.get_form()
    form["email"] = email
    form["password1"] = password
    form["password2"] = password
    page = form.submit().follow()
    assert page.has_text(f"Successfully signed in as {email}")


def test_search():
    client = testino.WSGIAgent(application, TEST_SERVER_URL)

    register(client, **USER_DATA)

    page = client.get("/")
    assert page.status_code == 200, page.status_code
    assert page.has_text("My evaluations")

    form = page.get_form("#search-form")
    form["search_phrase"] = "Floop"
    page = form.submit()

    assert page.has_text("0 evaluations found")
