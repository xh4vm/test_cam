from http import HTTPStatus

import pytest

from ..utils.fake_models.frame import FakeFrame
from ..utils.responses.frame import CreateVideoFrame

pytestmark = pytest.mark.asyncio
user_data = {'email': 'user1@test.ru', 'password': 'test123!@#'}


async def test_frame_create_success(generate_users, generate_user_sessions, sqlite_get_request, make_request_context):
    new_frame = {'cam_id': 99, 'TimeSection': '01-01-2023:01-01-01'}
    contributors = [1,2,3]
    frame = FakeFrame(**new_frame)
    
    frame_data = await sqlite_get_request(model=FakeFrame, table='frame', **new_frame)
    
    assert len(frame_data) == 0

    response = await make_request_context('POST', 'frame', json={**frame.request_data(), 'contributors':contributors})

    frame_data = await sqlite_get_request(model=FakeFrame, table='frame', **new_frame)

    assert len(frame_data) == 1

    assert response.status == HTTPStatus.CREATED
    assert response.body['message'] == CreateVideoFrame.SUCCESS
