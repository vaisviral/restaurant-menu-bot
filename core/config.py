import pydantic as pd
import typing as tp
from pydantic_settings import BaseSettings, SettingsConfigDict


class SettingsDB(BaseSettings):
    model_config = SettingsConfigDict()

    POSTGRESQL_HOST: tp.Optional[str] = None
    POSTGRESQL_PORT: tp.Optional[int] = None
    POSTGRESQL_USER: tp.Optional[str] = None
    POSTGRESQL_PASSWORD: tp.Optional[str] = None
    POSTGRESQL_DATABASE: tp.Optional[str] = None
    POSTGRESQL_SCHEMA: tp.Optional[str] = None
    DATABASE_URI: tp.Union[tp.Optional[pd.PostgresDsn], tp.Optional[str]] = None

    @pd.field_validator("DATABASE_URI", mode="before")
    @classmethod
    def assemble_db_connection(
            cls,
            value: tp.Optional[str],
            values: pd.ValidationInfo
    ) -> tp.Any:
        if isinstance(value, str):
            return value
        return pd.PostgresDsn.build(
            scheme="postgresql",
            username=values.data.get("POSTGRESQL_USER"),
            password=values.data.get("POSTGRESQL_PASSWORD"),
            host=values.data.get("POSTGRESQL_HOST"),
            port=values.data.get("POSTGRESQL_PORT"),
            path=f"{values.data.get('POSTGRESQL_DATABASE') or ''}",
        )


settings_db = SettingsDB(_env_file="../.env")
settings_db_test = SettingsDB(_env_file="../test_db.env")
print(f"{settings_db.DATABASE_URI.unicode_string()}")
print(f"{settings_db_test.DATABASE_URI.unicode_string()}")
