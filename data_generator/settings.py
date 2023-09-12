import os
from pydantic import Field
from pydantic_settings import BaseSettings


class ApiSettings(BaseSettings):
    URL: str = Field("http://localhost", env="API_URL")
    PORT: str = Field("80", env="API_PORT")
    PATH: str = Field("/api", env="API_PATH")
    VERSION: str = Field("v1", env="API_VERSION")

    class Config:
        env_prefix = "API_"


class Config(BaseSettings):
    API: ApiSettings = ApiSettings()
    BASE_DIR: str = os.path.dirname(os.path.abspath(__file__))


CONFIG = Config()
