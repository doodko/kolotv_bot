from pydantic import BaseSettings, SecretStr


class Settings(BaseSettings):
    app_name: str = 'Kolo bot'
    token: SecretStr
    superuser_id: int
    db: str
    pattern: str

    class Config:
        env_file = ".env"


config = Settings()
