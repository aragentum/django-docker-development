import pytest


@pytest.mark.django_db
def test_sample_api(client):
    response = client.get('/api/sample_api/')
    assert response.status_code == 200
    assert response.json() == dict(sample_data=123)
