from helpers import *


def test_create_user(client):
    response = adicionar_contato(client)
    res_data = response.get_json()
    assert response.status_code == 201
    assert str(type(response.get_json())) == "<class 'dict'>"
    assert res_data.get('contato').get("nome") == CONTATO_DATA.get('nome')
    assert res_data.get('contato').get('telefone') == CONTATO_DATA.get('telefone')

def test_listar_contatos(client):
    adicionar_contato(client)

    response = listar_contatos(client)
    assert response.status_code == 200
    assert str(type(response.get_json())) == "<class 'list'>"
    assert response.get_json()[0].get('nome') == CONTATO_DATA.get('nome')
    assert response.get_json()[0].get('telefone') == CONTATO_DATA.get('telefone')

def test_remover_contato(client):
    # create the user first
    adicionar_contato(client)

    # then get the user by email
    response = remover_contato(client)
    assert response.status_code == 200
    assert str(type(response.get_json())) == "<class 'dict'>"
    assert response.get_json().get('mensagem') == 'Contato removido com sucesso.'
