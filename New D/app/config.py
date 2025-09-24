from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    database_url: str = "sqlite:///./app.db"

    class Config:
        env_file = ".env"
        extra = "ignore"


settings = Settings()


