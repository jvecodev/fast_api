from fastapi.testclient import TestClient
from fast_api.app import app


def test_root():
    """
    Esse teste tem 3 etapas: (AAA)
    
    1. Arrange: configurar o ambiente de teste, criando um cliente de teste
    2. Act: chamar a rota raiz da aplicação e executa a ação
    3. Assert: verificar se a resposta é a esperada e garante que a aplicação está funcionando corretamente
    4. Alguns ensinadores incluem o teardown, mas nesse caso não é necessário, que no caso é a limpeza do ambiente de teste, queda do ambiente, etc.
    """
    # Arrange
    client = TestClient(app)

    # Act
    response = client.get('/')

    # Assert
    assert response.status_code == 200 # Ou HTTPStatus.OK no lugar do 200
    assert response.json() == {'MSG': 'Hello World'}
