from http import HTTPStatus

import pytest

from ..utils.fake_models.user_frame import FakeUserFrame

pytestmark = pytest.mark.asyncio


async def test_user_frame(generate_user_frames, make_request):
    assert False
