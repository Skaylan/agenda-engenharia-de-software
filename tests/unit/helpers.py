import os
import requests
from requests import Response
from dotenv import load_dotenv
from app import create_app, db
from tests.config_test import TestConfig
import pytest

load_dotenv()

CONTATO_DATA = {
    "nome": "test",
    "telefone": "(99) 99999-9999"
}



ENDPOINT = 'http://localhost:5000/api/v1'
SECRET_KEY = 'test-secret-key'

HEADERS = {
    "Content-Type": "application/json",
    "Service-Token": os.getenv('SERVICE_TOKEN')
}

def listar_contatos(client) -> Response:
    return client.get(ENDPOINT + '/listar_contatos', headers=HEADERS)

def adicionar_contato(client) -> Response:
    return client.post(ENDPOINT + '/adicionar_contato', json=CONTATO_DATA, headers=HEADERS)

def remover_contato(client):
    return client.delete(ENDPOINT + '/remover_contato', json=CONTATO_DATA, headers=HEADERS)
