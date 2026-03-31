"""
Inline keyboard builders for the quiz flow.
All answer choices are presented as inline buttons so users just tap — zero typing.
"""

from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

# Number emoji labels — short buttons that work on any screen size
_LABELS = ["1️⃣", "2️⃣", "3️⃣", "4️⃣"]


def build_answer_keyboard() -> InlineKeyboardMarkup:
    """Build a compact 4-button inline keyboard. Answer text is shown in the message body."""
    buttons = [
        [
            InlineKeyboardButton(text=_LABELS[0], callback_data="answer:0"),
            InlineKeyboardButton(text=_LABELS[1], callback_data="answer:1"),
            InlineKeyboardButton(text=_LABELS[2], callback_data="answer:2"),
            InlineKeyboardButton(text=_LABELS[3], callback_data="answer:3"),
        ],
        [InlineKeyboardButton(text="❌ Cancel Quiz", callback_data="cancel_quiz")],
    ]
    return InlineKeyboardMarkup(inline_keyboard=buttons)


def format_options(options: list[str]) -> str:
    """Format answer options with number labels for the message body."""
    return "\n\n".join(f"{_LABELS[i]}  {opt}" for i, opt in enumerate(options))
