from .utils import with_authenticated_client, with_client


@with_client
def test_get_data_download_not_authenticated(client):
    response = client.get("/data-download/")
    assert response.status_code == 302, response.status_code


@with_authenticated_client
def test_get_data_download(client):
    response = client.get("/data-download/")
    assert response.status_code == 200, response.status_code
