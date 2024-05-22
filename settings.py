# for loading commands from cmds directory to bot dynamically
import pathlib

#[T] = Token
from dotenv import load_dotenv
import os
load_dotenv()
TOKEN = os.getenv('TOKEN')

# the path of parent directory of file.
BASE_DIR = pathlib.Path(__file__).parent
# path of cmds directory
CMDS_DIR = BASE_DIR / "cmds"
# path of cogs directory
COGS_DIR = BASE_DIR / "cogs"

#[L] = Logger
import logging
from logging.config import dictConfig
LOGGING_CONFIG = {
    "version": 1,
    "disabled_existing_Loggers": False,
    "formatters":{
        "verbose":{
            "format": "%(levelname)-10s - %(asctime)s - %(module)-15s : %(message)s"
        },
        "standard":{
            "format": "%(levelname)-10s - %(name)-15s : %(message)s"
        }
    },
    "handlers":{
        "console":{
            "level": "DEBUG",
            "class": "logging.StreamHandler",
            "formatter": "standard"
        },
        "console2":{
            "level": "WARNING",
            "class": "logging.StreamHandler",
            "formatter": "standard"
        },
        "file":{
            "level": "INFO",
            "class": "logging.FileHandler",
            "filename": "logs/infos.log",
            "mode": "w",
            "formatter": "verbose"
        }
    },
    "loggers":{
        "bot":{
            "handlers": ["console"],
            "level": "INFO",
            "propagate": False
        },
        "discord":{
            "handlers": ["console2", "file"],
            "level": "INFO",
            "propagate": False
        }
    }
}
dictConfig(LOGGING_CONFIG)