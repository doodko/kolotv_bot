from dotenv import find_dotenv
from pydantic import SecretStr
from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    model_config = SettingsConfigDict(
        env_file=find_dotenv(filename=".env", usecwd=True),
        env_file_encoding='utf-8',
        extra='allow')

    app_name: str = 'Kolo bot'
    token: SecretStr
    destination_chat: int
    db: str
    pattern: str = ""
    admins_str: str

    @property
    def admins(self):
        return [int(admin) for admin in self.admins_str.split(',')]


config = Settings()
