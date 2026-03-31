"""
Inline keyboard builders for the quiz flow.
All answer choices are presented as inline buttons so users just tap — zero typing.
"""

from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

# Letter labels for cleaner display
_LABELS = ["🅰️", "🅱️", "🅲", "🅳"]


def build_answer_keyboard(options: list[str]) -> InlineKeyboardMarkup:
    """Build a 4-button inline keyboard for a quiz question."""
    buttons = [
        [InlineKeyboardButton(
            text=f"{_LABELS[i]}  {opt}",
            callback_data=f"answer:{i}",
        )]
        for i, opt in enumerate(options)
    ]
    # Add a cancel row at the bottom
    buttons.append([
        InlineKeyboardButton(text="❌ Cancel Quiz", callback_data="cancel_quiz"),
    ])
    return InlineKeyboardMarkup(inline_keyboard=buttons)
