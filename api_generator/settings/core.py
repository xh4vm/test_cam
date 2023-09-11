from pydantic import BaseSettings, Field


class ApiSettings(BaseSettings):
    URL: str = Field('http://localhost', env='API_URL')
    PORT: str = Field('80', env='API_PORT')
    PATH: str = Field('/api', env='API_PATH')
    VERSION: str = Field('v1', env='API_VERSION')

    class Config:
        env_prefix = 'API_'
