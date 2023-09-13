from http import HTTPStatus

import pytest

from ..utils.fake_models.frame import FakeFrame

pytestmark = pytest.mark.asyncio


async def test_frame(generate_frames, make_get_request):
    assert True
