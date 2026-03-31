"""
ForexMindsetBot — Full Question Bank (65 questions)
====================================================
Each question is a dict with:
  - "text"    : The question string
  - "options" : List of 4 answer strings (displayed in order)
  - "scores"  : List of 4 ints mapping to each option's point value (0 or 1)

Scoring philosophy:
  • Every question has exactly ONE best-practice answer worth 1 point.
  • The other three answers score 0.
  • Total quiz score is always out of 10 (10 random questions × 1 pt each).

DESIGN PRINCIPLE — These questions are HARD on purpose:
  • Multiple options sound reasonable / "smart".
  • Wrong answers are common trader beliefs that FEEL correct.
  • The right answer often contradicts gut instinct or popular advice.
  • You need real trading psychology experience to consistently score well.

To add new questions, just append a new dict to QUESTION_BANK.
Keep the same structure and the bot picks it up automatically.
"""

from typing import TypedDict

class Question(TypedDict):
    text: str
    options: list[str]
    scores: list[int]


QUESTIONS_ORIGINAL: list[Question] = [
    # ── FOMO & Impatience (nuanced) ────────────────────────────────────
    {
        "text": "EUR/USD just broke a key resistance you'd been watching, ran 80 pips, and is now pulling back. You have no open position. Best move?",
        "options": [
            "Enter on the pullback — the breakout confirms your bias",
            "Wait for a new setup at the NEXT key level — this move is spent",
            "Enter half size on the pullback as a 'discounted' entry",
            "Set a limit order at the breakout level in case it retests",
        ],
        "scores": [0, 1, 0, 0],
    },
    {
        "text": "You've been flat for 3 days while other traders in your group are posting wins. Your strategy has given zero signals. Most honest response?",
        "options": [
            "Drop to a lower timeframe to find more signals this week",
            "Reevaluate your strategy — 3 days with no signals is a problem",
            "Stay flat and trust the process — your edge only works on YOUR setups",
            "Take one reduced-risk 'B-grade' setup just to stay active",
        ],
        "scores": [0, 0, 1, 0],
    },
    {
        "text": "Your analysis predicted GBP/JPY would drop, and it did — but you missed the entry because you were away from your desk. It's already -120 pips. Now what?",
        "options": [
            "Enter now with a wider stop — the thesis is playing out perfectly",
            "Mark it as a missed trade, journal the lesson, and look for the next setup",
            "Enter with smaller size since you're late — partial credit is better than nothing",
            "Set an alert for a retracement to a key fib level and enter if it pulls back",
        ],
        "scores": [0, 1, 0, 0],
    },
    {
        "text": "You see a 'perfect' setup on a pair at 2am, outside your normal trading hours. You…",
        "options": [
            "Set a limit order with SL/TP and go to sleep — the setup is there",
            "Skip it entirely — trading outside your hours leads to undisciplined habits",
            "Wake up early to manage it manually — can't waste a perfect setup",
            "Take it now and set a hard SL — good setups don't care about the clock",
        ],
        "scores": [0, 1, 0, 0],
    },
    {
        "text": "Every pair on your watchlist is moving EXCEPT the one you're in. Your trade is valid but slow. What's really going through your mind?",
        "options": [
            "Close the slow trade and rotate into the moving pairs",
            "Hold — but hedge with a position on one of the moving pairs",
            "Hold and stop checking the other pairs — they're not your setup",
            "Tighten your stop to breakeven and enter one of the moving pairs too",
        ],
        "scores": [0, 0, 1, 0],
    },
    # ── Revenge Trading & Loss Recovery (trap answers) ─────────────────
    {
        "text": "You just took a clean -1R loss that followed your plan perfectly. 20 minutes later, a new valid A+ setup appears on the same pair. You…",
        "options": [
            "Skip it — never trade the same pair right after a loss",
            "Take it at reduced size — the entry is valid but you're emotionally compromised",
            "Take it at full size — a valid setup is a valid setup regardless of your last trade",
            "Wait an hour first to make sure you're not revenge trading",
        ],
        "scores": [0, 0, 1, 0],
    },
    {
        "text": "You're down -3R today after two losing trades. A third A+ setup appears. What separates a disciplined trader from someone revenge trading?",
        "options": [
            "A disciplined trader would stop trading after -3R no matter what appears",
            "The answer depends on whether you feel emotional — if calm, take it; if not, skip",
            "A disciplined trader takes it because the SETUP is valid — they pre-defined their daily loss limit and haven't hit it",
            "A disciplined trader scales down to half size as protection",
        ],
        "scores": [0, 0, 1, 0],
    },
    {
        "text": "You lost because your stop got hunted by a wick, then price reversed perfectly in your direction. This has happened 3 times this month. You…",
        "options": [
            "Widen your stop losses by 10-15 pips to avoid the hunts",
            "Review all 3 trades — are you placing stops at obvious liquidity levels instead of structural ones?",
            "Switch to mental stops and exit manually to avoid getting hunted",
            "Accept it as the cost of doing business — random wicks happen",
        ],
        "scores": [0, 1, 0, 0],
    },
    {
        "text": "You blew a prop firm challenge on the last day by overtrading. You immediately consider buying another challenge. Best move?",
        "options": [
            "Buy it now — get right back on the horse",
            "Wait at least a week, journal what happened, and identify the exact behavioral trigger before trying again",
            "Go back to demo for a month to rebuild discipline",
            "Buy it but promise yourself you'll trade differently this time",
        ],
        "scores": [0, 1, 0, 0],
    },
    {
        "text": "After a -5% drawdown week, a mentor tells you to 'just keep trading your system.' But another trader says to 'take a break and come back fresh.' Who's right?",
        "options": [
            "The mentor — if you followed your rules, keep executing your edge",
            "The second trader — breaks always help after drawdowns",
            "It depends: if you followed rules, keep trading; if you broke rules, pause and diagnose",
            "Neither — you need to adjust the system to prevent another drawdown",
        ],
        "scores": [0, 0, 1, 0],
    },
    # ── Discipline & Plan Adherence (all sound good) ───────────────────
    {
        "text": "You followed your plan and took a loss. Your friend ignored his plan and accidentally caught a 5R winner. Who traded better?",
        "options": [
            "You — process over outcome, always",
            "Neither — trading can't be judged on a single trade",
            "Your friend — results are what matter at the end of the month",
            "You, but you should study why his 'accident' worked",
        ],
        "scores": [1, 0, 0, 0],
    },
    {
        "text": "Your strategy's rules say to exit at 2R, but you 'feel' this trade could run to 5R. The chart supports the extension. You…",
        "options": [
            "Move TP to 5R — adapting to what the chart shows is smart trading",
            "Take profit at 2R as planned — you can backtest the 5R idea later",
            "Close half at 2R and let the rest run to 5R — best of both worlds",
            "Trail your stop and let the market decide",
        ],
        "scores": [0, 1, 0, 0],
    },
    {
        "text": "Your backtested strategy has a win rate of 42% with 2.5R average winner. After 8 losses in your last 12 trades (33% win rate), you should…",
        "options": [
            "Stop trading it live and go back to backtesting — something's broken",
            "Keep executing — a 12-trade sample is far too small to judge a statistical edge",
            "Reduce position size by half until the win rate normalizes",
            "Add a filter to reduce the losing trades",
        ],
        "scores": [0, 1, 0, 0],
    },
    {
        "text": "Mid-trade, you notice a piece of news that could invalidate your setup but hasn't moved price yet. Your SL hasn't been hit. You…",
        "options": [
            "Close immediately — new information has changed the analysis",
            "Move SL to breakeven as protection and let it play out",
            "Hold — your SL is your risk management, let it do its job",
            "Close half and tighten the stop on the remainder",
        ],
        "scores": [1, 0, 0, 0],
    },
    {
        "text": "You just switched from scalping to swing trading. After two weeks you have zero closed trades. Your old scalping strategy had wins daily. You…",
        "options": [
            "Go back to scalping — you clearly work better with fast feedback",
            "Stay the course — swing trading requires patience you haven't built yet",
            "Run both simultaneously — scalp for income, swing for growth",
            "Modify the swing strategy to take more setups so you're not waiting as long",
        ],
        "scores": [0, 1, 0, 0],
    },
    # ── Risk Management (subtle traps) ─────────────────────────────────
    {
        "text": "You normally risk 1% per trade. An A++ confluence setup appears — your highest conviction trade in months. You…",
        "options": [
            "Size up to 2-3% — conviction-based risk scaling is professional",
            "Risk 1% — the setup quality doesn't change your risk parameters",
            "Risk 1.5% — a small bump for exceptional confluence is reasonable",
            "Risk 1% but enter on two correlated pairs to capture more from the thesis",
        ],
        "scores": [0, 1, 0, 0],
    },
    {
        "text": "Your trade is +1.8R and your TP is 2R. Price stalls and forms a reversal candle. You…",
        "options": [
            "Close it — a reversal candle at +1.8R is close enough",
            "Hold for the full 2R — don't leave money on the table",
            "Move stop to +1R and let it play out",
            "Add to the position — the stall is just consolidation before the final push",
        ],
        "scores": [0, 0, 1, 0],
    },
    {
        "text": "You're risking 1% per trade on USD/JPY and 1% on USD/CHF. Both are long USD. Your REAL risk is…",
        "options": [
            "2% — straightforward math",
            "More than 2% because the trades are correlated — your effective USD exposure is amplified",
            "Less than 2% because diversification across pairs provides some hedge",
            "Exactly 2% — correlation doesn't matter when each trade has its own SL",
        ],
        "scores": [0, 1, 0, 0],
    },
    {
        "text": "You want to take a trade but your calculated SL would be 80 pips, making a 1% risk position only 0.2 lots. You normally trade 0.5 lots minimum. You…",
        "options": [
            "Take the trade at 0.2 lots — risk management is non-negotiable",
            "Tighten the stop to 30 pips so you can trade your normal 0.5 lots",
            "Skip the trade — if you can't trade meaningful size, it's not worth your time",
            "Enter with 0.5 lots and accept the 2.5% risk — it's still relatively low",
        ],
        "scores": [1, 0, 0, 0],
    },
    {
        "text": "Your risk per trade is 1%. You have 5 open positions. Price action looks like all 5 could get stopped out in the same session. What should you have done?",
        "options": [
            "Maximum 2-3 trades open at once — hard rule",
            "Ensured the 5 trades weren't correlated before entering all of them",
            "Used 0.5% per trade when running 5+ positions so total exposure stays at ~2.5%",
            "Staggered entries so they're not all in the same phase of the trade",
        ],
        "scores": [0, 1, 0, 0],
    },
    # ── Emotional Control (hard to distinguish) ────────────────────────
    {
        "text": "You notice you always feel anxious when a trade moves against you by 20 pips, even though your SL is 50 pips away. This suggests…",
        "options": [
            "Your position size is too big for your psychological comfort",
            "You need to work on trusting your analysis more",
            "You should use a tighter stop loss to reduce the anxiety",
            "This is normal — experienced traders still feel anxious, they just manage it",
        ],
        "scores": [1, 0, 0, 0],
    },
    {
        "text": "You feel completely numb after losses — no emotion at all. This means…",
        "options": [
            "You've mastered emotional control — that's the goal",
            "You might be dissociating from risk, which can lead to reckless sizing later",
            "Your risk is appropriately sized — losses don't feel big",
            "You've reached a professional level of detachment",
        ],
        "scores": [0, 1, 0, 0],
    },
    {
        "text": "You executed your plan perfectly today and took a -2R loss. You feel calm. But your spouse asks 'how was trading?' and you get irritated. This means…",
        "options": [
            "You didn't actually process the loss — the calm was surface-level",
            "You're fine — external annoyance has nothing to do with your trade",
            "You should avoid discussing trading with family",
            "The -2R loss bothered you more than you think — leaking stress is a red flag",
        ],
        "scores": [0, 0, 0, 1],
    },
    {
        "text": "After a massive winning day (+5R), you notice you feel invincible and want to 'play with house money' tomorrow. The correct interpretation is…",
        "options": [
            "You've earned the right to be more aggressive — capitalize on momentum",
            "Euphoria is as dangerous as despair — treat tomorrow exactly like any other day",
            "Take tomorrow off to let the high settle before you trade again",
            "Trade tomorrow but reduce size to protect profits",
        ],
        "scores": [0, 1, 0, 0],
    },
    {
        "text": "You feel most confident about trades you enter without hesitation, and your 'hesitation trades' often work better. This likely means…",
        "options": [
            "Your confident trades are driven by impulse; hesitation trades involve proper deliberation",
            "You should trust your instincts more — confidence correlates with better reads",
            "The hesitation trades work because you place tighter stops out of uncertainty",
            "This is random variance — confidence level doesn't predict trade quality",
        ],
        "scores": [1, 0, 0, 0],
    },
    # ── Greed & Overtrading (tempting traps) ───────────────────────────
    {
        "text": "You've had 3 winners in a row. Your 'system' didn't show a 4th setup but you see a reasonable trade forming on a non-watchlist pair. You…",
        "options": [
            "Take it — the market is giving and you should receive",
            "Skip it entirely — your system, your rules, your watchlist only",
            "Mark it, watch how it plays out, and consider adding the pair to your watchlist if the pattern is real",
            "Take it at half size — low risk way to test whether you should expand",
        ],
        "scores": [0, 0, 1, 0],
    },
    {
        "text": "It's Friday, you're up +4% for the week. An A+ setup appears at 3pm NY close. You…",
        "options": [
            "Skip it — protect the green week, there's always Monday",
            "Take it — an A+ setup doesn't care about the calendar",
            "Take it at reduced size — good setup but protect the week",
            "Paper trade it to see what happens without risking the green week",
        ],
        "scores": [0, 1, 0, 0],
    },
    {
        "text": "You realize you've taken 6 trades today vs. your normal 2-3. All followed your rules technically. But…",
        "options": [
            "No issue — if they all followed rules, quantity doesn't matter",
            "The market probably gave 6 valid setups — it happens on volatile days",
            "You should investigate whether you subconsciously lowered your criteria — high trade count is a warning sign even when 'rules' are met",
            "Cut the day short — you've used up your daily focus capacity",
        ],
        "scores": [0, 0, 1, 0],
    },
    {
        "text": "Your TP hits at +2R but the candle closes strong. Every fibre of your being says it's going further. You already locked in profit. You…",
        "options": [
            "Re-enter with a new position — this is a NEW setup now",
            "Let it go — you executed your plan and got your R",
            "Re-enter at half size with a tight stop — worst case it's a small loss",
            "Regret not trailing your stop — adjust your rules going forward",
        ],
        "scores": [0, 1, 0, 0],
    },
    {
        "text": "Your monthly target is +6%. You hit +5.5% on the 20th. Best approach for the remaining 10 days?",
        "options": [
            "Trade normally — targets are milestones, not finish lines",
            "Reduce risk to protect the +5.5% — you're almost there",
            "Push harder — 0.5% is nothing, but overperforming builds your confidence",
            "Only take your absolute #1 highest-conviction setups for the rest of the month",
        ],
        "scores": [1, 0, 0, 0],
    },
    # ── Journaling & Self-Review (deceptive) ───────────────────────────
    {
        "text": "You journal every trade in detail but your performance hasn't improved in 6 months. The problem is likely…",
        "options": [
            "Your journaling is too detailed — simplify to key metrics only",
            "You're journaling but not REVIEWING — a journal is useless without periodic pattern analysis",
            "Journaling doesn't work for everyone — some traders improve through screen time alone",
            "You need to switch from a written journal to a visual one with screenshots",
        ],
        "scores": [0, 1, 0, 0],
    },
    {
        "text": "In your journal review, you notice your winning trades average +1.8R but your losing trades average -1.2R. Looks fine, right? The hidden issue is…",
        "options": [
            "There is no issue — positive expectancy is positive expectancy",
            "You might be cutting winners short — if your planned TP is 2R, you're leaving 0.2R on the table systematically",
            "The losses should be -1R or less if you're using proper stop losses",
            "Both B and C — you're leaving money on winners AND bleeding extra on losers",
        ],
        "scores": [0, 0, 0, 1],
    },
    {
        "text": "You review your last month and realize 80% of your losses came from Tuesday and Wednesday sessions. You should…",
        "options": [
            "Stop trading Tuesdays and Wednesdays",
            "Investigate what's different — news events, your energy, market conditions — before making any rule changes",
            "Trade Tue/Wed on demo only until the pattern resolves",
            "Reduce your risk by half on those days as a compromise",
        ],
        "scores": [0, 1, 0, 0],
    },
    {
        "text": "You track your emotions pre-trade on a 1-5 calm scale. Trades taken at level 4-5 calm have a 55% win rate. Trades at level 1-2 calm have a 38% win rate. The best response is…",
        "options": [
            "Only trade when you feel 4-5 calm — hard rule",
            "Use the data as a filter but investigate WHY low-calm trades underperform before changing rules",
            "This shows emotions cause losses — meditate more",
            "Ignore it — the sample is probably too small to mean anything",
        ],
        "scores": [0, 1, 0, 0],
    },
    {
        "text": "Your backtest shows 200 trades with 48% win rate and 2.1R avg winner. In live trading over 50 trades you have 41% win rate and 1.7R avg winner. This gap most likely reflects…",
        "options": [
            "Normal variance — 50 trades isn't enough to match backtest stats",
            "Psychological execution errors — fear is making you exit early and hesitate on entries",
            "The backtest was overfitted and real market conditions are different",
            "Slippage and spread that weren't accounted for in the backtest",
        ],
        "scores": [0, 1, 0, 0],
    },
    # ── Patience & Timing (all plausible) ──────────────────────────────
    {
        "text": "Price is 3 pips from your limit order. It reverses and starts going your intended direction without filling you. You…",
        "options": [
            "Market-order in immediately — 3 pips difference is negligible",
            "Let it go — if the order didn't fill, the setup didn't trigger",
            "Chase with a slightly worse entry — you were RIGHT about the direction",
            "Move the limit to current price for a fill at a slightly worse price",
        ],
        "scores": [0, 1, 0, 0],
    },
    {
        "text": "You wait 4 hours for your setup. It triggers. You enter. Within 30 seconds, price reverses 15 pips against you. Your SL is 40 pips away. You…",
        "options": [
            "Close at -15 and reassess — sometimes the market tells you you're wrong fast",
            "Hold — your SL is 40 pips for a reason, 15 pips of noise means nothing",
            "Reduce size by half to limit damage if it keeps going",
            "Move stop to -20 pips since money management matters",
        ],
        "scores": [0, 1, 0, 0],
    },
    {
        "text": "You enter a swing trade expecting it to play out over 3-5 days. On day 1, price moves +1R in your favor, then stalls for 48 hours. You…",
        "options": [
            "Take the +1R profit — the stall might be topping/bottoming",
            "Move SL to breakeven and tighten TP — the momentum is clearly weak",
            "Hold exactly as planned — your thesis hasn't been invalidated, 48 hours is normal for swings",
            "Add to the position — the consolidation will break in your direction if the thesis is right",
        ],
        "scores": [0, 0, 1, 0],
    },
    {
        "text": "Your setup requires an engulfing candle on the 4H. The current candle has 90 minutes left and looks like it WILL form an engulfing. You…",
        "options": [
            "Enter now — don't wait for the close when it's obviously going to engulf",
            "Wait for the 4H candle to close and confirm — early entries on unconfirmed signals is a discipline leak",
            "Enter half now and half on the close — hedging impatience while respecting the signal",
            "Set a limit order at the level and let the candle close naturally",
        ],
        "scores": [0, 1, 0, 0],
    },
    {
        "text": "Asian session: your pair is dead flat, 10-pip range. London open is in 2 hours. You…",
        "options": [
            "Pre-position for the expected London volatility at a good price",
            "Set alerts at the range highs/lows and wait for a breakout with confirmation",
            "Mark key levels but don't trade until at least 30 min after London open",
            "Trade the range extremes — buy low sell high in the box",
        ],
        "scores": [0, 1, 0, 0],
    },
    # ── Confidence & Self-Belief (all sound wise) ──────────────────────
    {
        "text": "You followed a top trader's exact system for 3 months and it's not working for you, despite working for them. Most likely reason?",
        "options": [
            "Their system requires a personality type or time commitment you don't have — edge must fit the trader",
            "You're not executing it correctly — study harder",
            "Their public results are exaggerated — don't trust gurus",
            "3 months isn't enough — commit for at least a year",
        ],
        "scores": [1, 0, 0, 0],
    },
    {
        "text": "Your strategy has been profitable for 8 months. A new indicator catches your eye and backtests well alongside your system. You should…",
        "options": [
            "Add it — backtested confirmation = safe improvement",
            "Test it on a demo account or with micro size for 2-3 months BEFORE integrating it into your live system",
            "Ignore it — never fix what isn't broken",
            "Paper trade it alongside your live system and compare results after a month",
        ],
        "scores": [0, 1, 0, 0],
    },
    {
        "text": "You're in a group where everyone uses SMC. You use classical support/resistance and it works for you. They constantly dismiss your approach. You should…",
        "options": [
            "Stay in the group for community but trade YOUR system — their opinion doesn't change your P&L",
            "Learn SMC alongside your method — multiple tools make you better",
            "Leave the group — toxic influence will eventually erode your confidence",
            "Challenge them to a public track-record comparison",
        ],
        "scores": [1, 0, 0, 0],
    },
    {
        "text": "Your confidence is highest immediately after a winning streak and lowest after a losing streak. This pattern indicates…",
        "options": [
            "Normal human psychology — just be aware of it",
            "Your confidence is outcome-dependent rather than process-dependent — this is a vulnerability",
            "You should take larger positions during winning streaks since you're more confident and accurate",
            "You need to build a bigger sample of wins to establish baseline confidence",
        ],
        "scores": [0, 1, 0, 0],
    },
    {
        "text": "You see a setup that perfectly matches your rules, but 'something feels off' — you can't articulate what. You…",
        "options": [
            "Take it — feelings aren't data, and your rules say it's valid",
            "Skip it — subconscious pattern recognition is real and worth respecting, but journal the 'why' afterward",
            "Take it at reduced size — compromise between rules and intuition",
            "Wait for the next signal — there'll always be another setup",
        ],
        "scores": [0, 1, 0, 0],
    },
    # ── Tilt & Self-Awareness (all seem right) ─────────────────────────
    {
        "text": "You realize you're on tilt AFTER you've already entered a trade impulsively. The trade is currently -5 pips. Best recovery?",
        "options": [
            "Close immediately — tilt trades should be exited the moment you recognize them",
            "Set a tight SL at -10 pips and walk away — limit damage without panic-closing",
            "Hold it and manage it normally — closing out of emotion is also a tilt behavior",
            "Add a mental stop and reduce size if you detect further tilt",
        ],
        "scores": [1, 0, 0, 0],
    },
    {
        "text": "You trade best in the morning and worst in the afternoon. But a major trade opportunity often appears at 3pm. You should…",
        "options": [
            "Trade it anyway — you can't control when setups appear",
            "Set a limit order with SL/TP in the morning and let it trigger without you watching",
            "Skip all afternoon setups — protect yourself from your worst hours",
            "Take afternoon trades but with halved position size",
        ],
        "scores": [0, 1, 0, 0],
    },
    {
        "text": "You haven't slept well in 3 nights. Markets are open. Your rules say nothing about sleep. You…",
        "options": [
            "Trade normally — your rules don't restrict this and you feel fine enough",
            "Skip the session — sleep deprivation impairs judgment even when you don't feel it",
            "Trade demo only today to stay engaged without real risk",
            "Trade but reduce size by half as a precaution",
        ],
        "scores": [0, 1, 0, 0],
    },
    {
        "text": "You look at your trading stats and realize you overtrade on Mondays (6+ trades vs. 2-3 other days). What's the smart play?",
        "options": [
            "Hard cap: maximum 3 trades on Mondays, no exceptions",
            "Don't trade Mondays at all until you understand why the pattern exists",
            "Investigate first: is it because Monday has more setup opportunities, or is it a behavioral pattern from weekend anticipation?",
            "Keep a tally sheet on Mondays and stop after 3 whether or not setups appear",
        ],
        "scores": [0, 0, 1, 0],
    },
    {
        "text": "Your partner says 'you're a different person on bad trading days — more irritable, withdrawn.' This feedback should be treated as…",
        "options": [
            "A relationship issue to discuss, not a trading issue",
            "Evidence that your position sizing is too large — losses are hitting your nervous system too hard",
            "A sign you need better work-life separation",
            "Normal — everyone's mood is affected by work performance",
        ],
        "scores": [0, 1, 0, 0],
    },
    # ── Mindset & Growth (philosophical traps) ─────────────────────────
    {
        "text": "Which statement reflects the highest level of trading psychology?",
        "options": [
            "I treat every loss as a learning opportunity",
            "I don't categorize trades as wins or losses — only as 'followed plan' or 'broke plan'",
            "I feel nothing about individual trades — only my monthly equity curve matters",
            "I celebrate wins and analyze losses to constantly improve",
        ],
        "scores": [0, 1, 0, 0],
    },
    {
        "text": "Two traders have identical strategies. Trader A makes 15% annually. Trader B makes 8%. Same system, same market. The MOST likely difference is…",
        "options": [
            "Trader A sizes more aggressively — same edge, more leverage",
            "Trader A has better execution discipline — takes every signal, exits on plan",
            "Trader A got lucky — 1 year isn't a meaningful sample",
            "Trader A has more screen time and catches more setups",
        ],
        "scores": [0, 1, 0, 0],
    },
    {
        "text": "You hear 'the market is designed to take your money.' The psychologically healthy response to this belief is…",
        "options": [
            "True — that's why you need a better strategy than most",
            "Irrelevant — the market doesn't know you exist; focus on your process, not conspiracy",
            "This mindset keeps you cautious which is actually useful",
            "Partially true — market makers do hunt stops, so trade accordingly",
        ],
        "scores": [0, 1, 0, 0],
    },
    {
        "text": "A profitable trader tells you 'I'm wrong on 55% of my trades.' Your reaction reveals your psychology level. Best response?",
        "options": [
            "They probably have terrible entries and compensate with huge R:R",
            "That's a healthy win rate for most strategies — they clearly manage risk well",
            "They'd be even more profitable if they improved their win rate",
            "55% wrong seems too high — I wouldn't use a strategy that loses more than it wins",
        ],
        "scores": [0, 1, 0, 0],
    },
    {
        "text": "You read that meditation improves trading performance. After trying it for a week, you don't notice any difference. You…",
        "options": [
            "Drop it — it doesn't work for you",
            "Keep going for at least 30-60 days — psychological habits take TIME to show results in performance",
            "Switch to a different type of meditation or breathwork",
            "It's only useful if you have emotional control problems, which maybe you don't",
        ],
        "scores": [0, 1, 0, 0],
    },
    # ── Routine & Process (subtle) ─────────────────────────────────────
    {
        "text": "You trade the London session (3am-12pm your time). You've been waking at 2:30am for months and feeling exhausted by noon. You should…",
        "options": [
            "Power through — this is what commitment looks like",
            "Go to bed earlier so you get 7-8 hours before your alarm",
            "Reassess whether London session fits your LIFE — sustainable performance requires a sustainable schedule",
            "Use caffeine strategically and nap after the session",
        ],
        "scores": [0, 0, 1, 0],
    },
    {
        "text": "Your pre-session analysis takes 2 hours, but you've noticed your best trades are often Level 1 (obvious) setups, not the complex ones you spend time on. This suggests…",
        "options": [
            "Shorten analysis — you're over-complicating it and analysis paralysis is hurting execution",
            "The complex analysis is still valuable for understanding context even if you trade simple setups",
            "You should only trade Level 1 setups and cut analysis to 30 minutes",
            "Keep the analysis but be honest about whether the extra work actually improves your edge",
        ],
        "scores": [0, 0, 0, 1],
    },
    {
        "text": "You follow a strict pre-trade checklist. One day you skip step 3 (news check) and the trade turns into a +3R winner. This experience…",
        "options": [
            "Proves step 3 is unnecessary — consider removing it",
            "Is meaningless — one trade outcome doesn't validate or invalidate a process step",
            "Shows you should be more flexible with your checklist",
            "Means you should backtest trades with and without the news check to see if it helps",
        ],
        "scores": [0, 1, 0, 0],
    },
    {
        "text": "You've been profitable 7 of the last 12 months. Someone asks 'are you a profitable trader?' Honest answer?",
        "options": [
            "Yes — 7/12 profitable months means I'm net positive",
            "It depends — I need to check my TOTAL P&L across all 12 months, not just count green months",
            "Not yet — a true profitable trader is green at least 10/12 months",
            "It's too early to tell — I need at least 2 years of data",
        ],
        "scores": [0, 1, 0, 0],
    },
    {
        "text": "You want to add a new currency pair to your watchlist. The correct process is…",
        "options": [
            "Backtest your strategy on the pair, demo trade it for 2+ weeks, then add to live",
            "Just start trading it — if your strategy is good, the pair doesn't matter",
            "Watch it for a month, note if your system generates valid signals, then start with half size",
            "Add it only if it has clean price action and good daily volume",
        ],
        "scores": [1, 0, 0, 0],
    },
    # ── Account & Capital Psychology (advanced) ────────────────────────
    {
        "text": "You moved from a $1K account to $50K funded. Your strategy hasn't changed but you notice you're cutting winners earlier. This is caused by…",
        "options": [
            "Smart adaptation — locking in profits is more important with real money on the line",
            "Dollar-amount fear — your P&L shows $500 swings instead of $10, and your brain responds to the dollar amount even though the % is identical",
            "Natural caution that will fade as you adjust to the bigger account",
            "An indication you should scale up gradually — go $10K, $25K, then $50K",
        ],
        "scores": [0, 1, 0, 0],
    },
    {
        "text": "You withdraw $5K from your $25K account for rent. Your per-trade risk should now be…",
        "options": [
            "Recalculated based on $20K — same % risk on the new smaller balance",
            "Kept the same dollar amount as before — you know your system works at this size",
            "Slightly reduced until you rebuild — you're in a psychologically weaker position now",
            "Same dollar amount but fewer trades per week to compensate",
        ],
        "scores": [1, 0, 0, 0],
    },
    {
        "text": "You compound your account for 4 months: $10K → $14K. Then you hit a -10% drawdown ($14K → $12.6K). The loss 'feels' bigger than it should. Why?",
        "options": [
            "Because $1,400 is a large amount of real money to lose",
            "Because you're anchored to the $14K peak rather than evaluating the drawdown as a normal % of your current equity",
            "Because the drawdown wiped out a month of compounded gains",
            "Because you psychologically 'own' the compounded gains and losing them feels like losing YOUR money",
        ],
        "scores": [0, 1, 0, 0],
    },
    {
        "text": "Your prop firm pays you 80% of profits. You hit the +$4K monthly profit target on the 15th. For the remaining 15 days you…",
        "options": [
            "Stop trading — protect the payout, don't give it back",
            "Continue trading your system normally — targets are milestones, not ceilings",
            "Trade conservatively with smaller size to protect profits while staying active",
            "Use the remaining days for higher-risk experiments you wouldn't normally try",
        ],
        "scores": [0, 1, 0, 0],
    },
    {
        "text": "You check your P&L 15+ times per day, even when you have no open trades. This habit is…",
        "options": [
            "Harmless — it's just monitoring your account like checking the time",
            "A dopamine-seeking behavior that keeps you emotionally tied to outcomes instead of process",
            "Good practice — staying aware of your account balance at all times is responsible",
            "Only a problem if it causes you to trade emotionally",
        ],
        "scores": [0, 1, 0, 0],
    },
]

# Quick sanity: every question must have exactly 4 options and 4 scores
for _i, _q in enumerate(QUESTIONS_ORIGINAL):
    assert len(_q["options"]) == 4, f"Question {_i} has {len(_q['options'])} options"
    assert len(_q["scores"]) == 4, f"Question {_i} has {len(_q['scores'])} scores"
    assert sum(_q["scores"]) == 1, f"Question {_i} doesn't have exactly one correct answer"
