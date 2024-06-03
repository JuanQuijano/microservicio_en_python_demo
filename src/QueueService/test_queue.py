import json
import pytest
from QueueService.queue import app

@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

def test_enqueue(client):
    data = {
        'operacion': 'add',
        'numero1': 5,
        'numero2': 10
    }
    response = client.post('/api/queue', json=data)
    assert response.status_code == 200
    assert response.json == {'status': 'Message enqueued'}

def test_dequeue(client):
    response = client.get('/api/queue')
    assert response.status_code == 200
    assert response.json == {'status': 'Message dequeued'}