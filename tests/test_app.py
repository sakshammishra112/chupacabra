import pytest

from app import create_app


@pytest.fixture
def client():
    app = create_app()
    app.testing = True
    return app.test_client()


def test_index(client):
    response = client.get("/")
    assert response.status_code == 200
    assert response.get_json() == {"message": "Hello, DevOps!"}


def test_health(client):
    response = client.get("/health")
    assert response.status_code == 200
    assert response.get_json() == {"status": "ok"}


def test_greet(client):
    response = client.get("/greet/DevOps")
    assert response.status_code == 200
    assert response.get_json() == {"message": "Hello, DevOps!"}


def test_add(client):
    response = client.get("/add?a=2&b=3")
    assert response.status_code == 200
    assert response.get_json() == {"result": 5}


def test_add_rejects_non_numeric_input(client):
    response = client.get("/add?a=foo&b=3")
    assert response.status_code == 400
    assert "error" in response.get_json()


def test_add_requires_both_params(client):
    response = client.get("/add?a=2")
    assert response.status_code == 400
