from pydantic import BaseSettings
from dotenv import load_dotenv
from pathlib import Path
import os

env_path = Path('app') / '.env'
load_dotenv(dotenv_path=env_path)

class Settings(BaseSettings):
    database_hostname: str
    database_port: int
    database_password: str
    database_name: str
    database_username: str
    secret_key: str
    algorithm: str
    access_token_expire_minutes: int

    class Config:
        env_file = str(env_path)

settings = Settings()
print(settings.dict())
