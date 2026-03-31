"""
Quiz command handlers — /psychology, answer callbacks, /cancel.
All per-user state is managed via aiogram FSM (MemoryStorage by default).
"""

from __future__ import annotations

import logging
import random

from aiogram import F, Router
from aiogram.filters import Command
from aiogram.fsm.context import FSMContext
from aiogram.types import CallbackQuery, Message

from bot.data.questions import QUESTION_BANK
from bot.data.scoring import get_result
from bot.keyboards.quiz_kb import build_answer_keyboard
from bot.states.quiz import QuizStates

logger = logging.getLogger(__name__)

router = Router(name="quiz")

QUIZ_LENGTH = 10  # questions per session


# ── Helpers ────────────────────────────────────────────────────────────────

def _progress_bar(current: int, total: int = QUIZ_LENGTH) -> str:
    """Sexy little progress bar for question headers."""
    filled = "🟢" * current
    empty = "⚫" * (total - current)
    return f"{filled}{empty}  ({current}/{total})"


async def _send_question(target: Message | CallbackQuery, state: FSMContext) -> None:
    """Send the next question or finalize the quiz."""
    data = await state.get_data()
    index: int = data["current_index"]
    questions: list[dict] = data["questions"]
    score: int = data["score"]

    if index >= QUIZ_LENGTH:
        # Quiz complete — deliver results (using HTML for rich tips formatting)
        await state.clear()
        result_text = get_result(score)
        final_msg = (
            f"{'─' * 28}\n"
            f"🧠 <b>QUIZ COMPLETE</b> 🧠\n"
            f"{'─' * 28}\n\n"
            f"{result_text}\n\n"
            f"{'─' * 28}\n"
            f"<i>Type /psychology to retake anytime. Every quiz is different!</i> 🔄"
        )
        if isinstance(target, CallbackQuery):
            await target.message.edit_text(final_msg, parse_mode="HTML")
        else:
            await target.answer(final_msg, parse_mode="HTML")
        logger.info("Quiz completed | score=%d/10", score)
        return

    # Send the next question
    q = questions[index]
    question_num = index + 1
    progress = _progress_bar(question_num)

    text = (
        f"*Question {question_num} of {QUIZ_LENGTH}*\n"
        f"{progress}\n\n"
        f"_{_escape_md(q['text'])}_"
    )
    kb = build_answer_keyboard(q["options"])

    if isinstance(target, CallbackQuery):
        await target.message.edit_text(text, reply_markup=kb, parse_mode="MarkdownV2")
    else:
        await target.answer(text, reply_markup=kb, parse_mode="MarkdownV2")


def _escape_md(text: str) -> str:
    """Escape MarkdownV2 special characters."""
    special = r"_*[]()~`>#+-=|{}.!\\"
    for ch in special:
        text = text.replace(ch, f"\\{ch}")
    return text


# ── /psychology — Start the quiz ──────────────────────────────────────────

@router.message(Command("psychology"))
async def cmd_psychology(message: Message, state: FSMContext) -> None:
    """Start a fresh 10-question psychology quiz."""
    # Pick 10 random questions from the bank
    selected = random.sample(QUESTION_BANK, k=QUIZ_LENGTH)
    random.shuffle(selected)

    await state.set_state(QuizStates.answering)
    await state.update_data(
        questions=selected,
        current_index=0,
        score=0,
    )

    welcome = (
        f"{'─' * 28}\n"
        f"🧠 *FOREX MINDSET CHECK* 🧠\n"
        f"{'─' * 28}\n\n"
        f"Alright trader, let's see where your head's at\\. 💭\n\n"
        f"📋 *10 questions* about your trading psychology\n"
        f"⏱️ Takes about *2 minutes*\n"
        f"🎯 Score out of *10*\n"
        f"💡 Personalized tips at the end\n\n"
        f"_Tap the answers below — no typing needed\\._\n"
        f"_Hit /cancel anytime to stop\\._\n\n"
        f"Let's go\\! 🚀"
    )
    await message.answer(welcome, parse_mode="MarkdownV2")
    await _send_question(message, state)

    logger.info(
        "Quiz started | user=%s (%s)",
        message.from_user.id,
        message.from_user.full_name,
    )


# ── Answer callback ───────────────────────────────────────────────────────

@router.callback_query(QuizStates.answering, F.data.startswith("answer:"))
async def on_answer(callback: CallbackQuery, state: FSMContext) -> None:
    """Process an answer tap and move to the next question."""
    await callback.answer()  # dismiss the loading spinner instantly

    choice_index = int(callback.data.split(":")[1])
    data = await state.get_data()

    current_index: int = data["current_index"]
    questions: list[dict] = data["questions"]
    score: int = data["score"]

    # Score the answer
    q = questions[current_index]
    points = q["scores"][choice_index]
    new_score = score + points

    await state.update_data(
        current_index=current_index + 1,
        score=new_score,
    )

    logger.debug(
        "Answer | user=%s q=%d choice=%d pts=%d total=%d",
        callback.from_user.id,
        current_index + 1,
        choice_index,
        points,
        new_score,
    )

    await _send_question(callback, state)


# ── Cancel via inline button ──────────────────────────────────────────────

@router.callback_query(F.data == "cancel_quiz")
async def on_cancel_button(callback: CallbackQuery, state: FSMContext) -> None:
    """Cancel the quiz via the inline button."""
    await callback.answer()
    current = await state.get_state()
    await state.clear()

    if current:
        await callback.message.edit_text(
            "❌ *Quiz cancelled\\.* No worries — come back anytime\\!\n"
            "_Type /psychology when you're ready to go again\\._ 🔄",
            parse_mode="MarkdownV2",
        )
    else:
        await callback.message.edit_text("No active quiz to cancel\\. 🤷", parse_mode="MarkdownV2")


# ── /cancel command ───────────────────────────────────────────────────────

@router.message(Command("cancel"))
async def cmd_cancel(message: Message, state: FSMContext) -> None:
    """Cancel the active quiz via /cancel command."""
    current = await state.get_state()
    await state.clear()

    if current:
        await message.answer(
            "❌ *Quiz cancelled\\.* No worries, trader\\!\n"
            "_Type /psychology when you're ready for round two\\._ 💪",
            parse_mode="MarkdownV2",
        )
        logger.info("Quiz cancelled by user %s", message.from_user.id)
    else:
        await message.answer(
            "Nothing to cancel — you don't have an active quiz\\. 🤷\n"
            "_Type /psychology to start one\\!_",
            parse_mode="MarkdownV2",
        )
