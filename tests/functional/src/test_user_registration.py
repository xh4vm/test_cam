from http import HTTPStatus

import pytest

from ..utils.fake_models.user import FakeUser
from ..utils.responses.user import RegistrationResponse

pytestmark = pytest.mark.asyncio


async def test_user_registration_success(sqlite_get_request, sqlite_delete_request, make_request):
    user_email = 'new-user@test.ru'
    user = FakeUser(email=user_email, password='test123!@#')
    
    user_data = await sqlite_get_request(model=FakeUser, table='user', email=user_email)
    
    assert len(user_data) == 0

    response = await make_request('POST', 'user/registration', json=user.request_data())

    user_data = await sqlite_get_request(model=FakeUser, table='user', email=user_email)

    assert len(user_data) == 1

    await sqlite_delete_request(model=FakeUser, table='user', email=user_email)
    
    assert response.status == HTTPStatus.CREATED
    assert response.body['message'] == RegistrationResponse.SUCCESS


async def test_user_registration_already_exists(generate_users, sqlite_get_request, make_request):
    user_email = 'user1@test.ru'
    user = FakeUser(email=user_email, password='test123!@#')
    
    user_data = await sqlite_get_request(model=FakeUser, table='user', email=user_email)
    
    assert len(user_data) == 1

    response = await make_request('POST', 'user/registration', json=user.request_data())

    user_data = await sqlite_get_request(model=FakeUser, table='user', email=user_email)

    assert len(user_data) == 1

    assert response.status == HTTPStatus.BAD_REQUEST
    assert response.body['email'] == RegistrationResponse.ALREADY_EXISTS


async def test_user_registration_bad_email(make_request):
    user_email = 'new-user'
    user = FakeUser(email=user_email, password='test123!@#')
    
    response = await make_request('POST', 'user/registration', json=user.request_data())

    assert response.status == HTTPStatus.BAD_REQUEST
    assert response.body['email'] == RegistrationResponse.INVALID_EMAIL
