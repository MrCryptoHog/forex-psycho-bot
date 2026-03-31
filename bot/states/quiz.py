"""
FSM states for the psychology quiz flow.
One state per question is overkill — we use a single 'answering' state
and store the current question index in FSM data.
"""

from aiogram.fsm.state import State, StatesGroup


class QuizStates(StatesGroup):
    answering = State()  # User is actively answering questions
