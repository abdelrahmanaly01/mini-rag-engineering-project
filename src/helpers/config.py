from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):

    APP_NAME: str 
    APP_VERSION: str
    
    ALLOWED_FILE_TYPES: list[str] 
    MAX_FILE_SIZE: int 

    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8",
    )


def get_settings()-> Settings:
    return Settings()