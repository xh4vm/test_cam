from http import HTTPStatus

import pytest

from ..utils.responses.frame import CreateVideoFrame


pytestmark = pytest.mark.asyncio


async def test_frame_detail_success(
    generate_users,
    generate_frames,
    generate_user_sessions,
    generate_user_frames,
    sqlite_get_request,
    make_request
):
    user = generate_users[0]
    frame = generate_frames[0]

    response = await make_request('POST', 'user/auth', json=user.request_data())
    
    response = await make_request('GET', f'frame/{frame.id}', cookies=response.cookies)

    assert response.status == HTTPStatus.OK
    assert response.body == frame.response_data()


async def test_frame_detail_idor_check(
    generate_users,
    generate_frames,
    generate_user_sessions,
    generate_user_frames,
    sqlite_get_request,
    make_request
):
    user = generate_users[0]
    frame = generate_frames[0]

    response = await make_request('POST', 'user/auth', json=user.request_data())
    
    response = await make_request('GET', f'frame/99', cookies=response.cookies)

    assert response.status == HTTPStatus.NOT_FOUND


async def test_frame_detail_forbidden(
    generate_users,
    generate_frames,
    generate_user_sessions,
    generate_user_frames,
    sqlite_get_request,
    make_request
):
    frame = generate_frames[0]

    response = await make_request('GET', f'frame/{frame.id}')

    assert response.status == HTTPStatus.FORBIDDEN
    assert response.body['detail'] == CreateVideoFrame.FORBIDDEN
