"""
Common handler: /start, /help.
"""

from aiogram import Router
from aiogram.filters import CommandStart, Command
from aiogram.types import Message

router = Router(name="common")


@router.message(CommandStart())
async def cmd_start(message: Message) -> None:
    await message.answer(
        "🧠 *Welcome to TB's Psychology Bot\\!*\n\n"
        "I'm your personal forex trading psychology coach, "
        "built exclusively for the @TradingBrew community\. ☕\n\n"
        "🔹 /psychology — Start a 10\\-question mindset quiz\n"
        "🔹 /cancel — Stop the quiz at any time\n"
        "🔹 /help — See this message again\n\n"
        "_Every quiz is randomly generated from 65\\+ questions — "
        "no two runs are the same\\!_ 🎲\n\n"
        "Not in the group yet\\? Join us 👉 @TradingBrew\n\n"
        "Ready to see where your head's at\\? Let's gooo\\! 🚀",
        parse_mode="MarkdownV2",
    )


@router.message(Command("help"))
async def cmd_help(message: Message) -> None:
    await message.answer(
        "📖 *TB's Psychology Bot — Commands*\n\n"
        "🔹 /psychology — Take the trading psychology quiz \\(10 Qs\\)\n"
        "🔹 /cancel — Stop the current quiz\n"
        "🔹 /help — Show this help message\n\n"
        "Join the community 👉 @TradingBrew\n\n"
        "_Built for traders who take their mental game seriously\\._ 💪",
        parse_mode="MarkdownV2",
    )
