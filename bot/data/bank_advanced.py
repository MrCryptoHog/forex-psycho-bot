"""
Question Bank — Advanced: Cognitive Biases, Edge Cases, Capital Psychology,
Trade Management, System Design, Market Structure Psychology, Social Dynamics,
and Professional Mindset (~165 questions)
"""

QUESTIONS_ADVANCED = [
    # ── Cognitive Biases ──────────────────────────────────────────────
    {
        "text": "You hear 'USD will crash' on 3 separate podcasts. You don't see it in your charts. But the repetition makes you lean bearish. This is an example of…",
        "options": ["Good research — multiple sources confirm the thesis", "The availability heuristic — hearing something repeatedly makes it feel more probable than it is", "Fundamental analysis overriding technicals, which is appropriate", "Consensus trading, which is usually profitable"],
        "scores": [0, 1, 0, 0],
    },
    {
        "text": "You bought EUR/USD at 1.0850. It's now 1.0810. You keep looking at your entry price instead of asking 'would I enter HERE?' This is…",
        "options": ["Normal position management — entry price determines R:R", "Anchoring bias — your entry price is psychologically hijacking your exit decision", "Smart — your entry price determines whether the trade thesis is still valid", "Best practice — always manage relative to your entry"],
        "scores": [0, 1, 0, 0],
    },
    {
        "text": "Your last 4 trades were winners. You 'feel' the next one will win too. This is…",
        "options": ["Pattern recognition — your strategy is working well", "The hot-hand fallacy — past independent outcomes don't change the probability of the next trade", "Justified confidence based on recent performance", "A sign your system is in sync with the market — ride it"],
        "scores": [0, 1, 0, 0],
    },
    {
        "text": "You avoid selling GBP/USD because you're British and it 'feels wrong' to bet against the pound. This is…",
        "options": ["Patriotic — nothing wrong with it", "Home bias — an emotional attachment to familiar assets that limits your objectivity", "Reasonable — you understand the UK economy better", "Smart — trading what you know gives an informational edge"],
        "scores": [0, 1, 0, 0],
    },
    {
        "text": "After a losing trade, you remember all the reasons it should have worked and ignore the signs it was weak. This is…",
        "options": ["Normal post-trade analysis — understanding why should have worked helps next time", "Confirmation bias in hindsight — you're selectively remembering information that supports your original decision", "Useful reflection that builds conviction for similar future setups", "Just processing the loss in a healthy way"],
        "scores": [0, 1, 0, 0],
    },
    {
        "text": "You have a 62% win rate but FEEL like you lose most trades. Your journal shows the opposite. Why the disconnect?",
        "options": ["Losses are more memorable than wins — negativity bias makes them feel more frequent", "Your winning trades are probably small and forgettable", "You might be counting differently than your journal", "Your recent trades are probably losers, skewing your perception"],
        "scores": [1, 0, 0, 0],
    },
    {
        "text": "You predicted EUR/USD would fall and it did. You feel like a genius. But you didn't actually trade it. The feeling of being 'right' makes you want to trade the next prediction more aggressively. This is…",
        "options": ["Gaining confidence from accurate analysis — use it", "Hindsight bias combined with overconfidence — predicting without trading is meaningless, and the 'genius' feeling will inflate your next position", "Natural — accurate predictions should build trading confidence", "A sign you should have traded it and should be bolder next time"],
        "scores": [0, 1, 0, 0],
    },
    {
        "text": "You've spent 200 hours developing a trading system. It's not working. You keep using it because of the time invested. This is…",
        "options": ["Dedication — 200 hours deserves a fair trial", "The sunk cost fallacy — time already spent should NEVER factor into the decision to continue", "Reasonable — 200 hours of work shouldn't be abandoned quickly", "Smart — complex systems take time to become profitable"],
        "scores": [0, 1, 0, 0],
    },
    {
        "text": "You consistently overestimate your ability to predict market direction. Your predictions are right 48% of the time but you'd guess 70%+. This is…",
        "options": ["Normal optimism that helps trading confidence", "The overconfidence bias — one of the most destructive biases in trading because it affects position sizing", "Close enough — perception lag is natural", "A sign you need a better prediction method"],
        "scores": [0, 1, 0, 0],
    },
    {
        "text": "You keep holding a losing trade because 'it HAS to come back — it's been down too long.' This reasoning is…",
        "options": ["Based on mean reversion, which is a valid strategy", "The gambler's fallacy — the market has no obligation to reverse just because it's been trending", "Reasonable for range-bound markets", "Fine if the fundamentals support a reversal"],
        "scores": [0, 1, 0, 0],
    },
    {
        "text": "You only remember your biggest wins and biggest losses but forget the 80% of trades that were average. Impact on your self-assessment?",
        "options": ["Minimal — extreme trades are the ones that matter most", "Severe — peak-end bias means your self-assessment is based on outliers, not your actual average performance", "Positive — remembering big wins builds confidence", "Not important — what matters is the bottom line P&L"],
        "scores": [0, 1, 0, 0],
    },
    {
        "text": "You read a headline: 'Top Hedge Fund Manager Predicts Dollar Crash.' You immediately want to short USD. This impulse is driven by…",
        "options": ["Credible information from an expert worth acting on", "Authority bias — a famous name doesn't make a prediction reliable, and he has a different timeline and risk tolerance than you", "Smart use of fundamental analysis", "The fact that hedge fund money moves markets, so following them makes sense"],
        "scores": [0, 1, 0, 0],
    },
    {
        "text": "You look at a chart and see a 'clear' head and shoulders pattern. Your friend looks at the same chart and sees nothing. This disagreement suggests…",
        "options": ["You're more experienced at pattern recognition", "Apophenia — the human brain finds patterns everywhere, even where they don't exist, and chart patterns are highly subjective", "Your friend needs more training", "The pattern is there but requires experience to see"],
        "scores": [0, 1, 0, 0],
    },
    {
        "text": "You've been trading for 2 years and consistently lose. But you keep thinking 'I'm SO close to figuring it out.' Realistically, this thought is…",
        "options": ["Potentially true — many traders need 3-5 years to become profitable", "Likely the optimism bias keeping you in a losing game — evaluate your ACTUAL progress data, not your feelings", "Motivational — giving up would guarantee failure", "The mindset of every eventually-successful trader"],
        "scores": [0, 1, 0, 0],
    },
    {
        "text": "A coin flip came heads 8 times in a row. You KNOW it's 50/50 but you FEEL tails is due. In trading, this same bias makes you…",
        "options": ["Counter-trend trade after an extended move, expecting a reversal", "Nothing — knowing about the bias prevents it from affecting you", "More cautious after a win streak, which is actually healthy", "Expect losing streaks to end sooner than they do"],
        "scores": [1, 0, 0, 0],
    },
    # ── Capital & Money Psychology ────────────────────────────────────
    {
        "text": "You funded your trading account by selling your car. Every loss now feels like 'losing your car.' This is a problem because…",
        "options": ["You'll trade scared — money you can't afford to lose creates fear-based decisions that destroy edge execution", "It's motivating — you HAVE to make it work, which increases focus", "It's fine if you have a positive expectancy system", "The source of the money doesn't matter once it's in the account"],
        "scores": [1, 0, 0, 0],
    },
    {
        "text": "You have $10,000 in your account. You risk 1% ($100) per trade. But sometimes you think 'what's $100? I make that in an hour at work.' This mindset…",
        "options": ["Is healthy — detaching from the dollar amount helps you trade without fear", "Is dangerous — if $100 doesn't feel like real money, you'll be sloppy with risk because the 'punishment' for bad trades isn't felt", "Shows the account is properly sized for your income", "Means you should increase risk to 2% where it starts to feel meaningful"],
        "scores": [0, 1, 0, 0],
    },
    {
        "text": "Your account hit $25,000 — a number you never imagined reaching. Now you're trading differently. You're more conservative, taking fewer setups. What changed?",
        "options": ["Wisdom — protecting gains is smart at higher account levels", "The account size crossed a psychological barrier, and now the FEAR of losing back to $20K is distorting your decision-making", "Natural evolution from aggressive to conservative as accounts grow", "You should always get more conservative as your account grows"],
        "scores": [0, 1, 0, 0],
    },
    {
        "text": "You withdraw $5,000 profit from your account. The next week, you trade more aggressively. The likely reason?",
        "options": ["Confidence from the withdrawal — you proved you can make money", "The smaller account balance makes each trade feel less significant, reducing your respect for the capital", "No connection — your trading style shouldn't change based on withdrawals", "You want to rebuild the account quickly back to the pre-withdrawal level"],
        "scores": [0, 0, 0, 1],
    },
    {
        "text": "A trader with a $500 account is risking 10% per trade ($50). He says 'it's only $50.' This logic is…",
        "options": ["Valid — $50 is objectively a small amount", "The exact thinking that blows small accounts — percentage is what matters, not dollar amount", "Fine for learning — small accounts require more risk to grow", "Pragmatic — you can't grow a $500 account with 1% risk trades"],
        "scores": [0, 1, 0, 0],
    },
    {
        "text": "You're offered a trade: 80% chance of winning $200 vs 20% chance of losing $500. Expected value is +$60. Should you take it?",
        "options": ["Yes — positive expected value means you should always take the trade", "It depends on whether your account can ABSORB the $500 loss if it happens — EV alone isn't sufficient", "Yes — 80% probability is basically a sure thing", "No — the potential $500 loss is too large"],
        "scores": [0, 1, 0, 0],
    },
    {
        "text": "You make $2,000 in a day. You think 'If I make this every day, I'll make $500K a year!' This projection is…",
        "options": ["Motivational math — it shows what's possible", "Dangerous linear extrapolation — trading returns are non-linear, and exceptional days are outliers by definition", "Useful for setting annual goals", "A good way to calculate potential monthly income from trading"],
        "scores": [0, 1, 0, 0],
    },
    {
        "text": "You notice you take more risk on trades paid for by recent profits ('house money') vs. original capital. This is…",
        "options": ["Smart — playing with profits means you can afford to be aggressive", "The house money effect — profits are STILL your money, treating them as 'bonus' capital increases reckless behavior", "A good strategy for account growth", "A natural way to scale up as your account grows"],
        "scores": [0, 1, 0, 0],
    },
    {
        "text": "Your account is at $15,000. You want to buy a $15,000 watch as a reward for your trading success. This decision is…",
        "options": ["Earned — you made the money, enjoy it", "Potentially devastating — withdrawing 100% of your account for a luxury item shows you're trading for material rewards rather than compounding wealth", "Fine if you can fund the account again from your day job", "A celebration of your achievement"],
        "scores": [0, 1, 0, 0],
    },
    {
        "text": "Two traders have identical strategies. Trader A has $100K. Trader B has $5K. Who faces MORE psychological pressure?",
        "options": ["Trader A — more money at stake means more psychological pressure", "Trader B — the smaller account creates urgency to grow, leading to overtrading and over-leveraging", "Equal pressure — psychology is independent of account size", "Trader A — wealthy people have more to lose"],
        "scores": [0, 1, 0, 0],
    },
    {
        "text": "You're consistently profitable on a $10K account. A friend offers to give you $50K to trade. You should…",
        "options": ["Accept — more capital means more profit with the same edge", "Be very cautious — managing someone else's money adds a layer of psychological pressure that can destroy your edge", "Accept but take less risk percentage-wise", "Only accept if you've been profitable for at least 2 years"],
        "scores": [0, 1, 0, 0],
    },
    {
        "text": "Your account just crossed $50,000. You've never had this much money. You start treating your account like precious savings rather than working capital. How does this affect trading?",
        "options": ["It protects the account — being careful with large amounts is smart", "You'll under-trade and miss setups because the fear of going back below $50K overrides your system signals", "It naturally reduces risk, which is age-appropriate capital management", "You should feel protective — it took hard work to get here"],
        "scores": [0, 1, 0, 0],
    },
    {
        "text": "You calculate that you need to make 8% per month to quit your job. Your system averages 3%. You should…",
        "options": ["Optimize the strategy for higher returns", "Accept that the math doesn't work yet — either grow your capital until 3% provides enough income, or find ways to increase capital WITHOUT increasing risk", "Increase position size to close the gap", "Add more pairs and setups to increase trade frequency"],
        "scores": [0, 1, 0, 0],
    },
    {
        "text": "You lose $2,000 on a trade. That night you can't sleep, you're irritable with family, and you skip meals. This reaction tells you…",
        "options": ["Trading matters to you — passion is important", "Your position size is too large for your psychological capacity — the money risked per trade should NEVER affect your quality of life", "You had a bad day — it'll pass", "You need to develop thicker skin for trading"],
        "scores": [0, 1, 0, 0],
    },
    # ── Trade Management Psychology ───────────────────────────────────
    {
        "text": "Your trade is +1.5R and your TP is at +3R. Price stalls and forms a small reversal candle. You want to close to 'lock in' the profit. This impulse is…",
        "options": ["Smart trade management — taking profit when momentum stalls", "Fear-based — a single reversal candle within a +1.5R move is noise, and closing here means you'll never achieve your system's full R target", "Prudent — a guaranteed +1.5R is better than a potential +3R", "Active management — adjusting targets based on price action is professional"],
        "scores": [0, 1, 0, 0],
    },
    {
        "text": "You enter a trade and price immediately goes your way. Within 5 minutes you're at +0.5R. You feel euphoric. Watch out for…",
        "options": ["Nothing — enjoy the win", "The temptation to move your TP further because 'it's running so well' — or the opposite, closing early to capture the quick win", "A reversal — fast moves often retrace", "Over-leveraging the next trade because you feel invincible"],
        "scores": [0, 1, 0, 0],
    },
    {
        "text": "Your trailing stop is at +1R. Price is at +2.5R. You remove the trailing stop because 'I don't want to get stopped out of a big winner.' This decision…",
        "options": ["Is smart — trailing stops often exit too early in trending markets", "Just removed your ONLY protection against a full reversal — you're now risking 2.5R of open profit on hope", "Is reasonable if you plan to manage the exit manually", "Shows confidence in your analysis of the trend continuing"],
        "scores": [0, 1, 0, 0],
    },
    {
        "text": "You have 3 open trades. One is green, one is flat, one is red. You close the green one first for 'guaranteed' profit. This is an example of…",
        "options": ["Smart portfolio management — secure the winner and let the others develop", "The disposition effect — cutting winners and holding losers is the OPPOSITE of what profitable traders do", "Taking what the market gives you", "Risk reduction — fewer open positions means less exposure"],
        "scores": [0, 1, 0, 0],
    },
    {
        "text": "A trade is -0.5R against you. Your stop is at -1R. You start micro-managing every tick. This behavior will likely…",
        "options": ["Help you identify if the trade is failing before it hits your stop", "Cause you to exit prematurely on normal noise, turning what might become a winner into a confirmed loss", "Keep you engaged and alert to market changes", "Provide useful real-time data for future trade management"],
        "scores": [0, 1, 0, 0],
    },
    {
        "text": "You take partial profits at +1R (close half). The remaining position runs to +4R. You feel great about the +1R you locked in but terrible about the 'lost' half. The correct perspective?",
        "options": ["You made the right call — securing profits is always smart", "Your partial take-profit plan worked EXACTLY as designed — the regret about the 'other half' is irrational because you chose this structure IN ADVANCE", "You should have held the full position for +4R", "Adjust to taking only 25% off at +1R next time"],
        "scores": [0, 1, 0, 0],
    },
    {
        "text": "Your trade is running in profit. You keep checking your P&L every 30 seconds. Every uptick makes you happy, every downtick makes you anxious. What should you change?",
        "options": ["Check less frequently — set alerts at key levels and walk away", "Nothing — monitoring open trades is responsible", "Only check at candle closes on your trading timeframe, not on every tick", "Set a trailing stop and stop watching entirely"],
        "scores": [0, 0, 1, 0],
    },
    {
        "text": "You planned to hold a swing trade for 3-5 days. After 6 hours, it's +1.5R. You want to close because 'I can re-enter later.' The real reason you want to close is…",
        "options": ["Efficiency — bank the profit and find the next trade", "You can't handle the anxiety of watching open profit fluctuate for 3-5 days", "Smart management — taking profit when available is good practice", "You don't actually have the patience for swing trading"],
        "scores": [0, 1, 0, 0],
    },
    {
        "text": "Your trade has been open for 8 hours and hasn't moved. It's flat. You're bored and want to close it and find 'something better.' This restlessness is…",
        "options": ["A sign you should trade faster timeframes", "Dangerous — closing a perfectly valid trade because of BOREDOM is one of the most common edge-killers", "Understandable — stagnant trades tie up margin for no reason", "A signal the trade is dead and you should move on"],
        "scores": [0, 1, 0, 0],
    },
    {
        "text": "You move your SL to breakeven because you 'can't handle another loss today.' Your system doesn't have a BE rule. This action is…",
        "options": ["Conservative — protecting against another loss", "Emotional position management — your SL should be at a TECHNICAL level, not a psychological one", "Reasonable — daily emotional limits are valid", "Fine as long as you're willing to re-enter if it hits BE and reverses"],
        "scores": [0, 1, 0, 0],
    },
    {
        "text": "You have a winning trade and your spouse asks 'how much have you made?' Mid-trade, sharing specific P&L numbers can…",
        "options": ["Help you stay accountable", "Create external pressure to NOT close the trade at your planned TP because your spouse now has expectations", "Share the excitement and make trading more enjoyable", "Improve transparency in the household about finances"],
        "scores": [0, 1, 0, 0],
    },
    {
        "text": "Your trade hits your TP. You close it. Price continues another 200 pips in your direction. You should feel…",
        "options": ["Frustrated — you left 200 pips on the table", "Satisfied — your plan had a TP, price hit it, and you executed. What happened after is not your trade", "Motivated to hold longer next time", "Nothing — you followed the plan, which is all that matters"],
        "scores": [0, 1, 0, 0],
    },
    # ── System Design & Evaluation ────────────────────────────────────
    {
        "text": "You backtest your strategy and get 70% win rate over 200 trades. You're excited. But before going live, you should ask…",
        "options": ["Nothing — 200 trades at 70% is a strong sample", "Did I commit look-ahead bias, curve-fit the parameters, or cherry-pick the date range?", "How can I get it to 80%?", "What pairs does it work best on?"],
        "scores": [0, 1, 0, 0],
    },
    {
        "text": "Your strategy works on EUR/USD and GBP/USD but not on USD/JPY. You add a rule: 'don't trade JPY pairs.' This is…",
        "options": ["Smart — play to your system's strengths", "Potentially data-mining — unless you understand WHY the system fails on JPY, you might be overfitting to history", "A normal part of system development — not every strategy works on every pair", "Fine as long as you have enough setups on the remaining pairs"],
        "scores": [0, 1, 0, 0],
    },
    {
        "text": "You optimize your strategy's RSI parameter from 14 to 11 because 11 performed 0.3% better in backtesting. This optimization is…",
        "options": ["Data-driven improvement — always optimize based on data", "Likely curve-fitting — a 0.3% difference between RSI 14 and 11 is noise, not signal", "Worth implementing if the improvement is consistent across multiple pairs", "A good practice — small improvements compound over time"],
        "scores": [0, 1, 0, 0],
    },
    {
        "text": "Your system's win rate dropped from 58% to 51% over the last 3 months. Should you change anything?",
        "options": ["Yes — a 7% drop in win rate indicates the system is failing", "Maybe — first check if 51% is still within the expected statistical range for your system based on your sample size", "No — 51% is still above 50%, so the edge exists", "Add filters to improve the win rate back to 58%"],
        "scores": [0, 1, 0, 0],
    },
    {
        "text": "You have a system that makes money but you don't understand WHY it works. Is this a problem?",
        "options": ["No — results are all that matter", "Yes — if you don't understand the WHY, you can't distinguish between a broken system and a normal drawdown, and you'll abandon it at the worst time", "It depends on whether it's been profitable for more than a year", "No — many successful quant strategies aren't fully understood by their creators"],
        "scores": [0, 1, 0, 0],
    },
    {
        "text": "Your trading buddy has a system with a 45% win rate and 1:3 Risk Reward. You have a 65% win rate and 1:1.2 R:R. His system makes more money. You feel like your higher win rate SHOULD mean higher profit. Reality check?",
        "options": ["Your system IS better — higher win rate is always preferable", "Expectancy is what matters: his (0.45×3 - 0.55×1 = +0.80R) vs yours (0.65×1.2 - 0.35×1 = +0.43R) — math doesn't care about win rate", "Both systems are profitable, so comparison doesn't matter", "You need to increase your R:R while maintaining your win rate"],
        "scores": [0, 1, 0, 0],
    },
    {
        "text": "You forward test a strategy for 30 trades and it's profitable. You go live. Is 30 trades enough?",
        "options": ["Yes — 30 is the minimum for statistical significance", "No — 30 trades is a decent start but most statisticians want 100+ for confidence, and 30 includes zero trend changes or market regime shifts", "It depends on the win rate — high win rate needs fewer trades to validate", "30 is fine if they span at least 2 months of varying conditions"],
        "scores": [0, 1, 0, 0],
    },
    {
        "text": "Your system had a maximum historical drawdown of 12%. You should mentally prepare for a REAL drawdown of…",
        "options": ["12% — that's the tested maximum", "18-25% — real drawdowns typically exceed historical maximums, and you should plan for 1.5-2x your worst backtest", "10% — set a stop below the historical max to protect yourself", "12% exactly — if it exceeds that, the system is broken"],
        "scores": [0, 1, 0, 0],
    },
    {
        "text": "Two strategies have identical expectancy. Strategy A has 70% win rate. Strategy B has 35% win rate. Which is psychologically easier to trade?",
        "options": ["Strategy A — more frequent wins means better emotional experience and easier to stick with", "Strategy B — fewer wins means each one is more satisfying", "Both are equally easy — a rational trader focuses on expectancy", "The one with more trades per month because it stays engaging"],
        "scores": [1, 0, 0, 0],
    },
    {
        "text": "You discover your strategy's edge comes from ONE specific market condition that occurs ~20% of the time. The other 80% of the time, it's breakeven. You should…",
        "options": ["Improve the strategy for the 80% that's not working", "Trade ONLY during that 20% condition and sit flat the rest — concentrating your edge is smarter than diluting it", "Find a second strategy for the other 80%", "Accept the breakeven periods as the cost of the profitable 20%"],
        "scores": [0, 1, 0, 0],
    },
    # ── Social Dynamics & External Pressure ───────────────────────────
    {
        "text": "Everyone in your trading group is using the same ICT 'silver bullet' strategy. You're the only one trading supply/demand. You start doubting your method. This is…",
        "options": ["A valid signal — if everyone's using ICT successfully, maybe you should too", "Social conformity pressure — the popularity of a method says NOTHING about its edge. Your system's backtest data is what matters", "A sign to investigate ICT and see if it complements your approach", "Reasonable doubt — the consensus is usually right"],
        "scores": [0, 1, 0, 0],
    },
    {
        "text": "You post your trade in a group chat. Three experienced traders disagree with your analysis. You're now in the trade. What should you do?",
        "options": ["Close the trade — 3 experienced traders can't all be wrong", "Manage the trade based on YOUR plan, not their opinions — you entered for a reason", "Tighten your stop as a compromise", "Close half to reduce exposure in case they're right"],
        "scores": [0, 1, 0, 0],
    },
    {
        "text": "A 'guru' with 100K followers says 'trading psychology is overrated — just find a good strategy.' Your response should be…",
        "options": ["He's probably right — strategy matters more than psychology", "A good strategy you CAN'T execute is worth nothing — psychology is what bridges the gap between knowing and doing", "Strategy and psychology are equally important", "For beginners, strategy matters more; for experienced traders, psychology matters more"],
        "scores": [0, 1, 0, 0],
    },
    {
        "text": "You keep comparing your monthly returns to traders on social media. This month they posted +20%, you made +3%. This comparison is…",
        "options": ["Motivational — aspire to their level", "Toxic — social media returns are self-reported, survivorship-biased, cherry-picked, often on demo accounts, and comparing to them deteriorates your confidence in a REAL +3%", "Useful benchmarking — you know what's possible", "Helpful for setting realistic but ambitious goals"],
        "scores": [0, 1, 0, 0],
    },
    {
        "text": "Your trading mentor retires and you no longer have anyone to discuss trades with. You notice your discipline drops. This reveals…",
        "options": ["You need a new mentor — dependence on external guidance is normal", "Your discipline was partially 'borrowed' from the mentor relationship — you need to build independent systems", "Mentors are essential — find a new one immediately", "This is a temporary adjustment — your discipline will come back once you adapt"],
        "scores": [0, 1, 0, 0],
    },
    {
        "text": "A friend asks you to teach him to trade. You've been profitable for 1 year. Should you teach?",
        "options": ["Yes — teaching reinforces your own knowledge", "Be honest: tell him that 1 year of profitability doesn't make you qualified to teach, and bad lessons could cost him money", "Yes — he'll learn faster with a guide than alone", "Only if he understands the risks and you share your REAL track record including drawdowns"],
        "scores": [0, 0, 0, 1],
    },
    {
        "text": "You trade alone from home. No one in your life understands what you do. The isolation is affecting your mental health, which affects your trading. Best solution?",
        "options": ["Find an online trading community with serious, like-minded traders — the combo of accountability and understanding is irreplaceable", "Get a non-trading hobby for social interaction, keep trading solo", "Explain your trading to family and friends so they can support you", "Hire a trading coach for weekly check-ins"],
        "scores": [1, 0, 0, 0],
    },
    {
        "text": "Your group all went long GBP/USD. You think it's going short. The pressure to conform is real. What separates professionals from amateurs here?",
        "options": ["Professionals follow the majority — the group has more collective intelligence", "Professionals trade their OWN analysis and are comfortable disagreeing with everyone, because conviction comes from process not consensus", "Professionals would take a smaller position against the group", "Professionals would wait to see who's right before entering"],
        "scores": [0, 1, 0, 0],
    },
    {
        "text": "You secretly trade without telling your spouse. Why is the secrecy itself a trading risk?",
        "options": ["It's not a risk — finances can be private even in relationships", "Secrecy allows unaccountable behavior — if nobody knows, there's no external consequence for blown risk limits or revenge trades", "The stress of hiding it affects your trading focus", "It only matters if you're losing money"],
        "scores": [0, 1, 0, 0],
    },
    {
        "text": "A prop firm offers you funding. The rules limit your drawdown to 5%. Your normal max drawdown is 8%. Should you take the offer?",
        "options": ["Yes — adapt your system to fit the 5% max DD", "Think carefully — if your system's natural drawdown exceeds 5%, the prop firm rules will force you to deviate from your strategy at the worst times", "Yes — the extra capital outweighs the constraint", "Take it and simply use smaller position sizes to reduce max DD"],
        "scores": [0, 1, 0, 0],
    },
    # ── Professional Mindset & Long-Term Thinking ─────────────────────
    {
        "text": "You've been profitable for 3 years. A younger trader asks 'what's your secret?' The honest answer is usually…",
        "options": ["A great strategy that gives me an edge", "Survival — I made every mistake in the book, kept going, and slowly eliminated them. There is no secret", "Risk management above all else", "Discipline and patience"],
        "scores": [0, 1, 0, 0],
    },
    {
        "text": "You make $0 this month. But you didn't lose money either. How should you view a breakeven month?",
        "options": ["A wasted month — trading costs you time and opportunity cost", "A successful month of capital preservation during a period where your edge wasn't present — this IS the job sometimes", "Acceptable but disappointing", "Better than a losing month, but you need to generate returns to justify the effort"],
        "scores": [0, 1, 0, 0],
    },
    {
        "text": "You hear: 'Trading is 80% psychology, 20% strategy.' You've been spending 95% of your development time on strategy and 5% on psychology. This allocation…",
        "options": ["Is right — you need a good strategy before psychology matters", "Probably explains why your strategy 'works in backtesting but not in live trading'", "Is normal — most traders focus on strategy first, psychology second", "Should be reversed to 50/50 for maximum improvement"],
        "scores": [0, 1, 0, 0],
    },
    {
        "text": "A successful trader tells you he meditates for 20 minutes every morning before trading. You think that's 'woo-woo.' The research says…",
        "options": ["Meditation has no proven benefit for trading performance", "Meditation demonstrably improves focus, emotional regulation, and decision-making under pressure — all critical for trading", "It's a personal preference, not a performance enhancer", "Physical exercise would be more beneficial than meditation"],
        "scores": [0, 1, 0, 0],
    },
    {
        "text": "You realize that your WORST trades all share one characteristic: they were all taken outside your written plan. But they only represent 15% of your trades. The impact on your P&L is…",
        "options": ["Minor — 15% is a small fraction",  "Likely massive — Plan-violating trades typically have the WORST risk management, meaning 15% of trades can account for 50%+ of losses", "Proportional — 15% of trades ≈ 15% of losses", "Depends on the size of those trades"],
        "scores": [0, 1, 0, 0],
    },
    {
        "text": "You haven't traded in 2 weeks because there were no setups. You feel 'rusty.' Is rust a real concern?",
        "options": ["Yes — you need regular practice to stay sharp", "Only if you stopped doing your daily analysis — being FLAT isn't the same as being INACTIVE. Reviewing charts daily keeps skills sharp even with no trades", "Two weeks without a trade means your system is too strict", "Yes — you should lower your standards slightly to get more repetitions"],
        "scores": [0, 1, 0, 0],
    },
    {
        "text": "You read that 'elite traders make money in 7 out of 12 months.' You've been profitable in 8 out of 12. Does this make you elite?",
        "options": ["Yes — you're beating the benchmark", "Not necessarily — the months' magnitude matters more than the count. Are your winning months bigger than losing months? What's the overall annual return?", "Yes — consistency across months is a strong sign", "Hard to say — compare your Sharpe ratio, not just winning months"],
        "scores": [0, 1, 0, 0],
    },
    {
        "text": "Your trading system works. But it's boring. You make money slowly and predictably. You want excitement. The correct reframe is…",
        "options": ["Find a more exciting strategy that also makes money", "Boring and profitable IS the goal — excitement in trading comes from uncontrolled risk, which destroys accounts", "Add some discretionary elements to keep yourself engaged", "Trade a small 'fun' account on the side for excitement"],
        "scores": [0, 1, 0, 0],
    },
    {
        "text": "After trading full-time for 2 years, you miss having colleagues, a boss, and structure. This is affecting your trading. The healthiest response is…",
        "options": ["Go back to a regular job and trade on the side", "Build structure OUTSIDE of trading: community, accountability groups, scheduled social activities, routine — the trading lifestyle requires intentional design", "Join a prop firm for the team environment", "Learn to enjoy solitude — independence is the gift of full-time trading"],
        "scores": [0, 1, 0, 0],
    },
    {
        "text": "You track your screen time and discover you spend 8 hours watching charts but only take 1-2 trades per day. Is this efficient?",
        "options": ["No — you should trade more to justify the time investment", "The hours aren't wasted IF you're doing quality analysis, but check if most of that time is aimless staring vs. structured work", "8 hours is professional — full-time traders spend full days at the desk", "Efficient — finding 1-2 quality trades in 8 hours shows high standards"],
        "scores": [0, 1, 0, 0],
    },
    {
        "text": "A trader says: 'I treat trading as a business, not a hobby.' Concretely, this means…",
        "options": ["He has an LLC and does his own taxes", "He has a written plan, tracks metrics, reviews performance data, manages risk like a CFO, and doesn't let ego drive capital allocation", "He trades full-time and depends on it for income", "He takes it more seriously than hobbyists"],
        "scores": [0, 1, 0, 0],
    },
    {
        "text": "You've achieved consistent profitability. But you're not 'happy.' You thought making money trading would bring fulfillment. This is…",
        "options": ["A sign trading isn't for you after all", "Extremely common — the hedonic treadmill means external achievements don't create lasting happiness. Fulfillment must come from life OUTSIDE of trading too", "A signal you need bigger goals — a larger account, higher returns", "Normal — work isn't supposed to make you happy, it's supposed to make you money"],
        "scores": [0, 1, 0, 0],
    },
    {
        "text": "Your annual trading review shows you're profitable but your return-per-hour is below minimum wage. Is trading still worth it?",
        "options": ["No — if you can't beat minimum wage, get a job", "It depends on the trajectory — Year 1 rates are meaningless if the skill compounds. Most businesses lose money in Year 1", "Yes — trading has unlimited upside, minimum wage doesn't", "Only if you genuinely enjoy the process of trading itself"],
        "scores": [0, 1, 0, 0],
    },
    {
        "text": "You blow your biggest account ever. $40K gone. You want to quit. Before you decide, you should…",
        "options": ["Quit — $40K is a fortune and you should cut your losses", "Take a full month OFF (zero screen time), process the emotions, then evaluate: was it a system failure or a discipline failure? The answer determines your path", "Start again with a small account to see if you can rebuild", "Analyze what went wrong and immediately start again to 'get back on the horse'"],
        "scores": [0, 1, 0, 0],
    },
    # ── Market Structure Psychology ───────────────────────────────────
    {
        "text": "You see a huge red candle on the daily chart. Your gut says 'sell!' But your system says 'wait for a pullback.' Which voice should win?",
        "options": ["Your gut — big candles show strong momentum you should capitalize on", "Your system — always. The big candle is designed to create the exact emotional reaction you're having. Don't oblige", "Use both — enter on the pullback but with the bias of the gut", "Neither — wait until the dust settles and reassess"],
        "scores": [0, 1, 0, 0],
    },
    {
        "text": "You read that 'the market is designed to do what will hurt the MOST people.' If this is true, the correct response is…",
        "options": ["Fade the crowd — always trade against what most people are doing", "Recognize that crowded positions become liquidity targets, so be cautious when your trade is TOO popular", "Markets aren't designed — this is conspiracy thinking", "Use retail sentiment indicators to always trade the opposite direction"],
        "scores": [0, 1, 0, 0],
    },
    {
        "text": "A big stop hunt wick sweeps your level and reverses. You KNOW this was manipulation. The professional interpretation is…",
        "options": ["Stop hunting is unfair and regulators should prevent it", "Liquidity events are a NORMAL part of market structure — if your stop is at an obvious level, it WILL be targeted. Adjust your strategy, not your complaints", "You need a broker with better execution to avoid the wicks", "Use mental stops instead of hard stops to avoid being hunted"],
        "scores": [0, 1, 0, 0],
    },
    {
        "text": "The market has been in a tight range for 3 weeks. You're bored. You know a breakout is coming but not WHEN. The correct approach is…",
        "options": ["Set breakout orders in both directions — capture the move regardless", "Patience. Set alerts at the range boundaries. Do analysis. Don't force trades just because range-bound markets are boring", "Trade the range — buy support, sell resistance", "Switch to a different pair that's trending"],
        "scores": [0, 1, 0, 0],
    },
    {
        "text": "NFP comes in massively bullish for USD. Price spikes up... then crashes down. You're confused. The lesson?",
        "options": ["News is unreliable — stop trading fundamentals", "The market's reaction to news is MORE important than the news itself — 'buy the rumor, sell the news' exists because positioning BEFORE the event often determines the move", "Market manipulation caused the reversal", "This is why you should never trade during news releases"],
        "scores": [0, 1, 0, 0],
    },
    {
        "text": "You notice that your system performs best on trending days and terribly on ranging days. Your edge depends on trend. During a choppy week you should…",
        "options": ["Keep trading — you can't predict which day will trend", "Recognize the environment doesn't favor your edge and DRAMATICALLY reduce activity or sit flat entirely", "Switch to a range-trading approach for the week", "Use a trend indicator to filter which days to trade"],
        "scores": [0, 1, 0, 0],
    },
    {
        "text": "Price has tested a support level 5 times. Every bounce is weaker. A sixth test is happening. Most traders expect another bounce. The smarter read is…",
        "options": ["Support gets stronger the more times it's tested — buy the bounce", "Repeated tests WEAKEN support because buyers dry up and sellers accumulate — the sixth test is more likely to break than bounced from", "5 bounces is statistically significant — the 6th will likely bounce too", "It depends on the timeframe and context — no universal answer"],
        "scores": [0, 1, 0, 0],
    },
    {
        "text": "Asian session: price moves in a tight range. London open: price breaks out aggressively. You chase the breakout. By NY session, the breakout has completely reversed. What happened?",
        "options": ["Bad luck — breakouts sometimes fail", "Textbook liquidity grab — London open often creates a 'fake' move that captures stops above/below the Asia range before reversing. This is a known market structure pattern", "The US data reversed the London move", "London and NY sessions naturally have different directional biases"],
        "scores": [0, 1, 0, 0],
    },
    {
        "text": "You're short EUR/USD. A Federal Reserve member makes a surprise dovish comment. EUR/USD spikes up, hitting your SL. Later it reverses and crashes past your TP. You should…",
        "options": ["Be angry — the speech cost you a winning trade", "Accept it — unexpected events are WHY you use stop losses. The SL protected you against the possibility that the spike DIDN'T reverse", "Trade without stops during news-heavy weeks", "Set wider stops during the following day to account for similar events"],
        "scores": [0, 1, 0, 0],
    },
    {
        "text": "You see a 'V-bottom' reversal on the 5-minute chart. On the daily chart, price is in a clear downtrend. Which timeframe should dominate your decision?",
        "options": ["5-minute — the reversal is right in front of you", "The daily — higher timeframe trends override lower timeframe noise. A 5-minute V-bottom in a daily downtrend is likely a temporary bounce, not a reversal", "Both — enter on the 5-minute but only target the daily resistance", "Depends on your trading style — scalpers use 5min, swing traders use daily"],
        "scores": [0, 1, 0, 0],
    },
    # ── Miscellaneous Advanced Scenarios ──────────────────────────────
    {
        "text": "You need to make a decision in 10 seconds: market order now or limit order 5 pips below. Your heart rate increases. In this state, which should you choose?",
        "options": ["Market order — speed is important before it moves further", "Limit order — when your heart rate tells you there's urgency, the SLOWER choice is almost always the better one", "Whichever your system says — ignore the heart rate", "Market order at half size — compromise between speed and caution"],
        "scores": [0, 1, 0, 0],
    },
    {
        "text": "You've been trading for 5 years and still make emotional mistakes. You're embarrassed. Is 5 years enough to 'solve' psychology?",
        "options": ["Yes — after 5 years you should have this figured out", "No — trading psychology is a LIFELONG practice, not a problem to solve. Even 20-year veterans manage emotions, they've just built better systems for it", "It depends on how much deliberate practice you've done", "5 years is enough to know if you're capable of trading or not"],
        "scores": [0, 1, 0, 0],
    },
    {
        "text": "You have a choice: trade an A+ setup with 1:2 R:R on a pair you hate, or a B setup with 1:3 R:R on your favorite pair. Objectively you should trade…",
        "options": ["The A+ setup — setup quality trumps pair preference or R:R difference", "Your favorite pair — familiarity and confidence improve execution", "The 1:3 R:R — higher reward justifies slightly lower setup quality", "Neither — wait for an A+ setup on your favorite pair"],
        "scores": [1, 0, 0, 0],
    },
    {
        "text": "You daydream about the lifestyle you'll have when your account reaches $500K. Currently you have $8K. The danger of this daydream is…",
        "options": ["It's not dangerous — visualization is a proven success technique", "The gap between dream ($500K) and reality ($8K) creates subconscious pressure to take bigger risks to close the gap faster", "It's motivating and keeps you going through tough times", "No danger as long as you have a realistic plan to get there"],
        "scores": [0, 1, 0, 0],
    },
    {
        "text": "You're about to click 'BUY' and you feel CERTAIN it will work. The most dangerous word in that sentence is…",
        "options": ["Buy — it implies directional bias", "About — hesitation indicates uncertainty", "Certain — certainty is the enemy of good risk management. The moment you feel certain is when you're most vulnerable to oversizing and abandoning stops", "Click — impulsive execution from a phone or one-click button"],
        "scores": [0, 0, 1, 0],
    },
    {
        "text": "You've automated your strategy but you keep overriding the bot during drawdowns. What does this reveal?",
        "options": ["The bot needs better programming to handle drawdowns", "You trust the system with your LOGIC but not with your MONEY — the emotional brain overrides the rational brain every time", "You should use a fully hands-off approach with no override ability", "You need a hybrid system with some manual discretion"],
        "scores": [0, 1, 0, 0],
    },
    {
        "text": "Someone asks you: 'Can you make money trading forex?' The most psychologically mature answer is…",
        "options": ["Yes — I do it consistently", "Yes, it's possible, but most people fail because they underestimate the psychological demands and overestimate the speed of returns", "It's the hardest easy money you'll ever make", "Some can, some can't — it depends on personality and dedication"],
        "scores": [0, 1, 0, 0],
    },
    {
        "text": "You read that the average successful trader took 3-5 years to become consistently profitable. You're in year 2 and losing money. Your takeaway?",
        "options": ["You're behind schedule — you should be breakeven by year 2", "Average doesn't guarantee YOUR timeline — evaluate whether you're making PROGRESS (fewer mistakes, better process) not just profit", "You're on track — keep doing what you're doing", "3-5 years is for people who learn slowly — you can accelerate by studying harder"],
        "scores": [0, 1, 0, 0],
    },
    {
        "text": "You flip between 4 different trading strategies depending on what's working THIS week. Over 6 months, none of them is profitable. The diagnosis?",
        "options": ["None of the strategies have an edge", "Strategy hopping — you're never in one system long enough for the edge to play out statistically. You experience every drawdown but no recovery", "You haven't found the right strategy yet — keep searching", "The market is too unpredictable for any single strategy to work"],
        "scores": [0, 1, 0, 0],
    },
    {
        "text": "You track your 'time in trade' and discover you close winners 3x faster than losers. This asymmetry means…",
        "options": ["You're securing profits quickly, which is smart", "You're running your losers and cutting your winners — the exact OPPOSITE of what every trading principle teaches", "Winners move faster so they naturally close sooner", "You need tighter stops to close losers faster too"],
        "scores": [0, 1, 0, 0],
    },
    {
        "text": "It's New Year's Day. You're setting trading goals for the year. The BEST type of goal is…",
        "options": ["'Make $50,000 this year' — specific financial target", "'Follow my trading plan with 90%+ compliance this year' — a PROCESS goal you can control, not an outcome goal dependent on the market", "'Double my account this year' — ambitious return target", "'Take 200 trades this year' — volume-based target that ensures activity"],
        "scores": [0, 1, 0, 0],
    },
    {
        "text": "You're about to take your 1000th trade. Looking back at trades 1-100 vs trades 900-999, the BIGGEST difference should be…",
        "options": ["Higher win rate — experience improves selection", "Consistency of execution — the PROCESS quality of trade 999 vs trade 1 should be unrecognizable in terms of discipline, sizing, and emotional regulation", "Bigger position sizes from account growth", "Better entries from improved technical analysis"],
        "scores": [0, 1, 0, 0],
    },
    {
        "text": "A trader who makes money every single month for a year GUARANTEES future profitability. True or false?",
        "options": ["True — 12 months of consistency proves the edge", "False — 12 months might not include a market regime change, black swan event, or liquidity crisis. Past results genuinely do not guarantee future performance", "Mostly true — it's very strong evidence of a real edge", "True if the sample size is large enough (100+ trades per month)"],
        "scores": [0, 1, 0, 0],
    },
    {
        "text": "Your spouse asks: 'When will you start making real money from trading?' The HEALTHIEST response is…",
        "options": ["'Soon — I'm getting close'", "'I don't know — and anyone who gives a timeline is either lying or delusional. What I CAN tell you is whether my PROCESS is improving, and here's the data…'", "'Give me 6 more months and I'll show you'", "'I already am — look at last month's returns'"],
        "scores": [0, 1, 0, 0],
    },
    {
        "text": "You could either (A) improve your win rate from 55% to 60%, or (B) improve your rule compliance from 70% to 95%. Which creates MORE profit improvement?",
        "options": ["A — 5% win rate improvement means more winners", "B — most losses come from rule violations, not from the SYSTEM losing. Fixing compliance eliminates the #1 profit leak for most traders", "Equal — both improvements have similar magnitude", "A — strategy improvement is always more impactful than behavioral improvement"],
        "scores": [0, 1, 0, 0],
    },
    {
        "text": "You complete this quiz and score 3/10. Your reaction to this low score will itself tell you a LOT about your trading psychology. The ideal reaction is…",
        "options": ["Frustration — you expected to score higher", "Curiosity — 'What specifically did I get wrong and what does that reveal about blind spots in my thinking?'", "Dismiss it — a bot quiz doesn't reflect real trading ability", "Motivation — 'I'll study more and retake it'"],
        "scores": [0, 1, 0, 0],
    },
    {
        "text": "You just finished a 10-question psychology quiz. Your FIRST impulse is to retake it immediately trying to score higher. What does this impulse reveal?",
        "options": ["A healthy desire for self-improvement", "The same competitive/ego-driven impulse that causes overtrading — the need to 'win' even at a psychology quiz", "Good work ethic — practice makes perfect", "Nothing — it's natural to want to improve your score"],
        "scores": [0, 1, 0, 0],
    },
    {
        "text": "You enter a trade while eating lunch. You're distracted, chewing while clicking buttons. Is this a problem?",
        "options": ["No — multi-tasking is fine for experienced traders", "Yes — divided attention during order entry leads to sizing errors, wrong pairs, and missed stops. Entry is a surgical moment", "Only for scalpers who need full focus — swing traders can multitask", "Slightly — but the time saved is worth the small risk"],
        "scores": [0, 1, 0, 0],
    },
    {
        "text": "Your trading plan is 1 page long but very precise. Your friend's plan is 10 pages but vague. Whose plan is better?",
        "options": ["Your friend's — more thorough", "Yours — specificity beats length. A plan is only useful if every rule is clear and actionable", "Neither — plan quality depends on the results it produces", "Combine both approaches — detailed AND specific"],
        "scores": [0, 1, 0, 0],
    },
    {
        "text": "A trade you were going to take but didn't (because it didn't fully qualify) ends up being a massive winner. Your journal entry should…",
        "options": ["Reflect on the missed opportunity and how to catch similar moves", "Note the outcome but emphasize: 'My criteria said no, so the answer was no. I cannot evaluate a system based on trades I DIDN'T take'", "Add this scenario to your setup criteria for next time", "Calculate how much you missed and factor it into next month's targets"],
        "scores": [0, 1, 0, 0],
    },
    {
        "text": "You discover that your most profitable trades are the ones you felt LEAST confident about at entry. What does this counterintuitive data mean?",
        "options": ["You're bad at reading your own confidence accurately", "High-confidence trades tend to be crowded (obvious setups, wide consensus), while low-confidence trades often have more contrarian edge", "It's coincidence — confidence and trade quality aren't related", "You hesitate on good setups and rush into bad ones"],
        "scores": [0, 1, 0, 0],
    },
    {
        "text": "You just had a baby. Sleep-deprived, emotional, life-changing event. You plan to keep trading as usual. Realistic?",
        "options": ["Yes — trading provides income the family needs", "No — major life events drain the cognitive and emotional resources required for good trading decisions. Scale down or pause", "Yes if you switch to longer timeframes that require less screen time", "Only if you automate your entries"],
        "scores": [0, 1, 0, 0],
    },
    {
        "text": "You find yourself 'negotiating' with the market: 'Just come back to breakeven and I'll close.' How productive is this?",
        "options": ["Everyone does it — it's harmless self-talk", "It reveals magical thinking — the market doesn't negotiate, and this mindset delays the disciplined action of stopping out", "It helps process emotions about the trade", "It's a way of setting a mental take-profit, which is fine"],
        "scores": [0, 1, 0, 0],
    },
    {
        "text": "End of year trading review: you were profitable. But 85% of the profit came from just 3 trades. Should you be concerned?",
        "options": ["No — a few big winners carrying the year is normal for many strategies", "Yes — it means you might be dependent on outlier events rather than having a consistent edge. Investigate whether those 3 trades were system-generated or lucky", "That IS the goal — let winners run and cut losers short means a few big wins", "Excited — those 3 trades prove you can find big movers"],
        "scores": [0, 1, 0, 0],
    },
    {
        "text": "A researcher tells you: 'The average retail forex trader would make MORE money by trading LESS.' You find this…",
        "options": ["Hard to believe — more trades means more opportunities", "Completely plausible — overtrading is the #1 profit leak. Each additional trade has diminishing quality because the best setups are rare by definition", "Only true for bad traders — good traders benefit from more trades", "Interesting but not applicable to systematic traders"],
        "scores": [0, 1, 0, 0],
    },
    {
        "text": "You're watching a YouTube 'live trading' stream. The trader takes 5 trades in an hour and wins 4. You think 'I should trade like that.' What are you missing?",
        "options": ["Nothing — his skill is on display", "Survivorship bias (only successful streams get views), selection bias (he might turn off the stream during losses), and the fact that YOU are not him with his specific skillset and years of experience", "His commission costs might eat his profits", "He's probably on a demo account"],
        "scores": [0, 1, 0, 0],
    },
    {
        "text": "If anxiety about a trade is at 1/10, you probably under-risked. If anxiety is at 9/10, you over-risked. The sweet spot is…",
        "options": ["1/10 — trading should be stress-free", "3-4/10 — enough emotional engagement to execute seriously, but not enough to cloud judgment", "5/10 — perfectly balanced between caution and aggression", "Zero anxiety — a truly disciplined trader feels nothing"],
        "scores": [0, 1, 0, 0],
    },
    {
        "text": "You practice gratitude journaling: every day you write 3 things you're grateful for in your trading. This sounds like 'fluffy' advice. But research shows…",
        "options": ["It has zero impact on trading performance", "Gratitude practice reframes the brain from 'scarcity mode' (fear of loss, urgency to profit) to 'abundance mode' (patience, discipline) which directly improves decision quality", "It might improve mood but doesn't affect trade quality", "It's only useful during drawdowns to maintain morale"],
        "scores": [0, 1, 0, 0],
    },
    {
        "text": "You trade with money that was given to you as a gift. You notice you take more risk with it than with money you earned. This is because…",
        "options": ["Gift money doesn't feel 'real' — mental accounting makes you value different dollars differently based on source, not amount", "You're trying to grow it quickly to prove yourself to the gifter", "Natural — earned money feels more precious", "The gifter expected you to take risks with it"],
        "scores": [1, 0, 0, 0],
    },
    {
        "text": "A broker offers you 500:1 leverage. The ONLY correct psychological reaction is…",
        "options": ["Excitement — more leverage means faster account growth", "Caution — high leverage is a tool that amplifies BOTH gains and losses, and the temptation to over-leverage is the primary account killer in retail forex", "Indifference — leverage doesn't matter if your position sizing is correct", "Decline — anything above 50:1 is gambling"],
        "scores": [0, 1, 0, 0],
    },
    {
        "text": "'I'll start following my rules AFTER this one trade.' How many times have you thought this?",
        "options": ["Never — I always follow my rules", "Honestly? Many times — and 'after this one trade' never comes. This is the addictive loop of undisciplined trading", "Rarely — only in extreme circumstances", "This is a normal thought that doesn't indicate a problem"],
        "scores": [0, 1, 0, 0],
    },
    {
        "text": "You could either have A) $10,000 guaranteed or B) a 50% chance of $25,000 (expected value $12,500). Most traders choose A. Why is this a problem?",
        "options": ["It's not a problem — $10K guaranteed is the safe, smart choice", "Loss aversion makes traders prefer certainty over positive-EV gambles — the same psychology that causes cutting winners too short", "Most traders can't handle the 50% chance of nothing", "Both are valid — it depends on your financial situation"],
        "scores": [0, 1, 0, 0],
    },
    {
        "text": "Your trading edge requires you to endure a 15-trade losing streak before the winners arrive. Most traders would quit at loss 8. The differentiator for surviving to trade 16 is…",
        "options": ["Faith in the system", "Having TESTED the system thoroughly enough to KNOW (not believe) that 15-trade losers are within its normal distribution — knowledge beats faith", "A large enough account to absorb 15 losses", "Mental toughness and grit"],
        "scores": [0, 1, 0, 0],
    },
    {
        "text": "Final question. You've answered many questions about trading psychology. The real test isn't this quiz. It's…",
        "options": ["Whether you're profitable or not", "Whether you APPLY these principles during the next trade when your amygdala is screaming and your finger is hovering over the button", "How much you knew before taking this quiz", "Whether you remember these answers next week"],
        "scores": [0, 1, 0, 0],
    },
]
