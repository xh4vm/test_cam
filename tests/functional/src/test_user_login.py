from http import HTTPStatus

import pytest

from ..utils.fake_models.user import FakeUser 
from ..utils.fake_models.user_session import FakeUserSession 
from ..utils.responses.user import LoginResponse

pytestmark = pytest.mark.asyncio


async def test_user_login_success(generate_users, generate_user_sessions, sqlite_get_request, make_request):
    user = generate_users[0]
    
    login_data = await sqlite_get_request(model=FakeUserSession, table='user_session', user_id=user.id)
    
    assert len(login_data) == 0

    response = await make_request('POST', 'user/auth', json=user.request_data())

    login_data = await sqlite_get_request(model=FakeUserSession, table='user_session', user_id=user.id)
    
    assert len(login_data) == 1

    assert response.status == HTTPStatus.OK
    assert response.body['message'] == LoginResponse.SUCCESS


async def test_user_login_failure(generate_users, generate_user_sessions, sqlite_get_request, make_request):
    user = generate_users[1]
    user.password = 'wrong_password'
    
    login_data = await sqlite_get_request(model=FakeUserSession, table='user_session', user_id=user.id)

    assert len(login_data) == 0

    response = await make_request('POST', 'user/auth', json=user.request_data())

    login_data = await sqlite_get_request(model=FakeUserSession, table='user_session', user_id=user.id)
    
    assert len(login_data) == 0

    assert response.status == HTTPStatus.UNAUTHORIZED
    assert response.body['message'] == LoginResponse.INVALID


async def test_user_login_missing(generate_users, generate_user_sessions, sqlite_get_request, make_request):
    user = generate_users[0]
    user_data = await sqlite_get_request(model=FakeUser, table='user', email=user.email)
    
    assert len(user_data) == 1

    response = await make_request('POST', 'user/auth')

    assert response.status == HTTPStatus.BAD_REQUEST
    assert response.body['message'] == LoginResponse.MISSING
