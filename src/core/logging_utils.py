import logging

from src.core.constants import APP_ENV_DEVELOP, APP_ENV_LOCAL
from src.core.file_utils import get_app_env


def get_logger(name):
    logger = logging.getLogger(name)
    if not logger.handlers:
        app_env = get_app_env()
        if app_env == APP_ENV_LOCAL or app_env == APP_ENV_DEVELOP:
            logger.setLevel(logging.DEBUG)
        else:
            logger.setLevel(logging.INFO)
        formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")
        handler = logging.StreamHandler()
        handler.setFormatter(formatter)
        logger.addHandler(handler)
    return logger
