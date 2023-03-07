from .utils import with_client, with_authenticated_client


@with_client
def test_get_data_download_not_authenticated(client):
    urls_to_test = ["/data-download/", "/data-download/json/", "/data-download/csv/"]
    for url in urls_to_test:
        response = client.get(url)
        assert response.status_code == 302, response.status_code


@with_authenticated_client
def test_get_data_download(client):
    urls_to_test = ["/data-download/", "/data-download/json/", "/data-download/csv/"]
    for url in urls_to_test:
        response = client.get(url)
        assert response.status_code == 200, response.status_code
