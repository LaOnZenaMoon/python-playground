import os

from dotenv import load_dotenv

from src.core.constants import APP_ENV_LOCAL


def get_env_values(*keys):
    env = get_app_env()
    load_dotenv(f".env.{env}")

    if len(keys) == 1:
        return os.getenv(keys[0])

    return [os.getenv(key) for key in keys]


def get_app_env():
    return os.getenv("APP_ENV", APP_ENV_LOCAL)


def get_app_name():
    return os.getenv("APP_NAME", "ai-newsletter-backend")
