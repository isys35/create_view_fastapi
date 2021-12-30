import pytest
from db import manager as db_manager


@pytest.mark.usefixtures("setup")
def test_get_commands(client):
    response = client.get('/commands')
    response_data = response.json()
    assert response.status_code == 200
    assert len(response_data) == 1
    assert response_data[0] == {'id': 1, 'value': 'test_command'}


@pytest.mark.usefixtures("setup")
def test_create_command(client, session):
    response = client.post('/commands/', json={'value': 'test_create_command'})
    response_data = response.json()
    assert response.status_code == 200
    assert response_data['id'] == 2

    command = db_manager.get_command_by_id(session, response_data['id'])
    assert response_data['value'] == command.value


@pytest.mark.usefixtures("setup")
def test_get_command(client):
    response = client.get('/commands/1')
    response_data = response.json()
    assert response.status_code == 200
    assert response_data['id'] == 1
    assert response_data['value'] == 'test_command'


@pytest.mark.usefixtures("setup")
def test_delete_command(client, session):
    response = client.delete('/commands/1')
    response_data = response.json()
    assert response.status_code == 200
    assert response_data['status'] == True

    command = db_manager.get_command_by_id(session, 1)
    assert None == command


@pytest.mark.usefixtures("setup")
def test_update_command(client, session):
    response = client.patch('/commands/1', json={'value': 'updated_test_command'})
    session.commit()
    response_data = response.json()
    assert response.status_code == 200
    assert response_data['status'] == True

    command = db_manager.get_command_by_id(session, 1)
    assert command.id == 1
    assert command.value == 'updated_test_command'
