from http import HTTPStatus

import pytest

from ..utils.fake_models.user import FakeUser

pytestmark = pytest.mark.asyncio


async def test_user_registration(generate_users, make_get_request):
    assert False
