from http import HTTPStatus

import pytest

from ..utils.fake_models.user_frame import FakeUserFrame
from ..utils.responses.frame import CreateVideoFrame

pytestmark = pytest.mark.asyncio


async def test_frame_list_success(
    generate_users,
    generate_frames,
    generate_user_sessions,
    generate_user_frames,
    sqlite_get_request,
    make_request
):
    user = generate_users[0]

    user_frame_data = await sqlite_get_request(model=FakeUserFrame, table='user_frame', user_id=user.id)
    
    assert len(user_frame_data) == 2

    response = await make_request('POST', 'user/auth', json=user.request_data())
    
    response = await make_request('GET', 'frame', cookies=response.cookies)

    assert response.status == HTTPStatus.OK
    assert response.body['count'] == 2
    assert response.body['total_pages'] == 1
    assert response.body['results'] == [frame.response_data() for frame in generate_frames[:2]]


async def test_frame_list_forbidden(
    generate_users,
    generate_frames,
    generate_user_sessions,
    generate_user_frames,
    sqlite_get_request,
    make_request
):
    user = generate_users[1]

    user_frame_data = await sqlite_get_request(model=FakeUserFrame, table='user_frame', user_id=user.id)
    
    assert len(user_frame_data) == 3

    response = await make_request('GET', 'frame')

    assert response.status == HTTPStatus.FORBIDDEN
    assert response.body['detail'] == CreateVideoFrame.FORBIDDEN
