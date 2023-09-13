from http import HTTPStatus

import pytest

from ..utils.fake_models.user import FakeUser
from ..utils.storage.sqlite import SQLiteStorage

pytestmark = pytest.mark.asyncio


async def test_user_registration(generate_users, sqlite_get_request, make_request):
    a = await sqlite_get_request(model=FakeUser, table='user')
    assert False
