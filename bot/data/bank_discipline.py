"""
Question Bank — Part 3: Discipline, Rules & Process (100 questions)
"""

QUESTIONS_DISCIPLINE = [
    {
        "text": "You have a rule: only trade during London and NY overlap (8am-12pm EST). A perfect setup forms at 1:30pm. You…",
        "options": ["Take it — the setup quality overrides the time rule", "Skip it — your time window exists because YOUR best performance data backs it", "Set a limit order in case it retraces during tomorrow's session", "Take it at half size since you're only slightly outside your window"],
        "scores": [0, 1, 0, 0],
    },
    {
        "text": "Your written trading plan says 'max 3 trades per day.' It's 10am and you've already had 3 trades (2 wins, 1 loss). A 4th setup appears. The disciplined response?",
        "options": ["Take it — you're net positive and in the zone", "Stop. 3 means 3. Changing the rule mid-session is how rules become meaningless", "This is a good time to test if 4 trades works better than 3", "Log it as a 'paper trade' and see how it would have played out"],
        "scores": [0, 1, 0, 0],
    },
    {
        "text": "You've been following your trading plan perfectly for 2 months. Your results are mediocre. You're tempted to 'freestyle' for a week. This temptation is…",
        "options": ["Worth exploring — 2 months of mediocre results might mean the plan needs changing", "A classic discipline test — 2 months is not statistically significant for most strategies", "Smart — sometimes rigid rules hold you back from better performance", "A sign the plan needs refinement, not abandonment"],
        "scores": [0, 1, 0, 0],
    },
    {
        "text": "A setup meets 4 out of your 5 entry criteria. The one missing criterion is 'trend alignment on the daily chart.' You…",
        "options": ["Enter — 4 out of 5 is 80%, which is good enough", "Skip — your criteria exist as a COMPLETE checklist, not a majority-rules vote", "Enter at reduced size since one criterion is missing", "Check if the missing criterion has historically been the least important one"],
        "scores": [0, 1, 0, 0],
    },
    {
        "text": "You trade with a checklist. Your friend trades 'by feel' and makes more money this month. You start doubting your checklist approach. You should remind yourself…",
        "options": ["One month means nothing — ask him again in 2 years", "Feel-based trading works until it doesn't — checklists provide consistency across hundreds of trades", "Maybe you should add some discretionary elements to your checklist", "His strategy might genuinely be better — evaluate it objectively"],
        "scores": [0, 1, 0, 0],
    },
    {
        "text": "You created a rule last month: '1% risk per trade, no exceptions.' This month you feel confident and want to go to 2%. What should govern this decision?",
        "options": ["If you feel confident, that's a valid reason to increase risk", "Only your backtest/forward test data should change risk parameters — never a feeling", "Gradually increase to 1.5% first and see how it feels", "If you've had 3+ months of consistent profitability, a risk increase is warranted"],
        "scores": [0, 1, 0, 0],
    },
    {
        "text": "Your plan says 'no trading on NFP days.' NFP is Friday. On Thursday, you see a perfect setup that would require holding through NFP. You…",
        "options": ["Enter with the intention to close before NFP if needed", "Pass on the setup — your rule accounts for pre-NFP positioning risk too", "Enter but set a tight stop to protect against NFP volatility", "Enter at half size — a compromise between opportunity and rule"],
        "scores": [0, 1, 0, 0],
    },
    {
        "text": "You broke your own trading rules 3 times this week. Each time, you had a 'good reason.' If you're honest with yourself…",
        "options": ["The reasons were genuinely valid — rules need flexibility", "If you break a rule 3 times in a week, you don't have a rule — you have a suggestion", "Rules should be flexible enough to account for unusual circumstances", "Breaking rules occasionally is human — don't be too hard on yourself"],
        "scores": [0, 1, 0, 0],
    },
    {
        "text": "Your mentor gives you a complete trading system with precise rules. You keep 'tweaking' it based on gut feelings. After 3 months of tweaking, your results are worse. Why?",
        "options": ["The system wasn't right for your personality — find a better fit", "Your 'tweaks' were random noise additions to a signal-based system — you degraded the edge", "The system needs more backtesting after modifications", "Three months isn't enough to evaluate the tweaked version"],
        "scores": [0, 1, 0, 0],
    },
    {
        "text": "You realize you only follow your trading plan on 'calm' days. On volatile days, you abandon it. This pattern reveals…",
        "options": ["Your plan doesn't account for volatility — it needs a volatility filter", "Your discipline is conditional, which means it isn't discipline — it's comfort-zone trading", "Adapting to market conditions IS discipline, not a lack of it", "Volatility requires different tactics — flexible plans beat rigid ones"],
        "scores": [0, 1, 0, 0],
    },
    {
        "text": "You trade the same setup at 8:30am and at 3:30pm. The morning version wins. The afternoon version loses. Both followed your plan. Correct takeaway?",
        "options": ["Morning trading is better than afternoon — adjust your hours", "One data point per time slot means nothing — log it and look for patterns over 50+ trades", "Your plan works but needs a time-of-day filter", "The afternoon markets are more manipulated — avoid them"],
        "scores": [0, 1, 0, 0],
    },
    {
        "text": "You have a spreadsheet tracking your plan compliance. This month: 85% compliance, +4% return. Last month: 95% compliance, +2% return. What conclusion should you draw?",
        "options": ["Lower compliance = higher returns, so be more flexible", "NO conclusion — one month of data per category is noise, keep tracking for 6+ months", "The 4% month benefited from luck, not from breaking rules", "Maybe your rules are too strict and loosening them helps"],
        "scores": [0, 1, 0, 0],
    },
    {
        "text": "A professional athlete has pre-game rituals they NEVER skip. Your pre-trading routine takes 15 minutes but you often skip it when you 'feel ready.' The skip is…",
        "options": ["Fine — you know when you need the routine and when you don't", "A discipline problem — the routine's value comes from its consistency, not from how you feel", "Acceptable on days when you've already done thorough analysis", "Something to address — maybe shorten the routine to 5 minutes so you never skip it"],
        "scores": [0, 1, 0, 0],
    },
    {
        "text": "Your system says 'enter on the break of the previous candle high.' You see the breakout happening in real-time and enter 2 pips early because 'it's clearly going to break.' This is…",
        "options": ["Smart — getting a better entry price is always good", "Undisciplined — 'it's clearly going to break' is a prediction, and your rule says BREAK, not ALMOST break", "Fine as long as the difference is only 2-3 pips", "Aggressive but acceptable for experienced traders"],
        "scores": [0, 1, 0, 0],
    },
    {
        "text": "You've programmed your entries as alerts. The alert fires, you enter. No thinking required. After 4 months of this, you feel like a robot. This feeling is…",
        "options": ["Boring — maybe add some discretionary elements for engagement", "Exactly the point — mechanical execution removes emotion and IS the edge", "A sign you need a more intellectually stimulating strategy", "Dangerous — you should understand WHY each trade works, not just execute blindly"],
        "scores": [0, 1, 0, 0],
    },
    {
        "text": "Your trailing stop rule is: 'move SL to breakeven after 1:1 R.' A trade is at +0.9R and you want to move to breakeven 'just in case.' This is…",
        "options": ["Close enough — 0.9R is practically 1R", "A rule violation. 1R means 1R. You're letting fear make the decision early", "Smart risk management — protecting a trade in profit is never wrong", "Only matters if you do it consistently — one time won't hurt"],
        "scores": [0, 1, 0, 0],
    },
    {
        "text": "You trade both USD/JPY and GBP/USD. Your plan says 'max 2% total exposure.' Both pairs have setups simultaneously. Each would be 1.5% risk. Total would be 3%. You…",
        "options": ["Take both — they're on different pairs so the risk is diversified", "Choose the stronger setup and skip the other — 3% exceeds your 2% rule", "Take both at 1% each to stay within the 2% total", "Take both — correlation between these pairs is low enough"],
        "scores": [0, 0, 1, 0],
    },
    {
        "text": "Your buddy offers to share his screen so you can trade together in real-time. This sounds fun but the risk is…",
        "options": ["Social pressure will make you enter trades you wouldn't take alone", "No risk — accountability partners improve consistency", "You might copy his trades instead of following your own system", "You'll trade more frequently to 'keep up' with his pace"],
        "scores": [1, 0, 0, 0],
    },
    {
        "text": "You discover that your win rate drops from 58% to 41% when you trade more than 2 pairs simultaneously. This data means…",
        "options": ["You should specialize in fewer pairs for better performance", "Multi-pair trading splits your attention, reducing analysis quality — enforce a 2-pair maximum", "Correlation between pairs is hurting you", "Your system works better on some pairs than others"],
        "scores": [0, 1, 0, 0],
    },
    {
        "text": "Your trading plan doesn't have a rule for 'what to do when you feel emotionally compromised.' This is…",
        "options": ["Fine — plans should focus on analysis and entries, not feelings", "A critical gap — the most important rule a plan can have is 'don't trade when emotional'", "Not necessary if you have good risk management", "Something to add but not a high priority"],
        "scores": [0, 1, 0, 0],
    },
    {
        "text": "You're backtesting a new strategy, and you 'cheat' by peeking at future candles during the test. Your backtest results will be…",
        "options": ["Slightly optimistic but still directionally accurate", "Completely worthless — forward-looking bias invalidates the entire test", "Affected but not significantly — you can adjust for the bias", "Fine as long as you account for the peeking in your expectancy calculations"],
        "scores": [0, 1, 0, 0],
    },
    {
        "text": "Your system requires a specific candlestick pattern at a key level. You see the level but the pattern is 'close enough.' Your internal voice says 'take it.' You should…",
        "options": ["Trust your instinct — pattern recognition improves with experience", "Screenshot the 'close enough' setup, compare it to textbook examples, and decide factually", "Take it at reduced risk — the level is there even if the pattern isn't perfect", "Log it as a potential setup and wait for the next one that meets ALL criteria"],
        "scores": [0, 0, 0, 1],
    },
    {
        "text": "You always move your take-profit target when the trade is close to hitting it. You think 'it could go further.' This habit is…",
        "options": ["Smart — many trades DO go further than the initial target", "A discipline issue — you're constantly changing the rules DURING the trade based on greed", "Fine if you have a trailing stop protecting the profit", "Evidence that your TP targets are set too conservatively"],
        "scores": [0, 1, 0, 0],
    },
    {
        "text": "You review your last 100 trades. The ones where you followed ALL rules made +12%. The ones where you broke at least one rule made -8%. Despite this clear data, you STILL break rules. Why?",
        "options": ["Rules are hard to follow when real money is on the line — it's human nature", "Your emotional brain (amygdala) is faster than your rational brain (prefrontal cortex) — you need systems, not willpower", "The data sample might be coincidental — 100 trades isn't enough", "You need stronger consequences for breaking rules"],
        "scores": [0, 1, 0, 0],
    },
    {
        "text": "You write a trading plan but never look at it again. You 'know what's in it.' The problem is…",
        "options": ["No problem — internalizing the plan means you don't need the document", "Unreviewed plans drift in memory — you'll unconsciously modify rules to fit what you WANT to do", "As long as the key rules are memorized, daily review is unnecessary", "Reading it once a month is sufficient to stay aligned"],
        "scores": [0, 1, 0, 0],
    },
    {
        "text": "A new indicator shows a conflicting signal to your current setup. Your plan doesn't include this indicator. You should…",
        "options": ["Use it as additional confluence — more information is better", "Ignore it — trading signals not in your plan is the same as not having a plan", "Note it in your journal and backtest whether adding it improves your system", "Use it to filter out potentially weak trades"],
        "scores": [0, 0, 1, 0],
    },
    {
        "text": "Your plan says risk 1% per trade. Your account has grown 40% this year. You're still risking the same dollar amount instead of updating to 1% of the new balance. This means…",
        "options": ["You're being conservative — nothing wrong with that", "You're under-risking relative to your plan — update the dollar amount to reflect the new 1%", "Keep the same dollar amount to protect your gains", "Only increase risk when the account crosses a round number like doubling"],
        "scores": [0, 1, 0, 0],
    },
    {
        "text": "You keep a physical trading journal but often forget to write in it after losing trades. You always write after winners. This selective journaling is…",
        "options": ["Normal — it's harder to journal when you're upset", "Hugely problematic — you're creating a biased dataset and avoiding the analysis that matters most", "Not ideal but the winners data is still valuable", "A sign you should switch to a digital journal with automatic trade logging"],
        "scores": [0, 1, 0, 0],
    },
    {
        "text": "Your trading rules are extremely detailed — 47 conditions across 3 pages. You find it impossible to check all 47 before each trade. The solution is…",
        "options": ["Memorize the most important 10 and focus on those", "Simplify — if you can't process the rules in real-time, the system is too complex to execute consistently", "Use a digital checklist app to speed up the process", "Keep all 47 but organize them into tiers: must-have, nice-to-have, optional"],
        "scores": [0, 1, 0, 0],
    },
    {
        "text": "You set a rule to stop trading for the day after a 1.5% loss. You hit -1.5% and stopped. Then you watched a setup play out for +4R without you. The pain of missing it makes you want to remove the rule. You should…",
        "options": ["Remove the rule — it's causing you to miss profits", "Keep the rule — the rule exists because of ALL the times continuing at -1.5% led to -4%. One missed winner doesn't invalidate the rule", "Modify it: stop after -1.5% UNLESS an A+ setup appears", "Tighten it to -1% so the missed opportunities hurt less"],
        "scores": [0, 1, 0, 0],
    },
    {
        "text": "A professional trader you respect says he has only 3 rules. You have 15 rules. Does this mean your approach is wrong?",
        "options": ["Yes — simplicity is key in trading", "Not necessarily — the number of rules should match YOUR psychology and system complexity", "It means you should simplify over time as you internalize the rules", "3 rules means he's relying on discretion for the rest, which is risky"],
        "scores": [0, 1, 0, 0],
    },
    {
        "text": "You execute your plan perfectly for 3 weeks and the results are positive. Week 4, you freelance a few trades and they also win. You start thinking 'I don't need the plan.' This thought pattern is…",
        "options": ["Based on evidence — you win with and without the plan", "Extremely dangerous — recency bias is convincing you to abandon what works based on a few lucky discretionary wins", "Worth testing — track plan vs. freestyle performance over 3 months", "Natural evolution from rule-based to discretionary trading"],
        "scores": [0, 1, 0, 0],
    },
    {
        "text": "You normally trade with a 1:2 Risk/Reward. A setup appears with 1:1.5 R:R. Your plan says minimum 1:2. You…",
        "options": ["Take it — 1:1.5 is close enough and the setup is strong", "Skip it — 1:2 minimum is a rule, and 1:1.5 doesn't meet it", "Take it at smaller size to account for the lower R:R", "Check if the TP can be extended to reach 1:2"],
        "scores": [0, 1, 0, 0],
    },
    {
        "text": "After every trade, you score your execution from 1-10 regardless of the outcome. Why is this practice powerful?",
        "options": ["It separates process quality from outcome quality, which is the foundation of long-term profitability", "It makes you feel better about losses", "It helps identify your best setups", "It creates data for optimization"],
        "scores": [1, 0, 0, 0],
    },
    {
        "text": "You read a book that says 'the best traders break their own rules intelligently.' You interpret this as…",
        "options": ["Permission to be flexible when you feel confident", "A dangerous idea for anyone without 10,000+ hours of screen time — rules protect you until you've earned true intuition", "The natural progression: rules → mastery → transcending rules", "Only applicable to prop desk traders with years of mentorship"],
        "scores": [0, 1, 0, 0],
    },
    {
        "text": "Your accountability partner asks to see your full trade log every Friday. You start feeling anxious about showing losers. This anxiety is…",
        "options": ["Normal — no one likes showing losses", "Revealing — it means you're associating your self-worth with your P&L, not your process", "A sign the accountability setup is too intense for you", "Motivational — it will make you trade more carefully to avoid showing losses"],
        "scores": [0, 1, 0, 0],
    },
    {
        "text": "You created a pre-trade checklist with 8 items. You've been skipping items 7 and 8 because they 'slow you down.' What should you do?",
        "options": ["Remove items 7 and 8 — if they're slowing you down, they're not worth it", "Either follow all 8 or formally remove them after backtesting confirms they don't add value — but NEVER silently skip", "Keep items 1-6 as mandatory and 7-8 as optional", "Rearrange the order so 7 and 8 come earlier when your attention is fresher"],
        "scores": [0, 1, 0, 0],
    },
    {
        "text": "You trade on a platform that lets you set 'guardrails' — automatic daily loss limits, max position sizes, etc. A serious trader should…",
        "options": ["Use all available guardrails — removing human override ability is smart, not weak", "Trade without guardrails — self-discipline is the only sustainable approach", "Use them during drawdowns only", "Only use the loss limit guardrail, handle the rest manually"],
        "scores": [1, 0, 0, 0],
    },
    {
        "text": "Your mentor tells you to trade the EXACT same size on every trade for 6 months. No variation, no 'conviction sizing.' This feels limiting. Why would a mentor suggest this?",
        "options": ["To build discipline — variable sizing is for advanced traders", "Because conviction sizing lets emotion creep in disguised as 'higher confidence'", "To simplify decision-making so you can focus on execution", "To create clean data — variable sizing makes it impossible to evaluate the system accurately"],
        "scores": [0, 0, 0, 1],
    },
    {
        "text": "You maintain two journals: one for technical analysis of trades, one for emotional state during trades. Which is more valuable for improvement?",
        "options": ["Technical — that's where the actual trading edge is", "Emotional — understanding your psychological patterns prevents the behavioral errors that destroy edges", "They're equally important — one without the other is incomplete", "Technical during profitable periods, emotional during drawdowns"],
        "scores": [0, 0, 1, 0],
    },
    {
        "text": "You recently started following your trading plan on demo perfectly, but still struggle on live. The gap between demo discipline and live discipline is caused by…",
        "options": ["The lack of real money at stake in demo — fear and greed only activate with real capital", "The difference in position sizing — demo accounts are usually larger", "Demo platforms execute differently than live platforms", "You take demo less seriously, paradoxically making you more relaxed and disciplined"],
        "scores": [1, 0, 0, 0],
    },
    {
        "text": "Your plan says 'no trading during FOMC minutes release.' FOMC is at 2pm. You have an open trade from before the announcement. At 1:55pm you should…",
        "options": ["Close the trade to honor the spirit of the rule — no exposure during FOMC", "Hold it — the rule says no NEW trades during FOMC, not no existing exposure", "Tighten your stop to protect profits before the announcement", "It depends on whether the trade is in profit or loss"],
        "scores": [0, 0, 1, 0],
    },
    {
        "text": "You keep changing your trading plan every 2-3 weeks. You tell yourself you're 'optimizing.' The reality is…",
        "options": ["You ARE optimizing — plans should evolve with market conditions", "You haven't given any single version enough time to produce statistically valid results", "Frequent changes show you're learning and adapting quickly", "Some changes are valid — the issue is changing too many things at once"],
        "scores": [0, 1, 0, 0],
    },
    {
        "text": "If you had to choose between a trader with a mediocre strategy and perfect discipline vs. a trader with a great strategy and poor discipline, you'd bet on…",
        "options": ["Great strategy, poor discipline — edge matters more than execution", "Mediocre strategy, perfect discipline — the disciplined trader will survive long enough to improve the strategy", "Neither — both need fixing", "The great strategy trader — a strong edge can overcome some discipline issues"],
        "scores": [0, 1, 0, 0],
    },
    {
        "text": "You have a rule: 'review every trade within 24 hours.' You skipped the review of your last 5 trades because they were all winners. This is a problem because…",
        "options": ["Winners don't need reviewing — you already know what you did right", "Reviewing only losses creates a biased understanding — winning trades can ALSO contain process errors that won't repeat", "It breaks the review habit, making it easier to skip future reviews", "You might miss optimization opportunities in winning trades"],
        "scores": [0, 1, 0, 0],
    },
    {
        "text": "Your physical environment for trading is: couch, laptop on your knees, TV on in the background, phone within reach. How does this affect your discipline?",
        "options": ["It doesn't — trading is mental, environment doesn't matter", "Significantly — a casual environment produces casual attention, which leads to sloppy execution", "Minimally — as long as you can see the charts clearly", "Only affects short-term scalping, not swing trading"],
        "scores": [0, 1, 0, 0],
    },
    {
        "text": "You made a rule to never add to a losing trade. Your trade is -20 pips and price is now at a STRONGER support level. Should you add?",
        "options": ["Yes — the better level justifies the add, and your original analysis is confirmed", "No — your rule says never add to losers. If you want to trade the new level, close this trade and enter a new one", "Yes, but only if you maintain the same total risk", "It depends on how far the original SL is"],
        "scores": [0, 1, 0, 0],
    },
    {
        "text": "You've been disciplined for 90 days straight. You feel a sense of mastery. Psychologically, what's about to happen?",
        "options": ["You've built the habit permanently — it gets easier from here", "Overconfidence peak — the 90-day mark is where many traders relax their rules and slip", "Nothing special — consistency compounds from here", "Plateau — discipline alone won't improve returns further"],
        "scores": [0, 1, 0, 0],
    },
    {
        "text": "You trade 2 accounts: one follows your rules perfectly, one is 'experimental' where you freestyle. After 6 months, the experimental account is up more. You conclude…",
        "options": ["Freestyle trading is your true edge — you should apply it to both accounts", "6 months is still a small sample — the experimental account likely has higher variance and will eventually underperform risk-adjusted", "The data speaks for itself — keep experimenting", "Your rules need updating based on what worked in the experimental account"],
        "scores": [0, 1, 0, 0],
    },
    {
        "text": "Your trading plan states 'SL goes below the most recent swing low.' The swing low is at a round number (1.0800) that you suspect will be hunted. You should…",
        "options": ["Place SL exactly at the swing low as per your plan", "Place SL 10-15 pips below to account for the hunt — this is intelligent adaptation within your framework", "Skip the trade because the SL is at an obvious liquidity level", "Follow the rule exactly and accept that some stops will be hunted"],
        "scores": [0, 1, 0, 0],
    },
    {
        "text": "Your trading group does a monthly 'discipline challenge' where members share their plan compliance rates publicly. Your rate is 72%. You feel embarrassed. The productive response is…",
        "options": ["Leave the group — public shaming isn't motivating", "Use the embarrassment as fuel — identify the 28% of rule breaks, find the pattern, and build defenses", "72% is probably above average — don't be too hard on yourself", "Focus on raising it to 80% next month — incremental improvement"],
        "scores": [0, 1, 0, 0],
    },
    {
        "text": "You always second-guess your entries. You hesitate for 10-20 seconds after your signal fires, sometimes missing the entry entirely. The root cause is likely…",
        "options": ["Fear of loss — your position size might be too large for your psychology", "A need for 'extra' confirmation that isn't part of your system", "Smart caution — taking 10-20 seconds to verify is prudent", "Analysis paralysis — you have too many criteria to process quickly"],
        "scores": [1, 0, 0, 0],
    },
    {
        "text": "A discipline guru says: 'If you can't follow 5 rules perfectly for 30 days, you're not ready for live trading.' You've failed this test 3 times. Is this guru right?",
        "options": ["The test is too strict — nobody follows rules perfectly 100% of the time", "Directionally correct — if you can't follow 5 simple rules on a demo, real money will make it worse", "Everyone's timeline is different — keep trying", "The test doesn't account for live market conditions that force adaptation"],
        "scores": [0, 1, 0, 0],
    },
    {
        "text": "You're about to enter a trade and realize you forgot to check the economic calendar. Your rule says 'always check the calendar before entering.' There are no major events. Was skipping the check okay?",
        "options": ["Yes — there were no events, so no harm done", "No — the fact that nothing was scheduled is irrelevant. You broke the process. Next time it might be NFP day and you'll make the same skip", "It's fine occasionally — just make sure to check next time", "Set up a calendar widget on your charts so you never need to manually check"],
        "scores": [0, 1, 0, 0],
    },
    {
        "text": "Your mentor's #1 piece of discipline advice: 'Trade your plan, plan your trades.' You find this cliché. But the reason it's repeated everywhere is…",
        "options": ["Because mentors lack original advice", "Because it compresses the ENTIRE discipline challenge into 6 words, and most traders still can't do it after years", "Because new traders need simple rules to start with", "Because it sells courses and sounds good on social media"],
        "scores": [0, 1, 0, 0],
    },
    {
        "text": "You have the discipline to enter trades correctly, but you always mess up the exit — cutting winners short or holding losers. This suggests…",
        "options": ["Your stop loss and take profit rules aren't specific enough — make them mechanical", "You have entry discipline but not management discipline — they're separate skills that need separate training", "Price action after entry is harder to judge — this is normal", "Use automated SL/TP so you can't interfere with open trades"],
        "scores": [0, 1, 0, 0],
    },
    {
        "text": "You notice you're more disciplined on red (losing) days than green (winning) days. On green days, you get sloppy. Why?",
        "options": ["Pain is a stronger motivator than pleasure — losses sharpen your focus", "Winning creates dopamine, which increases risk-seeking behavior and decreases rule adherence", "You're naturally more cautious when your capital is at risk", "Green days make you feel like you've 'earned' the right to break rules"],
        "scores": [0, 1, 0, 0],
    },
    {
        "text": "You have a 'trade or no trade' decision sheet. Every morning you score: sleep quality, stress level, analysis completion, and market clarity. If any score is below 6/10, you don't trade. This is…",
        "options": ["Overly cautious — you'll miss too many days", "An excellent holistic discipline framework that accounts for performance readiness beyond just chart analysis", "Good for newbies, unnecessary for experienced traders", "Useful but should be simplified to a 'green light / red light' overall score"],
        "scores": [0, 1, 0, 0],
    },
    {
        "text": "You're considering getting a trading tattoo that says 'Follow the plan.' Extreme? Maybe. But the underlying principle is…",
        "options": ["Ridiculous — a tattoo won't improve discipline", "The right idea, wrong method — what you need is constant VISUAL reminders of your rules in your trading environment", "Hey, whatever works — commitment devices come in all forms", "Focus on internal motivation, not external reminders"],
        "scores": [0, 1, 0, 0],
    },
    {
        "text": "Your plan says to journal before you trade. You had a bad morning and just want to get into the market. You skip the journal and enter a trade. It wins. What's the real problem?",
        "options": ["No problem — the trade worked out", "The win just made it EASIER to skip journaling next time — the habit is weakening", "One skip isn't a big deal — resume journaling tomorrow", "The problem is the bad morning, not the journal skip"],
        "scores": [0, 1, 0, 0],
    },
    {
        "text": "You find it easy to follow rules for the first 5 trades of the day but break them by trade 8-10. This pattern suggests…",
        "options": ["Your willpower depletes throughout the day — set a 5-trade maximum", "Decision fatigue is real — your prefrontal cortex can only maintain discipline for so many consecutive decisions", "Later trades are in more volatile conditions, making rules harder to apply", "You should take a break between trades 5 and 6"],
        "scores": [0, 1, 0, 0],
    },
    {
        "text": "Your system has ZERO discretionary elements — every entry, exit, SL, and TP is predetermined. The benefit of this extreme approach is…",
        "options": ["Discipline becomes automatic — there's nothing to decide, so nothing to screw up", "You can't adapt to changing conditions", "It removes the emotional highs and lows of trading", "It's only suited for algorithmic execution"],
        "scores": [1, 0, 0, 0],
    },
    {
        "text": "You have rules for entries but no rules for 'what to do when there's no setup.' You spend idle time scrolling charts looking for trades. The missing rule should be…",
        "options": ["'If no setup in 30 minutes, close the platform until the next session'", "Something that structures your non-trading time: analysis, journaling, education — not aimless chart watching", "You don't need rules for not trading — just exercise willpower", "'Close all charts and go for a walk if nothing sets up by 10am'"],
        "scores": [0, 1, 0, 0],
    },
    {
        "text": "A trader with incredible discipline but a negative expectancy system will…",
        "options": ["Eventually become profitable through discipline alone", "Consistently and predictably lose money — discipline multiplies whatever the system produces", "Break even because discipline prevents large losses", "Succeed because discipline is the most important factor"],
        "scores": [0, 1, 0, 0],
    },
    {
        "text": "Your biggest discipline breakthrough came when you…",
        "options": ["Stopped seeing rules as restrictions and started seeing them as competitive advantages", "Had a massive loss that scared you straight", "Found a strategy you believed in enough to follow", "Started using automation for all entries and exits"],
        "scores": [1, 0, 0, 0],
    },
    {
        "text": "You know a trader who writes his 3 core rules on a sticky note and sticks it to his monitor every morning. He's been doing this for 7 years. Is this still necessary after 7 years?",
        "options": ["No — after 7 years the rules should be automatic", "Yes — the daily ritual reinforces the behavior, and even experts benefit from environmental cues", "He should evolve past needing physical reminders", "It's a personal preference that doesn't affect performance"],
        "scores": [0, 1, 0, 0],
    },
    {
        "text": "You attend a live trading room where the host takes trades that violate your system's rules. He's profitable. You start questioning your own rules. You should…",
        "options": ["Adopt some of his approach — clearly it works", "Recognize that HIS rules work for HIS system and psychology — importing them to yours randomly adds noise", "Note what he does differently and test it in backtesting", "Different traders can both be profitable with very different rules — confidence in your own is key"],
        "scores": [0, 0, 0, 1],
    },
    {
        "text": "You always set your SL and TP immediately upon entry. Your friend enters first and decides SL/TP later based on 'how the trade feels.' Who is more likely to survive long-term?",
        "options": ["You — predetermined risk removes the possibility of emotional management decisions", "Your friend — adaptive management based on real-time information is superior", "It depends on the strategy — some systems require dynamic management", "Both can work if the average risk per trade is the same"],
        "scores": [1, 0, 0, 0],
    },
    {
        "text": "Your discipline score (self-rated 1-10) for this week is 4/10. You're frustrated with yourself. The SINGLE most impactful thing you can do is…",
        "options": ["Commit to doing better next week", "Identify the ONE rule you broke most often and create a specific defense mechanism for just that rule", "Lower your expectations — perfect discipline is unrealistic", "Take a break and come back refreshed"],
        "scores": [0, 1, 0, 0],
    },
    {
        "text": "You notice your discipline is perfect on demo but falls apart with real money. The most likely reason is…",
        "options": ["Demo isn't realistic enough to practice discipline", "Your position size on live is too large relative to your psychology — the money at risk triggers emotional override", "You don't take demo seriously enough", "Live markets have worse execution, making you panic"],
        "scores": [0, 1, 0, 0],
    },
    {
        "text": "You're creating a new rule after analyzing a recurring mistake. The rule should be written as…",
        "options": ["A general guideline: 'Trade carefully during high-impact news'", "A specific, binary instruction: 'No new trades within 30 min before/after red calendar events'", "A flexible framework: 'Assess news risk on a case-by-case basis'", "A conditional rule: 'During news, reduce risk by 50%'"],
        "scores": [0, 1, 0, 0],
    },
    {
        "text": "You break a rule and immediately confess to your accountability group. They say 'don't worry about it.' This response is…",
        "options": ["Supportive and exactly what you need to hear", "Well-intentioned but unhelpful — 'don't worry about it' normalizes rule-breaking instead of solving it", "The right attitude — one slip isn't worth stressing over", "What a good group should say to keep morale high"],
        "scores": [0, 1, 0, 0],
    },
    {
        "text": "You discover that writing down your entry reason BEFORE confirming the trade reduces impulsive entries by 60% (based on your stats). You should…",
        "options": ["Add it to your required process — the data supports it overwhelmingly", "Try it for another month to confirm the finding", "Use it only during drawdowns when you're most prone to impulsivity", "It's a good practice but shouldn't be mandatory"],
        "scores": [1, 0, 0, 0],
    },
    {
        "text": "Discipline in trading is most similar to discipline in…",
        "options": ["Dieting — following rules when temptation is everywhere", "Athletic training — showing up daily to do the unglamorous work", "Surgery — executing a precise protocol where deviation can be catastrophic", "Meditation — the constant practice of returning to focus when the mind wanders"],
        "scores": [0, 0, 0, 1],
    },
    {
        "text": "If someone told you: 'I have a winning strategy but I can't follow it consistently,' the FIRST thing you'd recommend is…",
        "options": ["More practice on a demo account", "Reduce position size until the emotional stakes are low enough to follow rules effortlessly", "Get an accountability partner", "Automate the strategy to remove human interference"],
        "scores": [0, 1, 0, 0],
    },
    {
        "text": "You violated your plan and got a great result. Your journal entry should read…",
        "options": ["'Good trade — my instinct was right this time'", "'Rule violation. Positive outcome is irrelevant. Process grade: F. Outcome grade: A. PROCESS is what I track.'", "'Lucky break — won't happen again'", "'Maybe my rules need updating if my instinct is this good'"],
        "scores": [0, 1, 0, 0],
    },
    {
        "text": "The NUMBER ONE reason most traders fail to maintain discipline long-term is…",
        "options": ["Lack of a clear plan", "They try to use willpower instead of building systems that make discipline automatic", "They don't want it badly enough", "The markets are too unpredictable for rigid discipline"],
        "scores": [0, 1, 0, 0],
    },
]
