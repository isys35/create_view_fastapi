import pytest

from db import manager as db_manager


@pytest.mark.usefixtures("setup")
def test_create_replybutton(client, session):
    response = client.post('/replybuttons/', json={'value': 'test_replybutton_create'})
    response_data = response.json()
    assert response.status_code == 200
    assert response_data['id'] == 2

    replybutton = db_manager.get_reply_button_by_id(session, response_data['id'])
    assert response_data['value'] == replybutton.value


@pytest.mark.usefixtures("setup")
def test_get_replybutton(client):
    response = client.get('/replybuttons/1')
    response_data = response.json()
    assert response.status_code == 200
    assert response_data['id'] == 1
    assert response_data['value'] == 'test_replybutton'


@pytest.mark.usefixtures("setup")
def test_get_replybuttons(client):
    response = client.get('/replybuttons')
    response_data = response.json()
    assert response.status_code == 200
    assert len(response_data) == 1
    assert response_data[0] == {'id': 1, 'value': 'test_replybutton'}


@pytest.mark.usefixtures("setup")
def test_update_replybutton(client, session):
    response = client.patch('/replybuttons/1', json={'value': 'updated_test_replybutton'})
    session.commit()
    response_data = response.json()
    assert response.status_code == 200
    assert response_data['status'] == True

    replybutton = db_manager.get_reply_button_by_id(session, 1)
    assert replybutton.id == 1
    assert replybutton.value == 'updated_test_replybutton'
