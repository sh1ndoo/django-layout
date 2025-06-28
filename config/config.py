import base64
import os
from pathlib import Path
from typing import Literal

from goodconf import Field, GoodConf

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "config.settings")

PROJECT_DIR = Path(__file__).parents[1].resolve()


class Config(GoodConf):
    """Configuration for {{ project_name }}"""

    DEBUG: bool = True
    ALLOWED_HOSTS: list[str] = Field(
        default=["*"],
        description="Hosts allowed to serve the site "
        "https://docs.djangoproject.com/en/{{ docs_version }}/ref/settings/#allowed-hosts",
    )
    DATABASE_URL: str = Field(
        default="sqlite:///./sqlite3.db",
        description="A string with the database URL as defined in "
        "https://github.com/jazzband/dj-database-url#url-schema",
    )
    DJANGO_ENV: Literal["development", "dev", "production"] = Field(
        default="development",
        description="Toggle deployment settings for local development or production",
    )
    SECRET_KEY: str = Field(
        initial=lambda: base64.b64encode(os.urandom(60)).decode(),
        description="A long random string you keep secret "
        "https://docs.djangoproject.com/en/{{ docs_version }}/ref/settings/#secret-key",
    )
    ENVIRONMENT: str = Field(
        "development",
        description="Name of deployed environment (e.g. 'staging', 'production')",
    )

    model_config = {"default_files": ["config.yaml"]}


config = Config()
