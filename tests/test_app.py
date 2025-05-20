from http import HTTPStatus

def test_root_deve_retornar_ola_mundo(client):
    response = client.get('/')

    assert response.status_code == HTTPStatus.OK # assert
    assert response.json() == {'message':'Olá, mundo'} # assert


def test_create_user(client):    
    response = client.post(
        '/users/',
        json = {
            'username':'alice',
            'email': 'alice@example.com',
            'password': 'secret'
        },
    )

    assert response.status_code == HTTPStatus.CREATED
    assert response.json() == {
        'id': 1,
        'email':'alice@example.com',
        'username': 'alice'
    }

def test_read_users(client):
    response = client.get('/users/')

    assert response.status_code == HTTPStatus.OK
    assert response.json() == {
        'users': [
            {
                'username': 'alice',
                'email': 'alice@example.com',
                'id': 1,
            }
        ]
    }

def test_update_user(client):
    # Atualiza usuário
    response = client.put(
        '/users/1',
        json={
            'username': 'Bob',
            'email': 'bobd@example.com',
            'password': 'secret'
        }
    )

    assert response.status_code == HTTPStatus.OK
    assert response.json() == {
        'id': 1,
        'username': 'Bob',
        'email': 'bobd@example.com'
    }

def test_delete_user(client):
    response = client.delete('/users/1')

    assert response.status_code == HTTPStatus.OK
    assert response.json() == {
        'id': 1,
        'username': 'Bob',
        'email': 'bobd@example.com'
    }