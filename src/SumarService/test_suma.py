import pytest
from SumarService.suma import app

@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

def test_sumar_handler(client):
    response = client.post('/sumar', json={'cantidad1': 5, 'cantidad2': 7})
    assert response.get_json() == {"resultado": 12}

def test_sumar_handler_with_invalid_data(client):
    response = client.post('/sumar', json={'cantidad1': "invalid", 'cantidad2': 7})
    assert 'error' in response.get_json()

    response = client.post('/sumar', json={'cantidad1': 5, 'cantidad2': "invalid"})
    assert 'error' in response.get_json()

    response = client.post('/sumar', json={'cantidad1': "invalid", 'cantidad2': "invalid"})
    assert 'error' in response.get_json()