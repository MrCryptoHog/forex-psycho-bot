"""
Scoring engine & personalized result generation.
Tiers:
  8-10 → Trading God 🏆
  5-7  → Solid Trader 💪
  0-4  → Diamond in the Rough 💎

NOTE: All text returned here is RAW — the handler is responsible for
      escaping it before sending with MarkdownV2 parse_mode.
      We use HTML parse_mode instead for results (simpler escaping).
"""

import random


def get_result(score: int) -> str:
    """Return a motivational result message based on the user's score (0-10).
    Uses HTML formatting tags (<b>, <i>) for Telegram's HTML parse_mode.
    """
    if score >= 8:
        return _elite_result(score)
    elif score >= 5:
        return _average_result(score)
    else:
        return _needs_work_result(score)


# ── Tier 1: 8-10 (Elite Mindset) ──────────────────────────────────────────

_ELITE_INTROS = [
    "You're operating at an elite level, trader. 🔥",
    "Your psychology is DIALED IN. Most traders dream of this mindset. 🏆",
    "You're built different. Seriously — this is top-tier mental game. 👑",
    "Absolute machine. Your psych game is institutional-grade. 🧠⚡",
]

_ELITE_POLISH_TIPS = [
    "Keep refining your journaling — even pro athletes review tape daily.",
    "Consider mentoring others; teaching deepens your own discipline.",
    "Watch for complacency — the moment you think you've 'made it' is when habits slip.",
    "Add a monthly deep-review session to spot any creeping bad habits.",
    "Experiment with meditation or breathwork to push your edge even further.",
    "Track your physical state (sleep, hydration, exercise) alongside trade performance.",
]


def _elite_result(score: int) -> str:
    intro = random.choice(_ELITE_INTROS)
    tip = random.choice(_ELITE_POLISH_TIPS)
    return (
        f"📊 <b>Your Score: {score}/10</b>\n\n"
        f"🏆 <b>ELITE MINDSET</b>\n\n"
        f"{intro}\n\n"
        f"You've got the discipline, emotional control, and self-awareness "
        f"that separate consistent winners from the crowd.\n\n"
        f"🔑 <b>One thing to keep sharpening:</b>\n"
        f"→ {tip}\n\n"
        f"Keep doing exactly what you're doing. The market rewards this mindset. 💰🧘"
    )


# ── Tier 2: 5-7 (Solid Foundation) ────────────────────────────────────────

_AVERAGE_INTROS = [
    "You've got a solid foundation — now let's sharpen those edges. 💪",
    "Good stuff, trader! You're above average, but there's another level waiting. 📈",
    "You're on the right path — a few tweaks and you'll be unstoppable. 🚀",
    "Respect the grind! You clearly take this seriously. Let's level up. ⚡",
]

_AVERAGE_TIPS = [
    "📓 <b>Journal every single trade</b> — entry reason, emotion, outcome, and lesson. Review it every Sunday. The pattern recognition from this alone can add 10-20% to your consistency.",
    "⏸️ <b>Create a 'pause protocol'</b> — after any loss, physically stand up, take 5 deep breaths, then ask: 'Would I take this next trade if I hadn't just lost?' If no → walk away.",
    "🎯 <b>Define your A+ setup in writing</b> — print it, stick it next to your monitor. If a setup doesn't match ALL criteria, it's a skip. Period.",
    "📊 <b>Track your emotions on a 1-5 scale</b> before every session. Over time you'll see exactly which emotional states produce your best (and worst) trading.",
    "🛡️ <b>Set a hard daily loss limit</b> (e.g., 2% of account) and make it non-negotiable. When you hit it, platform closes. No exceptions. Ever.",
    "🧘 <b>Add a 5-minute pre-session ritual</b>: Review your plan, check your emotional state, set intentions. This tiny habit separates amateurs from pros.",
    "📸 <b>Screenshot every trade</b> — winners AND losers. Build a visual library you review monthly. You'll spot recurring mistakes you can't see in real-time.",
    "⚡ <b>Implement the 'one-hour rule'</b>: After a loss, wait at least one hour before your next entry. This single rule eliminates 90% of revenge trades.",
]


def _average_result(score: int) -> str:
    intro = random.choice(_AVERAGE_INTROS)
    tips = random.sample(_AVERAGE_TIPS, k=min(5, len(_AVERAGE_TIPS)))
    tips_block = "\n\n".join(tips)
    return (
        f"📊 <b>Your Score: {score}/10</b>\n\n"
        f"💪 <b>SOLID FOUNDATION</b>\n\n"
        f"{intro}\n\n"
        f"You clearly have trading knowledge — the next breakthrough is purely psychological. "
        f"Here are your personalized action items:\n\n"
        f"{tips_block}\n\n"
        f"Pick 2-3 of these, implement them THIS WEEK, and watch the difference. "
        f"You're closer than you think. 🔥"
    )


