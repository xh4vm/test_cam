from http import HTTPStatus

import pytest

from ..utils.fake_models.frame import FakeFrame
from ..utils.fake_models.user_frame import FakeUserFrame
from ..utils.responses.frame import CreateVideoFrame

pytestmark = pytest.mark.asyncio


async def test_frame_create_success(
    generate_users,
    generate_frames,
    generate_user_sessions,
    generate_user_frames,
    sqlite_get_request,
    make_request
):
    user = generate_users[3]

    contributors = [4]
    frame = FakeFrame()
    
    user_frame_data = await sqlite_get_request(model=FakeUserFrame, table='user_frame', user_id=user.id)
    
    assert len(user_frame_data) == 0

    await make_request('POST', 'user/auth', json=user.request_data())
    
    response = await make_request('POST', 'frame', json={**frame.request_data(), 'contributors':contributors})

    user_frame_data = await sqlite_get_request(model=FakeUserFrame, table='user_frame', user_id=user.id)

    assert len(user_frame_data) == 1

    assert response.status == HTTPStatus.CREATED
    assert response.body['message'] == CreateVideoFrame.SUCCESS.substitute(count=1)


async def test_frame_create_no_login_user(
    generate_users,
    generate_frames,
    generate_user_sessions,
    generate_user_frames,
    sqlite_get_request,
    make_request
):
    user = generate_users[4]

    contributors = [100]
    frame = FakeFrame()
    
    user_frame_data = await sqlite_get_request(model=FakeUserFrame, table='user_frame', user_id=user.id)
    assert len(user_frame_data) == 0

    await make_request('POST', 'user/auth', json=user.request_data())
    
    response = await make_request('POST', 'frame', json={**frame.request_data(), 'contributors':contributors})

    user_frame_data = await sqlite_get_request(model=FakeUserFrame, table='user_frame', user_id=user.id)
    assert len(user_frame_data) == 0

    assert response.status == HTTPStatus.CREATED
    assert response.body['message'] == CreateVideoFrame.SUCCESS.substitute(count=0)


async def test_frame_create_multiple_success(
    generate_users,
    generate_frames,
    generate_user_sessions,
    generate_user_frames,
    sqlite_get_request,
    make_request
):
    users = generate_users[5:]

    contributors = [6,7]
    frame = FakeFrame()
    
    user_frame_data = await sqlite_get_request(model=FakeUserFrame, table='user_frame', user_id=users[0].id)
    assert len(user_frame_data) == 0

    user_frame_data = await sqlite_get_request(model=FakeUserFrame, table='user_frame', user_id=users[1].id)
    assert len(user_frame_data) == 0

    await make_request('POST', 'user/auth', json=users[0].request_data())

    await make_request('POST', 'user/auth', json=users[1].request_data())
    
    response = await make_request('POST', 'frame', json={**frame.request_data(), 'contributors':contributors})

    user_frame_data = await sqlite_get_request(model=FakeUserFrame, table='user_frame', user_id=users[0].id)
    assert len(user_frame_data) == 1

    user_frame_data = await sqlite_get_request(model=FakeUserFrame, table='user_frame', user_id=users[1].id)
    assert len(user_frame_data) == 1

    assert response.status == HTTPStatus.CREATED
    assert response.body['message'] == CreateVideoFrame.SUCCESS.substitute(count=2)
