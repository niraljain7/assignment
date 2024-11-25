import os
from pydantic_settings import BaseSettings
from dotenv import load_dotenv

load_dotenv()

class Settings(BaseSettings):
    DUMMY_USERNAME: str = os.environ.get("DUMMY_USERNAME")
    DUMMY_PASSWORD: str = os.environ.get("DUMMY_PASSWORD")

    RAPID_API_HOST: str = os.environ.get("RAPID_API_HOST")
    RAPID_API_KEY: str = os.environ.get("RAPID_API_KEY")
    RAPID_API_URL: str = os.environ.get("RAPID_API_URL")

    SECRET_KEY: str = os.environ.get("SECRET_KEY")

    ACCESS_TOKEN_EXPIRE_MINUTES: int = 60

def get_settings():
    return Settings()
