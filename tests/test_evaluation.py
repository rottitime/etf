import testino

from . import utils

USER_DATA = {"email": "mr_evaluation_test@example.com", "password": "1-h4t3-p455w0rd-c0mpl3xity-53tt1ng5"}


def test_click_through_evaluation():
    client = utils.make_testino_client()
    utils.register(client, **USER_DATA)

    page = client.get("/")
    assert page.status_code == 200, page.status_code

    form = page.get_form("""form[action="/"]""")
    page = form.submit().follow()
    assert page.status_code == 200, page.status_code

    page = page.click(contains="Next")
    assert page.status_code == 200, page.status_code

    selector = testino.XPath('//form[.//button[contains(text(), "next")]]')

    while not page.has_text("Thank you"):
        el = page.one("button:contains('next'), a:contains('next')")
        print(page)
        if el.tag == "button":
            form_el = page.one(selector)
            form = testino.Form(page, form_el)
            page = form.submit().follow()
        else:
            page = page.click(contains="next")
        assert page.status_code == 200, page.status_code
