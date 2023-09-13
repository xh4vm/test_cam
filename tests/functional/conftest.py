import asyncio
import aiosqlite
from dataclasses import dataclass
from typing import Any

import aiohttp
import pytest_asyncio
from multidict import CIMultiDictProxy

from .settings import CONFIG
from .utils.data_generators.sqlite.user import UserDataGenerator
from .utils.data_generators.sqlite.frame import FrameDataGenerator
from .utils.data_generators.sqlite.user_frame import UserFrameDataGenerator

SERVICE_URL = f'{CONFIG.API.URL}:{CONFIG.API.PORT}'


@dataclass
class HTTPResponse:
    body: dict[str, Any]
    headers: CIMultiDictProxy[str]
    status: int


@pytest_asyncio.fixture(scope='session')
async def session():
    session = aiohttp.ClientSession()
    yield session
    await session.close()


@pytest_asyncio.fixture(scope='session')
async def sqlite_client():
    client = await aiosqlite.connect(CONFIG.DB.BASE)

    yield client

    await client.close()


@pytest_asyncio.fixture
def make_request(session):
    async def inner(request_method: str, rest_method: str, params: dict[str, Any] | None = None) -> HTTPResponse:
        params = params or {}
        url = SERVICE_URL + f'{CONFIG.API.PATH}/{CONFIG.API.VERSION}/' + rest_method
        
        async with getattr(session, request_method)(url, params=params) as response:
            return HTTPResponse(body=await response.json(), headers=response.headers, status=response.status,)

    return inner


@pytest_asyncio.fixture(scope='session')
def event_loop():
    loop = asyncio.get_event_loop()
    yield loop
    loop.close()


@pytest_asyncio.fixture(scope='session')
async def generate_users(sqlite_client):
    user_dg = UserDataGenerator(conn=sqlite_client)

    yield await user_dg.load()

    await user_dg.clean()


@pytest_asyncio.fixture(scope='session')
async def generate_frames(sqlite_client):
    frame_dg = FrameDataGenerator(conn=sqlite_client)

    yield await frame_dg.load()

    await frame_dg.clean()


@pytest_asyncio.fixture(scope='session')
async def generate_user_frames(sqlite_client):
    user_frame_dg = UserFrameDataGenerator(conn=sqlite_client)

    yield await user_frame_dg.load()

    await user_frame_dg.clean()
