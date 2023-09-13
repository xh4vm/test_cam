from http import HTTPStatus

import pytest

from ..utils.fake_models.user import FakeUser

pytestmark = pytest.mark.asyncio


import asyncio
import aiosqlite
from dataclasses import dataclass
from typing import Any, Optional

import aiohttp
import pytest
from multidict import CIMultiDictProxy

from ..utils.data_generators.sqlite.user import UserDataGenerator
from ..settings import CONFIG


async def test_user_registration(generate_users, make_get_request):
    assert False
