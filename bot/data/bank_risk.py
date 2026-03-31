"""
Question Bank — Part 4: Risk Management Psychology (100 questions)
"""

QUESTIONS_RISK = [
    {
        "text": "You normally risk 1% per trade. A setup appears that 'feels' like a guaranteed winner. Your impulse is to risk 3%. The experienced trader knows…",
        "options": ["No setup is guaranteed — the 1% rule exists for the trade that 'can't lose' and does", "If you've backtested higher conviction sizing, 3% can be appropriate", "3% is still conservative — professionals sometimes risk 5-10%", "Trust your gut — if the conviction is there, size up"],
        "scores": [1, 0, 0, 0],
    },
    {
        "text": "Your account is $10,000. You risk 2% ($200) per trade. After growing to $15,000, you still risk $200. What's the psychological trap here?",
        "options": ["You're being smart — the original risk amount protected you during the growth phase", "You've anchored to the old dollar amount and your position sizing isn't keeping up with your account growth", "Fixed dollar risk is better than percentage risk", "You should only update risk amounts quarterly"],
        "scores": [0, 1, 0, 0],
    },
    {
        "text": "You have 3 open trades, all correlated (EUR/USD long, GBP/USD long, USD/CHF short). Your 'per-trade' risk is 1% each. Your REAL risk is…",
        "options": ["3% — that's just 3 x 1%", "Potentially much higher than 3% because correlated trades can all fail simultaneously", "Lower than 3% because diversification reduces risk", "Exactly 3% if each has its own SL"],
        "scores": [0, 1, 0, 0],
    },
    {
        "text": "Your risk management says 1% per trade. The setup requires a 150-pip stop loss. This means your position size will be small. You feel it's 'not worth it.' You should…",
        "options": ["Tighten the stop to get a bigger position — you need a meaningful size", "Take the small position — if 1% risk isn't 'worth it' to you, your account is too small, not your SL too wide", "Skip the trade and look for one with a tighter stop", "Increase risk to 2% this one time since the stop is so wide"],
        "scores": [0, 1, 0, 0],
    },
    {
        "text": "You lose 5 trades in a row at 1% each. You're down 5%. Your risk of ruin at 1% with a 55% win rate over 1000 trades is effectively 0%. Knowing this, the correct response to the streak is…",
        "options": ["Reduce risk to 0.5% until the streak ends — protect capital first", "Continue at 1% — the math says this streak is normal and expected", "Pause trading to confirm the system still works", "Continue at 1% but take only A+ setups for the next 10 trades"],
        "scores": [0, 1, 0, 0],
    },
    {
        "text": "A trader tells you: 'I risk 5% per trade because I have a 70% win rate.' What's wrong with this statement?",
        "options": ["Nothing — high win rate justifies higher risk", "A 30% chance of losing 5% means a 6-trade losing streak (statistically likely) would cost 30% of the account", "5% is too high regardless of win rate — most pros never exceed 2%", "Win rate alone doesn't determine appropriate risk — average win size and loss size matter too"],
        "scores": [0, 0, 0, 1],
    },
    {
        "text": "You set a max daily loss limit of 3%. You hit it at 11am. The rest of the day, 4 perfect setups appear. At the end of the day, you calculate that taking them would have netted +5%. The lesson is…",
        "options": ["Your daily loss limit is too strict — raise it to 5%", "The limit worked EXACTLY as designed. The 4 missed winners are survivorship bias. You can't know they'll win in advance", "Maybe have a 'pause and re-evaluate' instead of a hard cutoff", "Set the limit at 2% so you have more room to trade afterwards"],
        "scores": [0, 1, 0, 0],
    },
    {
        "text": "You're calculating position size and discover your system requires a 200-pip SL on this trade. At 1% risk, the position size feels embarrassingly small. The mature response is…",
        "options": ["Take the trade at the correct size — 'embarrassing' position sizes are what keep you in the game", "Skip it — if the SL is that wide, the trade isn't worth taking", "Use a closer SL to get a bigger size, even though the technique says 200 pips", "Trade it on a higher leverage account to get a meaningful position"],
        "scores": [1, 0, 0, 0],
    },
    {
        "text": "You're up 8% for the month. With 3 days left, you're tempted to risk 3% on a 'home run' trade to make it a 10%+ month. This temptation reveals…",
        "options": ["Healthy ambition — aim for the best possible month", "You're gambling with profits and treating gains like 'house money' — a classic psychological bias", "Nothing wrong — increasing risk when you're in profit is sound money management", "A natural desire to end the month on a high note"],
        "scores": [0, 1, 0, 0],
    },
    {
        "text": "Your friend blew his $5,000 account. He says he's going to deposit another $5,000 and 'do it right this time.' Without changing ANYTHING about his approach. Your honest advice?",
        "options": ["Deposit $500, not $5,000 — smaller account until the process proves profitable", "Don't deposit anything until you've identified WHY the first $5,000 failed", "Give it another shot — sometimes it takes multiple attempts to succeed", "Switch to a prop firm challenge to protect personal capital"],
        "scores": [0, 1, 0, 0],
    },
    {
        "text": "You're managing a trade that's +2R in profit. Your plan says TP is at +3R. Price stalls and you start getting nervous. You…",
        "options": ["Close at +2R — a bird in the hand is worth two in the bush", "Follow your plan — +3R is the target and the trade isn't giving an exit signal", "Move SL to +1.5R to protect some profit while giving room for the TP", "Partially close at +2R and let the rest run to +3R"],
        "scores": [0, 1, 0, 0],
    },
    {
        "text": "You realize you've been risking 1% per trade but averaging out at 2% losses because of slippage, spread widening, and early SL hits. Your ACTUAL risk is…",
        "options": ["Close enough to 1% — slippage is unavoidable", "2% — and you need to either adjust your calculations to account for real-world execution or reduce target risk to 0.5%", "Somewhere between 1% and 2%, which is acceptable", "You're just having bad luck with execution"],
        "scores": [0, 1, 0, 0],
    },
    {
        "text": "A mentor says: 'The most important number in your trading isn't your win rate — it's your maximum drawdown.' Why?",
        "options": ["Because drawdowns determine if you survive long enough for win rate to matter", "Win rate IS more important — you can't profit without winning", "Maximum drawdown is a lagging indicator that doesn't predict future risk", "Both are equally important"],
        "scores": [1, 0, 0, 0],
    },
    {
        "text": "You move your stop loss to breakeven early on every trade. Your win rate is 45% but your average winner is only +0.8R because most trades get stopped at breakeven. This behavior…",
        "options": ["Is smart risk management — no trade at breakeven ever becomes a loss", "Is killing your edge — the move to breakeven is so tight that winning trades don't have room to develop", "Keeps your losses small, which is the most important thing", "Needs adjustment — wait for +1R before moving to breakeven"],
        "scores": [0, 1, 0, 0],
    },
    {
        "text": "You're offered two systems. System A: 60% WR, average win 1R, average loss 1R. System B: 40% WR, average win 3R, average loss 1R. Which has better expectancy?",
        "options": ["System A — higher win rate is always more profitable", "System B — the math: (0.4 × 3R) - (0.6 × 1R) = 0.6R per trade vs System A's 0.2R per trade", "They're about equal in long-term profitability", "Can't tell without knowing the number of trades per month"],
        "scores": [0, 1, 0, 0],
    },
    {
        "text": "You accidentally enter 10x your normal position size due to a typo. The trade immediately goes +5 pips. You should…",
        "options": ["Let it run — you're already in profit", "Close IMMEDIATELY — this trade violates every risk parameter regardless of the unrealized P&L", "Reduce to normal size and keep the remaining position", "Set a tight stop to protect the over-leveraged position"],
        "scores": [0, 1, 0, 0],
    },
    {
        "text": "Your backtested max drawdown was 12%. In live trading, you hit 15%. The correct response is…",
        "options": ["Stop trading — the system is broken if it exceeded the backtested max", "15% vs 12% is within the range of normal variance — continue with caution and reduced size", "Increase position size to recover faster", "Re-run the backtest — maybe the original data was wrong"],
        "scores": [0, 1, 0, 0],
    },
    {
        "text": "You trade with $50,000 of your own money. You're offered a $100,000 funded account with strict drawdown rules. You should…",
        "options": ["Take the funded account — it's free money and reduces personal risk", "Consider it carefully — funded account rules can force you to trade differently (more conservatively OR more aggressively)", "Only take it if they allow the same strategy you use on your personal account", "Use both simultaneously to maximize capital deployment"],
        "scores": [0, 1, 0, 0],
    },
    {
        "text": "You just had your best trade ever (+7R). The euphoria is incredible. The risk management danger in this moment is…",
        "options": ["There's no danger — celebrate the win and move on", "Euphoria increases risk-seeking behavior — you're most likely to over-leverage your next trade after a big win", "The next trade might be a loss, which will feel more painful by contrast", "You might set unrealistic expectations for future returns"],
        "scores": [0, 1, 0, 0],
    },
    {
        "text": "You've been trading 1% risk for 6 months. You're profitable but bored by the slow growth. You think 2% would 'double your returns.' The flaw in this thinking is…",
        "options": ["It's not flawed — 2% DOES double your return per trade", "2% also doubles your drawdowns, which may exceed your psychological tolerance and cause behavioral changes", "2% is still conservative — the flaw is being too cautious", "The growth rate isn't the problem — patience is what you actually need"],
        "scores": [0, 1, 0, 0],
    },
    {
        "text": "You use 100:1 leverage but risk 1% per trade. Your friend uses 10:1 leverage but risks 3% per trade. Who is actually taking more risk?",
        "options": ["You — 100:1 leverage is far riskier", "Your friend — leverage is irrelevant; the 3% per-trade risk determines actual exposure", "Equal — both will lose money at similar rates", "Can't determine without knowing their strategies"],
        "scores": [0, 1, 0, 0],
    },
    {
        "text": "A prop firm requires a maximum 5% drawdown. You normally have 12% drawdowns. To pass the challenge, you reduce risk to 0.25% per trade. Is this sustainable?",
        "options": ["Yes — it's conservative but it will pass the challenge", "Passing a challenge with parameters that DON'T match your real trading doesn't prove you can trade the funded account", "It's the right play — get the funded account first, then adjust", "Lower risk is always better, regardless of the reason"],
        "scores": [0, 1, 0, 0],
    },
    {
        "text": "Your 'risk per trade' includes which of the following?",
        "options": ["Just the stop loss distance × position size", "SL distance × position size + estimated slippage + spread cost + swap/rollover if holding overnight", "Whatever your broker says the margin requirement is", "The distance from entry to the worst possible gap scenario"],
        "scores": [0, 1, 0, 0],
    },
    {
        "text": "You have 5 open positions each at 1% risk. A new A+ setup appears requiring 1% risk. Total open risk would be 6%. Your max open risk rule is 5%. You…",
        "options": ["Take it — it's an A+ setup and 6% isn't much more than 5%", "Skip it or close one of the other positions to make room within your 5% rule", "Take it at 0.5% risk to keep total at 5.5%", "The A+ quality justifies exceeding the limit by 1%"],
        "scores": [0, 1, 0, 0],
    },
    {
        "text": "You notice you always hold losing trades longer than winning trades. This is called…",
        "options": ["Patience — giving losers room to recover", "Disposition effect — the psychological tendency to cut winners fast and hold losers too long", "Smart management — losers need more time to play out", "Normal — everyone hopes their losers will recover"],
        "scores": [0, 1, 0, 0],
    },
    {
        "text": "A trader says: 'I never use stop losses because they always get hunted.' The counterargument is…",
        "options": ["He's right — stops get hunted, so mental stops are better", "Without stops, a single adverse event (flash crash, news bomb) can wipe out months of profits", "He probably trades very small position sizes to compensate", "Professional traders don't use stops either — it's a retail myth"],
        "scores": [0, 1, 0, 0],
    },
    {
        "text": "Your system produces 10 trades per month. 6 winners at +2R, 4 losers at -1R. Monthly expectancy is +8R. You consider filtering to take only the 'best' 5 trades, hoping to get 5 winners. What's the likely outcome?",
        "options": ["Higher returns per trade since you're selecting only the best", "Lower total return — you can't reliably identify the winners in advance, so you'll cut profitable trades AND losers", "Same returns with less risk", "Depends on how good your filtering criteria is"],
        "scores": [0, 1, 0, 0],
    },
    {
        "text": "You're in a trade that's at -0.5R and approaching your stop. You feel the urge to widen the stop. The key question to ask yourself is…",
        "options": ["'Does the wider stop level have technical justification?'", "'Am I widening because of analysis or because I can't accept the loss?'", "'How much more can I afford to lose?'", "'Has the market structure changed since I entered?'"],
        "scores": [0, 1, 0, 0],
    },
    {
        "text": "Your annual return is +25% with a maximum drawdown of 8%. Your friend's return is +45% with a maximum drawdown of 35%. Risk-adjusted, who is the better trader?",
        "options": ["Your friend — higher absolute return is all that matters", "You — risk-adjusted returns (return/drawdown ratio) show you at 3.1 vs his 1.3", "Can't tell without more years of data", "Your friend — if he can stomach 35% drawdowns, more power to him"],
        "scores": [0, 1, 0, 0],
    },
    {
        "text": "You're offered 2 trading options: (A) guaranteed 1% per month, or (B) average 3% per month with occasional -10% months. Most retail traders choose B. Why is this psychologically revealing?",
        "options": ["B is smarter — 3% average beats 1% guaranteed over time", "Humans overweight the average and underweight the maximum drawdown, which is where accounts die", "B is the right choice for anyone with a long time horizon", "A is too conservative for anyone serious about trading"],
        "scores": [0, 1, 0, 0],
    },
    {
        "text": "You're scaling into a winning trade (adding to the position). The risk management principle most people violate when scaling in is…",
        "options": ["Adding too much too quickly", "Not adjusting the stop loss to ensure the TOTAL position risk never exceeds their per-trade maximum", "Adding at poor prices", "Not having a plan for how many additions to make"],
        "scores": [0, 1, 0, 0],
    },
    {
        "text": "Your drawdown reaches 20% — the worst in your career. You've never experienced this before. The risk management response should be…",
        "options": ["Stop trading entirely until you can identify what's going wrong", "Reduce risk to 0.5% per trade, continue with A+ setups only, and set a 25% hard stop for account reevaluation", "Keep trading normally — drawdowns are part of the game", "Add more funds to reduce the percentage drawdown"],
        "scores": [0, 1, 0, 0],
    },
    {
        "text": "You risk 1% per trade. After 20 consecutive wins, your account has grown 20%. You notice you 'feel' like you can afford to lose more now. This feeling…",
        "options": ["Is correct — you have a bigger buffer now", "Is the 'house money' effect — those gains are YOURS, not the market's money, and should be protected equally", "Justifies a small risk increase to 1.5%", "Is natural after a win streak — just maintain your 1% rule"],
        "scores": [0, 1, 0, 0],
    },
    {
        "text": "You're holding a trade overnight and can't sleep because you're worried about a gap against you. This sleeplessness indicates…",
        "options": ["Normal trader anxiety — everyone worries about overnight risk", "Your position is too large for your psychology — reduce size until overnight holds don't affect your sleep", "You should set a guaranteed stop to ease the anxiety", "You shouldn't hold trades overnight if it affects your health"],
        "scores": [0, 1, 0, 0],
    },
    {
        "text": "The Kelly Criterion suggests you should risk 10% on your edge. Most professional traders risk 1/4 to 1/5 of Kelly. Why?",
        "options": ["They're being too conservative", "Full Kelly assumes perfect knowledge of your edge, which you never have. Under-betting protects against estimation errors", "Because most pros trade other people's money and can't risk 10%", "Full Kelly produces too much volatility for psychologically comfortable trading"],
        "scores": [0, 1, 0, 0],
    },
    {
        "text": "You trade a strategy with 90% win rate but 1:9 R:R (you make $1 when you win, lose $9 when you lose). Is this trader profitable?",
        "options": ["Yes — 90% win rate is incredible", "Breakeven at best — (0.9 × $1) - (0.1 × $9) = $0. One unexpected loss streak destroys the account", "Yes — the rare losses are manageable at 10%", "Can't tell without knowing position size"],
        "scores": [0, 1, 0, 0],
    },
    {
        "text": "You enter a trade and your broker's margin call level is 50%. Your account is at 60% margin utilization. What should concern you?",
        "options": ["Nothing — you still have 10% buffer", "You are ONE adverse move from a margin call, which means your leverage is dangerously high", "Only worry if you hit 55%", "Margin utilization doesn't matter if your stop loss is in place"],
        "scores": [0, 1, 0, 0],
    },
    {
        "text": "You just survived a major black swan event (e.g., SNB unpegging CHF). Your account lost 30% despite proper stop losses. The lesson is…",
        "options": ["Stop losses don't work — they can't protect against gaps", "Risk management must account for TAIL EVENTS, not just normal market conditions — gaps through stops are possible", "Switch to a broker with guaranteed stops", "Black swans are too rare to plan for"],
        "scores": [0, 1, 0, 0],
    },
    {
        "text": "Your win rate is 55%. You risk 2% per trade. After 50 trades, you should statistically expect a maximum losing streak of approximately…",
        "options": ["2-3 trades — with 55% win rate, long streaks are unlikely", "5-8 trades — even at 55%, runs of 6+ losses are statistically normal over 50 trades", "1-2 trades — 55% win rate means losses are rare", "10+ trades is common"],
        "scores": [0, 1, 0, 0],
    },
    {
        "text": "You trade forex and crypto. Crypto has 5x the volatility. You use the same 1% risk on both. Is this appropriate?",
        "options": ["Yes — 1% risk is 1% risk regardless of the instrument", "It depends — your POSITION SIZE should be adjusted based on volatility so that 1% risk produces similar dollar exposure", "No — risk more on crypto since the opportunity is bigger", "No — risk less on crypto since it's more volatile"],
        "scores": [0, 0, 0, 1],
    },
    {
        "text": "Your monthly return history: +3%, +2%, +4%, +1%, -8%, +2%, +3%. What does the -8% month tell you about your risk management?",
        "options": ["One bad month out of 7 is acceptable", "The -8% is 2x the best month — this asymmetry suggests a risk management failure, not just bad luck", "It's within normal variance for an active trader", "Focus on the overall positive average, not the outlier"],
        "scores": [0, 1, 0, 0],
    },
    {
        "text": "You have a $100K account. You tell yourself '1% risk is only $1,000 — that's nothing.' But when a trade is at -$800, you feel sick. This disconnect means…",
        "options": ["You need to toughen up — $1,000 losses are part of trading a $100K account", "You're risking too much for your emotional capacity — reduce to the amount where losses DON'T make you sick", "You'll get used to the amounts over time", "The psychological impact of losses is always worse than the logical assessment"],
        "scores": [0, 1, 0, 0],
    },
    {
        "text": "Your system says to exit at -1R (stop loss). But you add a 'hard' rule: 'if account drawdown exceeds 6%, pause ALL trading.' Why is this second rule necessary?",
        "options": ["It's not — per-trade risk is sufficient", "Per-trade risk controls individual losses but doesn't protect against extended losing streaks or correlated failures", "It limits trading opportunities unnecessarily", "It's only necessary if you're revenge trading during drawdowns"],
        "scores": [0, 1, 0, 0],
    },
    {
        "text": "You trade with a friend's $20,000. You have a different emotional reaction to losses on his money vs. your own. Specifically, you find yourself…",
        "options": ["Taking less risk — the pressure of other people's money makes you conservative", "It doesn't matter whose money it is — you should trade the same way", "Taking more risk — it's not your money so losses feel less personal", "Being more cautious is the right response when managing others' capital"],
        "scores": [0, 0, 1, 0],
    },
    {
        "text": "You've been taught to 'let winners run.' Your trade is at +5R but your system says TP at +3R. The trade looks like it could go to +10R. You…",
        "options": ["Hold — let it run to +10R, the trend is strong", "Close at +3R per your system — 'let winners run' doesn't mean 'abandon your system mid-trade'", "Close half at +3R and let the rest run", "Move your SL to +4R and see what happens"],
        "scores": [0, 1, 0, 0],
    },
    {
        "text": "Your drawdown tolerance questionnaire says you can handle 15%. But when it actually happened, you panicked at 10%. This gap between hypothetical and real tolerance means…",
        "options": ["You underestimated yourself on the questionnaire", "You should size your risk based on your ACTUAL tolerance (10%), not your hypothetical one (15%)", "You need to build mental toughness to handle 15%", "Questionnaires are useless — real drawdowns feel completely different"],
        "scores": [0, 1, 0, 0],
    },
    {
        "text": "You're about to go on vacation for 2 weeks. You have 3 open trades. Best risk management decision?",
        "options": ["Close all trades — peace of mind during vacation is worth more than potential gains", "Set SL at breakeven on profitable trades, close losing trades, and enjoy vacation", "Leave them as-is with original SL/TP — the system works without you staring at it", "Give a trusted friend access to manage the trades"],
        "scores": [0, 1, 0, 0],
    },
    {
        "text": "You hear: 'risk what you can afford to lose.' A more accurate version of this advice is…",
        "options": ["Risk what won't change your behavior when lost", "Risk what feels comfortable", "Risk what you'd be willing to set on fire and walk away from", "Actually, risk what you CAN'T afford to lose — that's what creates edge-generating focus"],
        "scores": [1, 0, 0, 0],
    },
    {
        "text": "You have a winning trade at +2R and the market closes for the weekend. There's geopolitical uncertainty. You decide to hold over the weekend. On Sunday night, you're anxious. What went wrong?",
        "options": ["Nothing — weekend anxiety is normal", "You failed to account for weekend gap risk in your original risk assessment. If it causes anxiety, you're over-exposed", "Geopolitical events are unpredictable — anxiety is rational", "Close the trade next time — never hold over weekends"],
        "scores": [0, 1, 0, 0],
    },
    {
        "text": "Martingale strategy (doubling position after every loss) guarantees a profit eventually. Why is it still considered dangerous?",
        "options": ["It doesn't work — the math is wrong", "Because 'eventually' can exceed your account balance — it requires infinite capital and a losing streak WILL happen that bankrupts a finite account", "It's not dangerous if you start with small positions", "Brokers prevent it from working by adding spread"],
        "scores": [0, 1, 0, 0],
    },
    {
        "text": "Your trailing stop is hit and you exit with +1R profit. Price then continues another 100 pips in your direction. You feel like the trailing stop 'robbed' you. The correct perspective is…",
        "options": ["Trailing stops ARE problematic — they limit upside", "The trailing stop did its job: it locked in profit while giving the trade room. The 100-pip move AFTER is irrelevant to your trade", "You should widen your trailing stop", "Don't use trailing stops — use fixed TP targets instead"],
        "scores": [0, 1, 0, 0],
    },
    {
        "text": "You trade with a 2:1 R:R and 50% win rate. This gives you a positive expectancy. Your friend says 'you'd be better off with a 5:1 R:R.' Is he right?",
        "options": ["Yes — higher R:R is always better", "Not necessarily — going to 5:1 R:R will likely reduce your win rate significantly, potentially to below breakeven", "Yes — the extra profit per winner more than compensates for lower win rate", "R:R doesn't matter — only win rate determines profitability"],
        "scores": [0, 1, 0, 0],
    },
    {
        "text": "You have $50,000 in your trading account AND $50,000 in savings. You're considering moving $25,000 from savings to your trading account to 'trade bigger.' This decision should be based on…",
        "options": ["How confident you are in your edge", "Whether the additional capital is truly RISK capital you can lose without affecting your life — not your confidence level", "Your annual return percentage — if it's above 20%, adding capital makes sense", "Your trading track record over the past 2+ years"],
        "scores": [0, 1, 0, 0],
    },
    {
        "text": "You scalped 20 trades today. Each was 0.5% risk. But they overlapped in time — sometimes 4-5 were open at once. Your max exposure at peak was actually…",
        "options": ["Still 0.5% per trade — each had its own stop", "2-2.5% — correlated simultaneous positions stack their risk", "Unknowable without checking each trade's timing", "0.5% — individual risk is all that matters"],
        "scores": [0, 1, 0, 0],
    },
    {
        "text": "Your equity curve shows: smooth upward trend for 6 months, then a sharp 15% drop in 2 weeks. What does this pattern typically indicate?",
        "options": ["Normal drawdown after a good streak", "A strategy that works well in one market regime but fails in another — regime sensitivity is a hidden risk", "Bad luck that corrected your overperformance", "You got complacent after 6 good months"],
        "scores": [0, 1, 0, 0],
    },
    {
        "text": "Your broker offers 500:1 leverage. Your friend says 'only use 30:1 max.' He's right because…",
        "options": ["High leverage causes bigger losses per pip", "High leverage doesn't change per-trade risk if you size correctly, BUT it makes catastrophic errors (wrong size, missing SL) account-ending", "30:1 is the regulated maximum in most countries", "Higher leverage costs more in swap fees"],
        "scores": [0, 1, 0, 0],
    },
    {
        "text": "You're considering hedging a losing trade instead of cutting it. Opening an opposite position on the same pair. This 'hedge' actually…",
        "options": ["Protects you from further losses while you decide what to do", "Is equivalent to closing the original trade PLUS paying extra spread — you're not hedging, you're paying to feel better", "Is a legitimate risk management tool used by institutions", "Gives you time to wait for the original trade to come back"],
        "scores": [0, 1, 0, 0],
    },
    {
        "text": "A prop firm funded trader risks 0.25% per trade to avoid hitting the drawdown limit. His returns are +2% per month. His friends mock the 'small returns.' His response should be…",
        "options": ["He should take more risk to generate better returns", "2% per month on a funded account is free money with near-zero risk of personal loss — the mockers don't understand capital structure", "Trade your own money for bigger returns", "The returns are too small to be worth the effort"],
        "scores": [0, 1, 0, 0],
    },
    {
        "text": "You read that Warren Buffett's #1 rule is 'never lose money' and #2 is 'never forget rule #1.' In trading, this translates to…",
        "options": ["Never take losing trades", "Capital preservation is paramount — a 50% loss requires a 100% gain to recover, making large losses mathematically devastating", "Only take setups with extremely high probability", "Use guaranteed stop losses on every trade"],
        "scores": [0, 1, 0, 0],
    },
    {
        "text": "You want to test if increasing risk from 1% to 2% improves your overall returns. The MINIMUM sample size for a statistically valid comparison is…",
        "options": ["20 trades — enough to see a pattern", "30 trades — the standard sample size", "200+ trades at each risk level with all other variables held constant", "50 trades — gives a decent distribution"],
        "scores": [0, 0, 1, 0],
    },
    {
        "text": "You are highly profitable but take huge individual risks. Your best month was +40%, worst was -25%. A risk management coach would say…",
        "options": ["If it works, don't fix it", "You're one bad month away from psychological damage that will change your trading forever. Smooth out the equity curve before the inevitable bad streak hits", "High variance is fine if the average is positive", "Your personality is suited for high-risk trading — embrace it"],
        "scores": [0, 1, 0, 0],
    },
    {
        "text": "You're experiencing 'position sizing anxiety' — you hesitate to enter trades even though the risk is only 0.5%. The solution is NOT to push through the anxiety but to…",
        "options": ["Reduce to 0.25% until the anxiety disappears, then slowly titrate up", "Trade demo until you're comfortable", "Recognize the anxiety as normal and enter anyway", "See a therapist before trading again"],
        "scores": [1, 0, 0, 0],
    },
    {
        "text": "The relationship between risk and reward in trading is best described as…",
        "options": ["More risk always equals more reward", "Higher risk increases the VARIANCE of outcomes, not the expected value — you can (and people do) lose more by risking more", "Risk and reward are perfectly correlated", "Higher risk is required for higher returns — no way around it"],
        "scores": [0, 1, 0, 0],
    },
    {
        "text": "You risk 1% per trade. Your 10-trade baseline is: W, W, L, W, L, L, W, W, W, L. Net +4R. If you increase risk to 3%, net APPEARS to be +12R. But psychologically…",
        "options": ["12R is clearly better — the math is obvious", "At 3% risk, the 3 consecutive L, L, W, L (-9% over 4 trades) might cause you to abandon the system before reaching the recovery", "You should definitely increase to 3%", "Start at 2% as a middle ground"],
        "scores": [0, 1, 0, 0],
    },
    {
        "text": "The biggest risk management mistake in retail forex trading is…",
        "options": ["Using too much leverage", "Not having a stop loss", "Confusing position size with risk — using large positions without understanding the dollar amount at risk per trade", "Trading correlated pairs"],
        "scores": [0, 0, 1, 0],
    },
    {
        "text": "Your risk management system is only as good as…",
        "options": ["Your backtesting results", "Your ability to follow it during your WORST moments — the system is tested by drawdowns, not profits", "Your broker's execution speed", "The accuracy of your analysis"],
        "scores": [0, 1, 0, 0],
    },
]
