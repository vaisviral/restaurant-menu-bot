from pydantic_settings import BaseSettings, SettingsConfigDict


class SettingsDB(BaseSettings):
    model_config = SettingsConfigDict(env_file=".env")

    POSTGRESQL_HOST: str
    POSTGRESQL_PORT: str
    POSTGRESQL_USER: str
    POSTGRESQL_PASSWORD: str
    POSTGRESQL_DATABASE: str
    POSTGRESQL_SCHEMA: str


settings_db = SettingsDB(_env_file="../.env")
print(settings_db)