# ── Tier 3: 0-4 (Needs Work — Diamond in the Rough) ──────────────────────

_NEEDS_WORK_INTROS = [
    "Real talk: your psychology needs work — but that's exactly why you took this quiz. And that takes guts. 💎",
    "Honest score, honest conversation. The fact you're assessing yourself puts you ahead of 90% of traders who never look in the mirror. 🪞",
    "This score stings — but it's also your biggest opportunity. Most blown accounts come from ignoring EXACTLY these signals. Let's fix this. 🔧",
    "Don't be discouraged — every elite trader was here at some point. Awareness is step one. Let's build from here. 🏗️",
]

_NEEDS_WORK_TIPS = [
    "📓 <b>Start a trading journal TODAY</b> — not tomorrow, not Monday. Use Notion, a spreadsheet, even a notebook. Record: pair, direction, reason for entry, emotion before/during/after, outcome, and one lesson. This is the single highest-ROI habit in trading.",
    "🛑 <b>Set an absolute daily loss limit of 1-2%</b> and enforce it like your account depends on it (because it does). When you hit it, close the platform. Go outside. The market will be there tomorrow.",
    "🧘 <b>Start a daily 10-minute meditation practice</b> — apps like Headspace or Calm work great. Meditation literally rewires your brain to reduce impulsive decisions. After 30 days, your trading WILL be different.",
    "📝 <b>Write down your trading plan on paper</b> — specific entry criteria, exit rules, risk per trade, daily loss limit, and session times. Tape it to your monitor and read it before EVERY session.",
    "⏸️ <b>Implement a mandatory 15-minute cooldown after every loss</b>. Stand up, leave your desk, do 20 pushups, drink water. This interrupts the revenge-trading circuit in your brain.",
    "🎯 <b>Reduce to ONE strategy and ONE pair for the next 30 days</b>. Simplification removes decision fatigue and gives you clean data to analyze. You can expand later.",
    "📊 <b>Review your last 20 trades tonight</b> — categorize each as (a) followed plan, or (b) broke rules. Calculate what your P&L would be if you ONLY took category (a) trades. That number will shock you.",
    "🔢 <b>Never risk more than 1% per trade until you have 3 consecutive green weeks</b>. This isn't about making money — it's about building the habit of disciplined execution.",
    "📸 <b>Screenshot your biggest 3 losses this month</b> and write exactly what emotional state led to each one. Stick these screenshots on your wall as a visual reminder.",
    "⚡ <b>Create a pre-trade checklist</b> with 5 items you MUST check before entering (e.g., HTF direction, key level, risk calculated, emotional state, news check). If any item fails → no trade.",
    "🕐 <b>Define your trading hours and NEVER trade outside them</b>. The best setups happen at predictable times. Random screen time leads to random trades.",
    "🤝 <b>Find an accountability partner</b> — someone who you report to daily. Share your trades, your rules, and your slip-ups. Accountability is the cheat code nobody uses.",
    "📚 <b>Read 'Trading in the Zone' by Mark Douglas</b> — if you haven't already, this book alone can transform how you think about probability, risk, and emotional reactions.",
    "💤 <b>Track your sleep quality alongside your trading results</b> for 2 weeks. You'll likely find that your worst trading days correlate with poor sleep. Fix the sleep, fix the performance.",
]


def _needs_work_result(score: int) -> str:
    intro = random.choice(_NEEDS_WORK_INTROS)
    tips = random.sample(_NEEDS_WORK_TIPS, k=min(10, len(_NEEDS_WORK_TIPS)))
    tips_block = "\n\n".join(f"{i+1}. {tip}" for i, tip in enumerate(tips))
    return (
        f"📊 <b>Your Score: {score}/10</b>\n\n"
        f"💎 <b>DIAMOND IN THE ROUGH</b>\n\n"
        f"{intro}\n\n"
        f"Here's your full action plan — implement these one at a time over the next 30 days:\n\n"
        f"{tips_block}\n\n"
        f"<b>Start with #1 and #2 this week.</b> "
        f"Don't try to fix everything at once — stack one habit at a time. "
        f"Come back and retake this quiz in 30 days. You WILL score higher. 🚀💪"
    )
