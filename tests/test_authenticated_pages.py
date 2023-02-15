from .utils import with_authenticated_client


@with_authenticated_client
def test_get_pages_logged_in(client):
    urls_to_test = ["/search/", "/my-evaluations/"]
    for url in urls_to_test:
        response = client.get(url)
        assert response.status_code == 200
