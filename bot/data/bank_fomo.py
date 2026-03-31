"""
Question Bank — Part 1: FOMO, Chasing & Impatience (150 questions)
"""

QUESTIONS_FOMO = [
    {
        "text": "EUR/USD just broke a key resistance you'd been watching, ran 80 pips, and is now pulling back. You have no open position. Best move?",
        "options": ["Enter on the pullback — the breakout confirms your bias", "Wait for a new setup at the NEXT key level — this move is spent", "Enter half size on the pullback as a 'discounted' entry", "Set a limit order at the breakout level in case it retests"],
        "scores": [0, 1, 0, 0],
    },
    {
        "text": "You've been flat for 3 days while other traders in your group are posting wins. Your strategy has given zero signals. Most honest response?",
        "options": ["Drop to a lower timeframe to find more signals this week", "Reevaluate your strategy — 3 days with no signals is a problem", "Stay flat and trust the process — your edge only works on YOUR setups", "Take one reduced-risk 'B-grade' setup just to stay active"],
        "scores": [0, 0, 1, 0],
    },
    {
        "text": "Your analysis predicted GBP/JPY would drop, and it did — but you missed the entry because you were away from your desk. It's already -120 pips. Now what?",
        "options": ["Enter now with a wider stop — the thesis is playing out perfectly", "Mark it as a missed trade, journal the lesson, and look for the next setup", "Enter with smaller size since you're late — partial credit is better than nothing", "Set an alert for a retracement to a key fib level and enter if it pulls back"],
        "scores": [0, 1, 0, 0],
    },
    {
        "text": "You see a 'perfect' setup on a pair at 2am, outside your normal trading hours. You…",
        "options": ["Set a limit order with SL/TP and go to sleep — the setup is there", "Skip it entirely — trading outside your hours leads to undisciplined habits", "Wake up early to manage it manually — can't waste a perfect setup", "Take it now and set a hard SL — good setups don't care about the clock"],
        "scores": [0, 1, 0, 0],
    },
    {
        "text": "Every pair on your watchlist is moving EXCEPT the one you're in. Your trade is valid but slow. What's really going through your mind?",
        "options": ["Close the slow trade and rotate into the moving pairs", "Hold — but hedge with a position on one of the moving pairs", "Hold and stop checking the other pairs — they're not your setup", "Tighten your stop to breakeven and enter one of the moving pairs too"],
        "scores": [0, 0, 1, 0],
    },
    {
        "text": "Gold is rallying hard on geopolitical news. You don't trade gold and it's not in your system. Everyone in your group is long. You…",
        "options": ["Jump in with a small position — the trend is obvious", "Stick to your pairs — FOMO trades outside your system are the #1 account killer", "Add gold to your watchlist and start learning to trade it", "Enter with tight risk — worst case it's a small loss for a huge potential gain"],
        "scores": [0, 1, 0, 0],
    },
    {
        "text": "You place a limit order at a key level. Price comes within 2 pips but doesn't fill, then moves 60 pips in your direction. You feel…",
        "options": ["Furious — you should have used a market order", "Disappointed but disciplined — the level didn't hit, so the trade didn't exist", "Motivated to widen your limit orders by a few pips next time", "Nothing special — unfilled orders are part of the game"],
        "scores": [0, 1, 0, 0],
    },
    {
        "text": "A pair you've been watching breaks out during a news release while you were away. By the time you see it, it's moved 100+ pips. Best response?",
        "options": ["Chase the entry — the breakout is confirmed by the news catalyst", "Set an alert for the next key level and wait for a fresh setup", "Enter half size with a tight stop — it might keep running", "Analyze whether the news permanently shifts the fundamental picture before doing anything"],
        "scores": [0, 0, 0, 1],
    },
    {
        "text": "Your friend made 15% this week scalping a pair you don't trade. You made 2% following your swing system. Your honest internal reaction?",
        "options": ["Jealousy — maybe I should learn scalping too", "Comfortable — 2% per week compounds to 100%+ annually, which is elite", "Motivated to find higher-frequency opportunities within my system", "Indifferent — comparing returns across different strategies is meaningless without knowing risk"],
        "scores": [0, 0, 0, 1],
    },
    {
        "text": "You're watching a trade setup develop but it hasn't triggered yet. Your entry condition is a 4H candle close above resistance. The candle has 2 hours left and looks bullish. You…",
        "options": ["Enter early — it's clearly going to close above", "Wait for the 4H candle to actually close — unconfirmed signals are gambling", "Enter half now, half on the close", "Set a buy stop a few pips above resistance so you catch it either way"],
        "scores": [0, 1, 0, 0],
    },
    {
        "text": "Three consecutive valid setups appeared while you were at work. All would have been winners. You start thinking about quitting your job to trade full-time. This thought is…",
        "options": ["Rational — if your system generates consistent winners, why not go full-time?", "Dangerous — 3 missed trades is not enough data to make a life-changing decision", "A sign you need to adjust your trading hours, not quit your job", "Worth exploring seriously if you have 12+ months of consistent profitability"],
        "scores": [0, 0, 0, 1],
    },
    {
        "text": "London session opens with a massive impulse move. No setup from your system, but the move is huge. The FOMO is real. Smart play?",
        "options": ["Enter on the first pullback — impulse + pullback is a valid strategy", "Journal the FOMO feeling and do nothing — this is your discipline being tested", "Set alerts at the next structure level in case a real setup forms after the dust settles", "Trade it with minimal size just to scratch the itch"],
        "scores": [0, 0, 1, 0],
    },
    {
        "text": "You notice you always feel anxious when you DON'T have a trade on. Sitting flat makes you uncomfortable. This reveals…",
        "options": ["You're a natural trader — the discomfort means you belong in the market", "A psychological dependency on being in the market that will lead to overtrading", "You should trade more setups to keep yourself engaged", "Nothing — everyone prefers having trades on to sitting flat"],
        "scores": [0, 1, 0, 0],
    },
    {
        "text": "Your system gave 2 signals this week. A rival system that you considered using gave 8 signals and 6 winners. You…",
        "options": ["Seriously reconsider switching — 6/8 in one week is impressive", "Recognize one week is noise — your system was backtested over hundreds of trades", "Run both systems simultaneously and compare over a month", "Blend the best elements of both systems"],
        "scores": [0, 1, 0, 0],
    },
    {
        "text": "You're at a family dinner and check your phone. A perfect setup just formed. You have 5 minutes to enter. You…",
        "options": ["Enter it from your phone — a setup is a setup", "Put the phone away — entering on mobile at a dinner breaks every process rule you have", "Excuse yourself to the bathroom and enter it properly", "Set a limit order quickly and get back to dinner"],
        "scores": [0, 1, 0, 0],
    },
    {
        "text": "A Telegram signal channel you follow posts a trade alert at the same time your system shows no signal. You…",
        "options": ["Take the signal — they have a good track record", "Ignore it — your system is the only thing you trade", "Check if their signal aligns with your own analysis, and only then consider it", "Take it with half size as a 'bonus' trade"],
        "scores": [0, 0, 1, 0],
    },
    {
        "text": "DXY is showing extreme strength. All your USD short setups are invalidated. You've been flat for a week. A weak-looking long USD setup appears. You…",
        "options": ["Take it — at least it's in the direction of the dominant trend", "Skip it — a weak setup is a weak setup regardless of the macro picture", "Take it with reduced risk since the macro supports it", "Wait for a strong setup that aligns with the DXY trend"],
        "scores": [0, 0, 0, 1],
    },
    {
        "text": "You had a great system for 6 months. This month it's underperforming while 'ICT' traders in your group are crushing it. You start watching ICT YouTube videos. This is…",
        "options": ["Smart research — you should always be learning new approaches", "Strategy-hopping behavior triggered by comparison, which will destroy your edge over time", "Fine as long as you don't change your live system based on YouTube videos", "Proof that ICT might be superior and worth switching to"],
        "scores": [0, 1, 0, 0],
    },
    {
        "text": "Price taps your entry zone but your confirmation candle pattern doesn't form. Price starts to move in your anticipated direction anyway. You…",
        "options": ["Enter — the zone tap was the important part, confirmation is optional", "Let it go — without the full setup, this is not your trade", "Enter with a tighter stop than usual as a compromise", "Follow the trade mentally to see if skipping was the right call"],
        "scores": [0, 1, 0, 0],
    },
    {
        "text": "You calculated that you missed $4,200 in potential profit this month from trades you didn't take. The correct mindset is…",
        "options": ["Calculating missed profits is useful — it identifies execution problems", "Tracking 'missed profit' is toxic — it creates FOMO and makes you chase future setups", "Use it to refine entry criteria so you catch more next month", "It's useful data only if the missed trades were actually part of your system"],
        "scores": [0, 0, 0, 1],
    },
    {
        "text": "Sunday prep: you mark 8 potential setups for the week. By Wednesday, 5 already triggered while you were sleeping (different timezone). You…",
        "options": ["Enter the remaining 3 with more conviction since the others confirmed the bias", "Adjust your trading schedule to catch more of the 8 next week", "Stick to the 3 that haven't triggered and only trade them if they set up during your hours", "Set limit orders for all 8 next week so timezone doesn't matter"],
        "scores": [0, 0, 1, 0],
    },
    {
        "text": "You see a trader on Twitter post a 20R trade. You've never had anything close to that. Your immediate thought?",
        "options": ["I need a better strategy", "That's either fake, cherry-picked, or an outlier — 20R trades are not normal", "I should study their method", "I'm clearly doing something wrong if I can't hit those numbers"],
        "scores": [0, 1, 0, 0],
    },
    {
        "text": "A new forex pair just became available on your broker. Everyone's talking about its volatility. You…",
        "options": ["Start trading it immediately — volatility means opportunity", "Watch it for at least 2-3 months, backtest your system on it, then consider", "Trade it on demo while continuing your regular live trading", "Add it to your watchlist and note its behavior during your regular analysis time"],
        "scores": [0, 1, 0, 0],
    },
    {
        "text": "Your monthly target is 4%. You're at 3.8% on the 25th. A B-grade setup appears. You…",
        "options": ["Take it — you're so close to target, one more trade seals the month", "Skip it — B-grade is B-grade, the 0.2% difference isn't worth a bad habit", "Take it at half size — low risk way to finish the month", "Your monthly target shouldn't influence individual trade decisions at all"],
        "scores": [0, 0, 0, 1],
    },
    {
        "text": "You wake up Monday and see your pair gapped 40 pips past your intended entry. The gap is in your direction but your entry price is gone. You…",
        "options": ["Enter at market — a gap in your direction is bullish confirmation", "Wait for the gap to fill before entering at your original level", "Skip it — gaps change the risk profile and your planned R:R is worse now", "Adjust your stop loss to accommodate the new entry and recalculate everything"],
        "scores": [0, 0, 1, 0],
    },
]
