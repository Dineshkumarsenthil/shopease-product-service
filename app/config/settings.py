from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    app_name: str = "ShopEase Product Service"
    app_version: str = "1.0.0"
    port: int = 8003

    model_config = SettingsConfigDict(env_file=".env")


settings = Settings()