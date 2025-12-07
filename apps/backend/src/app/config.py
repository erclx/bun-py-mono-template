from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    model_config = SettingsConfigDict(
        env_file='.env',
        env_file_encoding='utf-8',
        case_sensitive=False,
    )

    APP_HOST: str = '127.0.0.1'
    APP_PORT: int = 8000
    ALLOWED_ORIGINS: list[str] = [
        'http://localhost:5173',
        'http://127.0.0.1:5173',
    ]


settings = Settings()
