import os
from pydantic import Field
from pydantic_settings import BaseSettings


class ApiSettings(BaseSettings):
    URL: str = Field("http://localhost")
    PORT: str = Field("8000")
    PATH: str = Field("/api")
    VERSION: str = Field("v1")

    class Config:
        env_prefix = "TEST_API_"


class DBSettings(BaseSettings):
    BASE: str
    
    class Config:
        env_prefix = "TEST_DB_"


class Config(BaseSettings):
    API: ApiSettings = ApiSettings()
    DB: DBSettings = DBSettings()
    BASE_DIR: str = os.path.dirname(os.path.abspath(__file__))


CONFIG = Config()
