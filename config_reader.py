from pydantic import BaseSettings, SecretStr


class Settings(BaseSettings):
    app_name: str = 'Kolo bot'
    token: SecretStr
    superuser_id: int

    class Config:
        env_file = ".env"


config = Settings()
