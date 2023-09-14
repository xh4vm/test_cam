from http import HTTPStatus

import pytest

from ..utils.fake_models.user import FakeUser
from ..utils.responses.user import RegistrationResponse

pytestmark = pytest.mark.asyncio


async def test_user_registration_success(
    generate_users, sqlite_get_request, make_request
):
    user_email = "new-user@test.ru"
    user = FakeUser(email=user_email, password="test123!@#")

    user_data = await sqlite_get_request(model=FakeUser, table="user", email=user_email)

    assert len(user_data) == 0

    response = await make_request("POST", "user/registration", json=user.request_data())

    user_data = await sqlite_get_request(model=FakeUser, table="user", email=user_email)

    assert len(user_data) == 1

    assert response.status == HTTPStatus.CREATED
    assert response.body["message"] == RegistrationResponse.SUCCESS


async def test_user_registration_already_exists(
    generate_users, sqlite_get_request, make_request
):
    user = generate_users[0]

    user_data = await sqlite_get_request(model=FakeUser, table="user", email=user.email)

    assert len(user_data) == 1

    response = await make_request("POST", "user/registration", json=user.request_data())

    user_data = await sqlite_get_request(model=FakeUser, table="user", email=user.email)

    assert len(user_data) == 1

    assert response.status == HTTPStatus.BAD_REQUEST
    assert RegistrationResponse.ALREADY_EXISTS in response.body["email"]


async def test_user_registration_bad_email(make_request):
    user_email = "new-user"
    user = FakeUser(email=user_email, password="test123!@#")

    response = await make_request("POST", "user/registration", json=user.request_data())

    assert response.status == HTTPStatus.BAD_REQUEST
    assert RegistrationResponse.INVALID_EMAIL in response.body["email"]


async def test_user_registration_numeric_password(
    generate_users, sqlite_get_request, make_request
):
    user_email = "new-user@test.ru"
    user = FakeUser(email=user_email, password="1234567890")

    user_data = await sqlite_get_request(model=FakeUser, table="user", email=user_email)

    assert len(user_data) == 0

    response = await make_request("POST", "user/registration", json=user.request_data())

    user_data = await sqlite_get_request(model=FakeUser, table="user", email=user_email)

    assert len(user_data) == 0

    assert response.status == HTTPStatus.BAD_REQUEST
    assert RegistrationResponse.PASSWORD_NUMERIC in response.body["password"]


async def test_user_registration_min_length_password(
    generate_users, sqlite_get_request, make_request
):
    user_email = "new-user@test.ru"
    user = FakeUser(email=user_email, password="t3St")

    user_data = await sqlite_get_request(model=FakeUser, table="user", email=user_email)

    assert len(user_data) == 0

    response = await make_request("POST", "user/registration", json=user.request_data())

    user_data = await sqlite_get_request(model=FakeUser, table="user", email=user_email)

    assert len(user_data) == 0

    assert response.status == HTTPStatus.BAD_REQUEST
    assert RegistrationResponse.PASSWORD_LENGTH in response.body["password"]
