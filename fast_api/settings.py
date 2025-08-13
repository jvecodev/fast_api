# fast_api/settings.py
from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    MONGO_URI: str
    MONGO_DB: str

    class Config:
        env_file = ".env"  
        extra = "ignore"

settings = Settings()
