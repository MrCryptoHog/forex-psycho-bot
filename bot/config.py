"""
Configuration — loads settings from environment variables.
"""

import os
from dataclasses import dataclass

from dotenv import load_dotenv

load_dotenv()  # reads .env in the project root


@dataclass(frozen=True)
class Config:
    bot_token: str
    log_level: str = "INFO"


def load_config() -> Config:
    token = os.getenv("BOT_TOKEN")
    if not token:
        raise RuntimeError(
            "BOT_TOKEN not found! Create a .env file with BOT_TOKEN=your_token "
            "or set the environment variable directly."
        )
    return Config(
        bot_token=token,
        log_level=os.getenv("LOG_LEVEL", "INFO"),
    )
