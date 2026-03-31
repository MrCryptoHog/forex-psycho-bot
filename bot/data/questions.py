"""
TB's Psychology Bot — Master Question Bank Aggregator
=====================================================
Imports questions from all category bank files and merges them
into a single QUESTION_BANK list used by the quiz handler.

Each question dict:
  - "text"    : The question string
  - "options" : List of 4 answer strings
  - "scores"  : List of 4 ints (exactly one 1, rest 0)
"""

from typing import TypedDict

class Question(TypedDict):
    text: str
    options: list[str]
    scores: list[int]


# ── Import every category bank ────────────────────────────────────────
from bot.data.bank_fomo import QUESTIONS_FOMO
from bot.data.bank_revenge import QUESTIONS_REVENGE
from bot.data.bank_discipline import QUESTIONS_DISCIPLINE
from bot.data.bank_risk import QUESTIONS_RISK
from bot.data.bank_emotions import QUESTIONS_EMOTIONS
from bot.data.bank_greed import QUESTIONS_GREED
from bot.data.bank_patience import QUESTIONS_PATIENCE
from bot.data.bank_confidence import QUESTIONS_CONFIDENCE
from bot.data.bank_mindset import QUESTIONS_MINDSET
from bot.data.bank_routine import QUESTIONS_ROUTINE
from bot.data.bank_advanced import QUESTIONS_ADVANCED
from bot.data.bank_extra import QUESTIONS_EXTRA
from bot.data.bank_original import QUESTIONS_ORIGINAL

# ── Merge into one master list ────────────────────────────────────────
QUESTION_BANK: list[Question] = [
    *QUESTIONS_FOMO,
    *QUESTIONS_REVENGE,
    *QUESTIONS_DISCIPLINE,
    *QUESTIONS_RISK,
    *QUESTIONS_EMOTIONS,
    *QUESTIONS_GREED,
    *QUESTIONS_PATIENCE,
    *QUESTIONS_CONFIDENCE,
    *QUESTIONS_MINDSET,
    *QUESTIONS_ROUTINE,
    *QUESTIONS_ADVANCED,
    *QUESTIONS_EXTRA,
    *QUESTIONS_ORIGINAL,
]

# ── Validation ────────────────────────────────────────────────────────
for _i, _q in enumerate(QUESTION_BANK):
    assert len(_q["options"]) == 4, f"Q{_i} has {len(_q['options'])} options (need 4)"
    assert len(_q["scores"]) == 4, f"Q{_i} has {len(_q['scores'])} scores (need 4)"
    assert sum(_q["scores"]) == 1, f"Q{_i} doesn't have exactly one correct answer"
