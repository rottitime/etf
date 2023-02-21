import testino

from . import utils

USER_DATA = {"email": "mr_evaluation_test@example.com", "password": "1-h4t3-p455w0rd-c0mpl3xity-53tt1ng5"}


def test_intervention():
    client = utils.make_testino_client()
    utils.register(client, **USER_DATA)

    page = client.get("/")
    assert page.status_code == 200, page.status_code

    form = page.get_form("""form[action="/"]""")
    page = form.submit().follow()
    assert page.status_code == 200, page.status_code

    page = page.click(contains="Next")
    assert page.status_code == 200, page.status_code

    selector = testino.XPath('//form[.//button[contains(text(), "Next")]]')

    while not page.has_text("The end"):
        el = page.one("button:contains('Next'), a:contains('Next')")
        if el.tag == "button":
            form_el = page.one(selector)
            form = testino.Form(page, form_el)
            page = form.submit().follow()
        else:
            page = page.click(contains="Next")
        assert page.status_code == 200, page.status_code
