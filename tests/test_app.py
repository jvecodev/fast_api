from http import HTTPStatus
from tests.conftest import client


# Configuração da fixture para ser passada para os testes como parametro
# Pytest esta encarregado de fazer esta mágica


def test_root(client):
    """
    Esse teste tem 3 etapas: (AAA)

    1. Arrange: configurar o ambiente de teste, criando um cliente de teste
    2. Act: chamar a rota raiz da aplicação e executa a ação
    3. Assert: verificar se a resposta é a esperada e garante que a aplicação está funcionando corretamente
    4. Alguns ensinadores incluem o teardown, mas nesse caso não é necessário, que no caso é a limpeza do ambiente de teste, queda do ambiente, etc.

    """

    # Act
    response = client.get('/')

    # Assert
    assert response.status_code == 200  # Ou HTTPStatus.OK no lugar do 200
    assert response.json() == {'message': 'Hello World'}


def test_second(client):
    """
    Teste para a rota /second
    """

    # Act
    response = client.get('/second')

    # Assert
    assert response.status_code == 200
    assert response.json() == {'message': 'Hello World 2'}


def test_both_route(client):
    response_root = client.get('/')
    response_second = client.get('/second')

    assert response_root.status_code == 200
    assert response_root.json() == {'message': 'Hello World'}

    assert response_second.status_code == 200
    assert response_second.json() == {'message': 'Hello World 2'}


def test_create_user(client):
    """
    Teste para a rota /user
    """

    # Act

    response_user = client.post(
        '/user/',
        json={
            'name': 'jhones',
            'email': 'joao@exemple.com',
            'password': '123456epic',
        },
    )

    assert response_user.status_code == HTTPStatus.CREATED
    assert response_user.json() == {
        'id': 1,
        'name': 'jhones',
        'email': 'joao@exemple.com',
    }


def test_get_users(client):
    response = client.get('/user/')

    assert response.status_code == HTTPStatus.OK
    assert response.json() == {
        'users': [
            {
                'id': 1,
                'name': 'jhones',
                'email': 'joao@exemple.com',
            }
        ]
    }


def test_update_user(client):
    response = client.put(
        '/user/1',
        json={
            'name': 'jhones',
            'email': 'jhones@example.com',
            'password': '123456epic',
        },
    )

    assert response.status_code == HTTPStatus.OK
    assert response.json() == {
        'id': 1,
        'name': 'jhones',
        'email': 'jhones@example.com',
    }


def test_delete_user(client):
    response = client.delete('/user/1')

    assert response.json() == {
        'id': 1,
        'name': 'jhones',
        'email': 'jhones@example.com',
    }
