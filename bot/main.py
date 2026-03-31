"""
ForexMindsetBot — Main entry point.
Run with: python -m bot.main
"""

from __future__ import annotations

import asyncio
import logging
import sys

from aiogram import Bot, Dispatcher
from aiogram.client.default import DefaultBotProperties
from aiogram.fsm.storage.memory import MemoryStorage

from bot.config import load_config
from bot.handlers.common import router as common_router
from bot.handlers.quiz import router as quiz_router


def setup_logging(level: str) -> None:
    """Configure structured logging for the entire app."""
    logging.basicConfig(
        level=getattr(logging, level.upper(), logging.INFO),
        format="%(asctime)s | %(levelname)-8s | %(name)s | %(message)s",
        datefmt="%Y-%m-%d %H:%M:%S",
        stream=sys.stdout,
    )
    # Silence noisy third-party loggers
    logging.getLogger("aiogram.event").setLevel(logging.WARNING)
    logging.getLogger("aiohttp.access").setLevel(logging.WARNING)


async def main() -> None:
    """Initialize and start the bot with long-polling."""
    config = load_config()
    setup_logging(config.log_level)

    logger = logging.getLogger(__name__)
    logger.info("Starting ForexMindsetBot...")

    # ── Storage (swap MemoryStorage → RedisStorage here if needed) ──
    storage = MemoryStorage()
    # To use Redis instead:
    # from aiogram.fsm.storage.redis import RedisStorage
    # storage = RedisStorage.from_url("redis://localhost:6379/0")

    bot = Bot(
        token=config.bot_token,
        default=DefaultBotProperties(parse_mode=None),
    )
    dp = Dispatcher(storage=storage)

    # Register routers (order matters — first match wins)
    dp.include_router(common_router)
    dp.include_router(quiz_router)

    # Set bot commands for the Telegram menu
    from aiogram.types import BotCommand

    await bot.set_my_commands([
        BotCommand(command="psychology", description="🧠 Take the trading psychology quiz"),
        BotCommand(command="cancel", description="❌ Cancel the current quiz"),
        BotCommand(command="help", description="📖 Show help"),
    ])

    logger.info("Bot is live! Polling for updates...")

    try:
        await dp.start_polling(bot, allowed_updates=dp.resolve_used_update_types())
    finally:
        await bot.session.close()
        logger.info("Bot shut down gracefully.")


if __name__ == "__main__":
    asyncio.run(main())
