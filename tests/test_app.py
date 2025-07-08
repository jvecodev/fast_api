from fastapi.testclient import TestClient
from fast_api.app import app


def test_root():
    client = TestClient(app)

    # precisamos do metodo get, a partir do client para chamar a rota de app, que esta no outro arquivo
    response = client.get('/')

    # precisamos pergar a resposta, retornando um json

    assert response.json() == {'MSG': 'Hello World'}
