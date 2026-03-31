"""
Question Bank — Part 2: Revenge Trading, Tilt & Recovery (100 questions)
"""

QUESTIONS_REVENGE = [
    {
        "text": "You just got stopped out on a textbook setup. Price reversed immediately after hitting your stop. You feel the urge to re-enter. You…",
        "options": ["Re-enter — the setup is still valid, you just got unlucky with the stop", "Walk away from the screen for at least 30 minutes before making ANY decision", "Re-enter with a wider stop this time — clearly it was too tight", "Accept the stop as proof that you need to adjust your stop placement method"],
        "scores": [0, 1, 0, 0],
    },
    {
        "text": "You've taken 3 losses in a row. All were valid setups. Your process was perfect but the outcomes weren't. You should…",
        "options": ["Stop trading for the day — 3 losses is your hard limit regardless of quality", "Keep trading — if your process was correct, stopping would be emotional, not logical", "Reduce position size by half and continue — good process in a drawdown", "Review the 3 losses to see if there's a pattern you're missing"],
        "scores": [1, 0, 0, 0],
    },
    {
        "text": "After a -3% loss, you spot what looks like an incredible A+ setup. Is it really a great trade or revenge in disguise?",
        "options": ["If the setup meets all criteria, it's real — take it at full size", "It doesn't matter how 'perfect' it looks — your judgment is compromised after a big loss", "Take it at half size as a compromise", "Ask a trading buddy to validate the setup before you enter"],
        "scores": [0, 1, 0, 0],
    },
    {
        "text": "You're down 2% and it's 2pm. Your daily loss limit is 2%. A high-probability setup appears. Your rules say stop at 2%. You…",
        "options": ["Take it — this setup is too good and could recover the whole day", "Follow the rule. 2% means done. No exceptions, no matter how good the setup looks", "Take it at quarter size — technically you're still managing risk", "Adjust your daily limit to 3% this one time since the setup quality warrants it"],
        "scores": [0, 1, 0, 0],
    },
    {
        "text": "You closed a winner too early and left 80 pips on the table. The frustration is eating at you. Your next action should be…",
        "options": ["Re-enter to capture the remaining move — the trade is still going", "Journal the early exit as a management error and move on to the next setup", "Adjust your take-profit rules to hold trades longer in the future", "Feel the frustration, acknowledge it, then do nothing until the next session"],
        "scores": [0, 0, 0, 1],
    },
    {
        "text": "A losing streak has put you down 8% for the month. You have 6 trading days left. The temptation to 'make it back' is strong. Best approach?",
        "options": ["Increase position size slightly — you need to be aggressive to recover", "Reduce position size to half and focus only on A+ setups for the rest of the month", "Take a full week off and start fresh next month", "Trade normally — changing anything because of P&L is emotional trading"],
        "scores": [0, 1, 0, 0],
    },
    {
        "text": "You lost on USD/JPY, so you immediately look for a setup on USD/JPY to 'get your money back from that pair.' This behavior is…",
        "options": ["Fine if the new setup is valid — the pair owes you nothing but valid setups are valid setups", "Classic revenge trading — you're selecting the pair based on emotion, not analysis", "Strategic — you already have context on that pair's behavior today", "Acceptable if you wait at least 1 hour before re-entering the same pair"],
        "scores": [0, 1, 0, 0],
    },
    {
        "text": "Your stop loss was hunted by a wick. You KNOW it was manipulation. The emotional response is rage. The professional response is…",
        "options": ["Widen stops to avoid the wicks — adapt to the manipulation", "Review whether your stop was at an obvious liquidity level, and adjust your placement strategy", "Accept that stop hunts are part of the game and your stop was too obvious", "Enter again immediately — the thesis is intact, only the stop was hit"],
        "scores": [0, 1, 0, 0],
    },
    {
        "text": "You've blown through your daily loss limit for the first time in 3 months. You're ashamed. The most productive next step?",
        "options": ["Double down tomorrow to make it back quickly and return to normal", "Journal exactly what happened, identify the trigger, and add a safeguard", "Take 2-3 days off to reset mentally before coming back", "Tell your accountability partner or group what happened"],
        "scores": [0, 1, 0, 0],
    },
    {
        "text": "After 5 consecutive winners, you lose big on trade #6. You feel like you 'gave back' your profits. This mindset is…",
        "options": ["Natural — no one likes giving back profits", "Problematic — it means you're mentally banking unrealized gains and treating losses differently after wins", "Motivational — it shows you care about your P&L", "A sign you should have stopped at 5 winners"],
        "scores": [0, 1, 0, 0],
    },
    {
        "text": "You realize you've doubled your normal trading frequency after a losing day. You didn't consciously decide to — it just happened. This is…",
        "options": ["Your subconscious trying to recover losses — classic tilt behavior you need to address immediately", "Normal adaptation — more trades means more chances to recover", "A sign your system has more opportunities today", "Not a problem if the extra trades are all valid setups"],
        "scores": [1, 0, 0, 0],
    },
    {
        "text": "A trade you exited at a loss just hit what would have been your take profit. You feel physically sick. The correct interpretation?",
        "options": ["You made the wrong decision to exit — learn to hold through pain next time", "Your exit rules need adjustment — this data point matters", "One trade hitting TP after you exited is not enough data to change anything", "You should re-enter now to capture any remaining move"],
        "scores": [0, 0, 1, 0],
    },
    {
        "text": "Your trading buddy says: 'Just forget the loss and move on.' Is this good advice?",
        "options": ["Yes — dwelling on losses is unproductive", "Partially — you should process the loss THEN move on, not suppress it", "No — you need to deeply analyze every loss to improve", "Yes — emotional detachment from outcomes is the goal"],
        "scores": [0, 1, 0, 0],
    },
    {
        "text": "You're on a 7-trade losing streak. All valid setups. A new A+ setup appears. Honestly, what's happening inside your head?",
        "options": ["'This one HAS to work' — and that desperation is exactly why you should skip it", "Confidence — your edge plays out over 100+ trades, not 7", "Fear — what if this is loss #8?", "Numbness — you've stopped caring about individual trade outcomes"],
        "scores": [0, 1, 0, 0],
    },
    {
        "text": "You made an impulsive revenge trade and it actually won. The lesson here is…",
        "options": ["Sometimes instinct beats rules", "The worst possible outcome — it just reinforced terrible behavior", "It worked this time, but you got lucky — don't repeat it", "Maybe your 'revenge' trades are actually based on solid subconscious analysis"],
        "scores": [0, 1, 0, 0],
    },
    {
        "text": "After a losing week, you spend the weekend binge-watching trading courses and backtesting new strategies. This is likely…",
        "options": ["Productive self-improvement during downtime", "Anxiety-driven behavior trying to 'fix' what might not be broken", "Exactly what successful traders do — constant learning", "A good use of your weekend to come back stronger Monday"],
        "scores": [0, 1, 0, 0],
    },
    {
        "text": "You notice your heart rate increases and palms sweat after a loss. Before your next trade you should…",
        "options": ["Push through it — successful traders handle pressure", "Recognize these as physiological signs you are NOT in a state to trade well and step away", "Take a few deep breaths and enter the next trade — breathing exercises fix everything", "Use the adrenaline — heightened arousal can improve pattern recognition"],
        "scores": [0, 1, 0, 0],
    },
    {
        "text": "You lost $500 on trade 1 and then made $500 on trade 2. You're breakeven for the day but feel like you need one more winner. Why?",
        "options": ["Because breakeven days feel like losses — the pain of the first loss isn't erased by the second win", "Because you're in the zone and should capitalize on it", "Because one more winner would confirm your recovery and build confidence", "That feeling is irrational — you're breakeven, act like it and stop if no setup exists"],
        "scores": [0, 0, 0, 1],
    },
    {
        "text": "Your monthly P&L is -5%. You start thinking about adding funds to your account to 'dilute' the loss percentage. This is…",
        "options": ["A reasonable capital management technique", "Paperwork psychology — you're trying to make the number look better without actually trading better", "Smart if you have the funds available", "Only makes sense if you're averaging into a larger account over time anyway"],
        "scores": [0, 1, 0, 0],
    },
    {
        "text": "You enter a revenge trade and price immediately goes against you. Instead of stopping out, you move your stop loss further. Now you're…",
        "options": ["Giving the trade more room to breathe — smart adaptation", "Two psychological mistakes deep — revenge entry AND stop manipulation", "Fine as long as the wider stop is at a technical level", "Managing the trade dynamically based on new information"],
        "scores": [0, 1, 0, 0],
    },
    {
        "text": "After a big loss, your spouse/partner asks 'how was trading today?' You feel the urge to lie or minimize. Why does this matter for your development?",
        "options": ["It doesn't — your private P&L is your business", "If you can't be honest about losses, you can't objectively analyze your trading", "It's normal to shield loved ones from volatility stress", "You should separate trading emotions from personal relationships entirely"],
        "scores": [0, 1, 0, 0],
    },
    {
        "text": "You revenge traded, lost more, and now you're down 6% in a single day. The absolute first thing you should do?",
        "options": ["Close all platforms and don't open them again today — damage control is the only priority", "Analyze what went wrong so you can trade better tomorrow", "Set a hard daily loss limit in your broker's settings so this can't happen again", "Call a trading mentor and talk through what happened"],
        "scores": [1, 0, 0, 0],
    },
    {
        "text": "You catch yourself scrolling for setups faster than usual after a loss. Your eyes are scanning but you're not really analyzing. This is…",
        "options": ["Efficient scanning — you're experienced enough to spot setups quickly", "Hunting mode — your brain wants a trade to fix the pain, not a GOOD trade", "Normal — sometimes setups jump out at you", "Fine as long as you slow down before actually entering anything"],
        "scores": [0, 1, 0, 0],
    },
    {
        "text": "You've consciously identified that you're tilting. You know you should stop trading. But you 'feel fine.' Should you trust that feeling?",
        "options": ["Yes — if you feel fine, you are fine", "No — tilt often masks itself as calmness or certainty because your brain is in autopilot mode", "It depends on whether your last trade was impulsive or systematic", "Trust it if you've taken at least 15 minutes to cool down"],
        "scores": [0, 1, 0, 0],
    },
    {
        "text": "Your friend says he never revenge trades. He says he just 'doesn't feel the urge.' What's the likely truth?",
        "options": ["He's naturally more disciplined than most traders", "He either hasn't traded long enough, doesn't risk enough to feel pain, or he's lying", "Some people genuinely don't have revenge impulses — it's personality-based", "He's probably using a fully automated system that removes emotion"],
        "scores": [0, 1, 0, 0],
    },
    {
        "text": "You set a rule: after 2 losses, take a 1-hour break. On day 1, you break the rule. On day 2, you follow it. On day 3, you break it again. This pattern suggests…",
        "options": ["The rule needs to be easier to follow — maybe make it 30 minutes", "You need an external enforcement mechanism because willpower alone is inconsistent", "You're improving — 1 out of 3 days following the rule is a start", "Rules are guidelines, not absolutes — flexibility is key"],
        "scores": [0, 1, 0, 0],
    },
    {
        "text": "You're in a drawdown and your internal voice says 'you're a terrible trader.' The healthy response is…",
        "options": ["Argue back with facts — look at your track record and prove the voice wrong", "Recognize that self-talk during drawdowns is emotion, not fact, and let it pass without engaging", "Use it as motivation to work harder", "Listen to it — self-criticism drives improvement"],
        "scores": [0, 1, 0, 0],
    },
    {
        "text": "You lost -4R on a single trade because you refused to honor your stop. Now you want to 'make up for it' with 4 separate 1R trades. This impulse is…",
        "options": ["Mathematically sound — 4 wins at 1R each would cover the loss", "Revenge logic wearing a mathematical costume — you'd need 4 consecutive winners which is not guaranteed", "A reasonable approach if the setups are all A-grade", "Better than trying to make it back in one trade"],
        "scores": [0, 1, 0, 0],
    },
    {
        "text": "It's Friday. You're down for the week. You see a 'perfect' setup 30 minutes before close. The weekend deadline is creating urgency. This setup is…",
        "options": ["Valid regardless of what day it is — good setups don't have calendars", "Contaminated by the emotional pressure of closing the week red", "Worth taking if you can hold over the weekend", "Best entered as a limit order for Monday's open"],
        "scores": [0, 1, 0, 0],
    },
    {
        "text": "After your worst month ever (-12%), you consider lowering your risk from 1% to 0.5% per trade. This is…",
        "options": ["Smart risk management — protect your capital during drawdowns", "A reasonable adjustment, but check if the decision is based on fear or logic", "Unnecessary if your system has positive expectancy — drawdowns are normal", "The right call — always scale down after a bad month"],
        "scores": [0, 1, 0, 0],
    },
    {
        "text": "You notice you only revenge trade on certain pairs. GBP/JPY losses make you tilt but EUR/USD losses don't. Why does this matter?",
        "options": ["It doesn't — revenge trading is revenge trading regardless of the pair", "It suggests the volatility and speed of GBP/JPY triggers a specific emotional response worth examining", "It means you should stop trading GBP/JPY", "It's because GBP/JPY losses are bigger due to the pip value"],
        "scores": [0, 1, 0, 0],
    },
    {
        "text": "You read that 'successful traders have short memories.' You interpret this as…",
        "options": ["Don't dwell on losses — quickly forget them and move on", "A misleading oversimplification — the best traders PROCESS losses fully, then release them", "You should literally stop thinking about previous trades", "Focus on the next trade, not the last one"],
        "scores": [0, 1, 0, 0],
    },
    {
        "text": "You're reviewing your journal and notice 80% of your biggest losses came from trades taken within 30 minutes of a prior loss. This data should make you…",
        "options": ["Add a mandatory 30-minute cooling period after every loss to your trading rules", "Feel guilty about all the money you've wasted on revenge trades", "Reduce position size for any trade taken within 30 minutes of a loss", "Use a timer that locks your platform for 30 minutes after each loss"],
        "scores": [1, 0, 0, 0],
    },
    {
        "text": "Two traders both lose $1,000. Trader A revenge trades and loses another $2,000. Trader B walks away and trades normally the next day. The REAL difference between them is…",
        "options": ["Discipline — Trader B has more of it", "Self-awareness — Trader B recognizes emotional states and has a plan for them", "Experience — Trader B has been through more losses", "Risk tolerance — Trader A simply can't handle $1,000 losses"],
        "scores": [0, 1, 0, 0],
    },
    {
        "text": "You've installed a browser extension that blocks your broker's website after 3 losses. A friend calls this 'extreme.' You think…",
        "options": ["He's right — it's babying yourself and won't build real discipline", "External guardrails are more reliable than willpower — this is a mature decision", "It's a temporary tool until you build the discipline to self-regulate", "It's unnecessary if you journal properly"],
        "scores": [0, 1, 0, 0],
    },
    {
        "text": "You notice your revenge trades have a 55% win rate but a negative expectancy because the losers are much bigger. This means…",
        "options": ["Your entries are actually good — just tighten the stops on revenge trades", "The win rate is deceiving you into thinking revenge trading 'works' when it's actually destroying your account", "You can make revenge trading profitable with better risk management", "55% win rate proves your analysis is solid even when emotional"],
        "scores": [0, 1, 0, 0],
    },
    {
        "text": "After a bad loss, you KNOW you shouldn't trade but you rationalize it: 'My system says trade, so not trading would be breaking my rules.' Is this valid?",
        "options": ["Yes — if the system generated a signal, you should take it", "No — your rule to stop after X losses IS part of your system, and it takes priority", "Partially — take it at reduced size as a compromise", "It depends on whether the drawdown rule or the signal rule was written first"],
        "scores": [0, 1, 0, 0],
    },
    {
        "text": "Your account is down 15% this quarter. Your yearly target is 30%. You start thinking about increasing risk to 'catch up.' This is…",
        "options": ["Math — you need bigger returns per trade to hit the annual target", "The exact thought pattern that turns 15% drawdowns into blown accounts", "Reasonable if you increase risk gradually, not all at once", "Something to discuss with a mentor before acting on"],
        "scores": [0, 1, 0, 0],
    },
    {
        "text": "You catch yourself saying 'the market is wrong' after a loss. The professional reframe is…",
        "options": ["The market is never wrong — my analysis didn't account for something", "Sometimes the market IS irrational, and that's not your fault", "The market can be wrong short-term — your analysis might be right long-term", "Neither is 'wrong' — trading is probabilities and this time it didn't work out"],
        "scores": [0, 0, 0, 1],
    },
    {
        "text": "You've developed a physical 'tell' before revenge trading — you lean forward in your chair and grip the mouse tighter. Knowing this, you should…",
        "options": ["Use an ergonomic setup to prevent the physical signs", "Set this physical state as your RED ALERT trigger to step away from the desk immediately", "Practice relaxation techniques while trading", "It's interesting but physical tells don't actually affect trade quality"],
        "scores": [0, 1, 0, 0],
    },
    {
        "text": "You lost on NFP. Not because of the number — your analysis was right. But slippage caused a stop out. The frustration is about…",
        "options": ["The unfairness — you were right but still lost", "A controllable factor you ignored — trading NFP WITH tight stops is known to cause slippage stops", "Your broker's execution quality — time to switch brokers", "Bad luck — nothing you could have done differently"],
        "scores": [0, 1, 0, 0],
    },
    {
        "text": "You lose a trade on Monday and can't stop replaying it in your mind on Tuesday. The trade is affecting your Tuesday analysis. You should…",
        "options": ["Trade anyway — Tuesday is a new day with new opportunities", "Write out a complete analysis of Monday's loss, extract ONE lesson, then deliberately close the book on it", "Skip Tuesday and come back Wednesday with a clear head", "Meditate to clear your mind, then trade normally"],
        "scores": [0, 1, 0, 0],
    },
    {
        "text": "Your girlfriend/boyfriend broke up with you last night. You sit down to trade the London open. Honestly, you should…",
        "options": ["Trade — trading is separate from personal life", "Not trade — your emotional baseline is devastated and it WILL affect your decisions", "Trade demo only if you need the routine", "Trade at reduced size — acknowledge the distraction but stay in the game"],
        "scores": [0, 1, 0, 0],
    },
    {
        "text": "After recovering from a drawdown back to breakeven, you feel like you haven't made any money because you only 'got back to zero.' The correct perspective is…",
        "options": ["You're right — breakeven isn't profit, the drawdown was wasted time", "Successfully recovering from a drawdown IS a demonstration of skill — most traders blow up", "Breakeven is neutral — neither good nor bad", "Use it as motivation to never draw down that far again"],
        "scores": [0, 1, 0, 0],
    },
    {
        "text": "You just had your biggest single-day loss. Everything feels wrong. The one thing that will help most RIGHT NOW is…",
        "options": ["A detailed post-mortem analysis of every trade", "Physical separation from the charts — go for a walk, exercise, call a friend", "Reminding yourself of your overall track record and win rate", "Setting up a revenge-proof system with hard daily loss limits"],
        "scores": [0, 1, 0, 0],
    },
    {
        "text": "You notice that after a loss you always switch to a smaller timeframe looking for 'quicker' setups. Why is this dangerous?",
        "options": ["Smaller timeframes are choppy and harder to trade", "Your system isn't designed for smaller timeframes, so every trade is discretionary gambling", "Speed of recovery isn't the issue — smaller TFs have lower win rates", "It's actually smart — smaller timeframes let you compound faster"],
        "scores": [0, 1, 0, 0],
    },
    {
        "text": "You've identified 3 personal triggers that cause revenge trading: (1) losses on your biggest position, (2) stop hunts, (3) missing a winner. The best use of this self-knowledge is…",
        "options": ["Create a specific protocol for each trigger — different situations need different responses", "Have one universal rule: walk away for 30 minutes after any of those events", "Reduce your biggest position size so trigger #1 hurts less", "Use all three as reasons to never trade those scenarios again"],
        "scores": [1, 0, 0, 0],
    },
    {
        "text": "You're keeping a 'tilt journal' separate from your trading journal where you record emotional episodes. After 3 months, you realize your worst tilt days are always Mondays. This insight…",
        "options": ["Means you should skip Monday trading sessions entirely", "Suggests weekend anticipation or weekend gap anxiety might be a factor worth investigating", "Is probably coincidence — day of the week doesn't affect psychology", "Means you need a better Sunday prep routine"],
        "scores": [0, 1, 0, 0],
    },
    {
        "text": "You revenge traded, won, and now you feel GREAT. You want to keep trading. The experienced trader knows…",
        "options": ["Ride the momentum — you're in the zone", "This is the most dangerous moment — the win just flooded your brain with dopamine that will fuel more reckless trades", "Take the win and stop — you earned it, now bank it", "One more trade, then stop — end the day on a high"],
        "scores": [0, 1, 0, 0],
    },
    {
        "text": "You ask an AI chatbot (like this one) whether you should keep trading after a big loss. The fact that you're asking an AI instead of following your pre-written rules suggests…",
        "options": ["Good use of technology — getting an objective second opinion", "You're looking for permission to do what you know you shouldn't", "You don't have clear enough post-loss rules", "Nothing wrong — AI can provide level-headed analysis"],
        "scores": [0, 1, 0, 0],
    },
    {
        "text": "Your risk management system automatically locks you out after a -3% day. Today you hit -3% and the lockout activated. You feel relieved. This tells you…",
        "options": ["The system is working perfectly — external controls are effective", "Your relief proves you KNEW you would have kept trading without the lock — you need to build internal discipline too", "You should keep the system permanently", "Relief is the correct emotion — the guardrail saved you money"],
        "scores": [0, 1, 0, 0],
    },
    {
        "text": "A professional poker player says: 'I never tilt because I think in terms of expected value over 10,000 hands.' How does this apply to trading?",
        "options": ["It means you should think about your next 10,000 trades, not the next trade", "The principle is right — but in practice, humans can't emotionally process single losses as 'just data' without training", "Poker math applies directly to trading — both are probability games", "If you adopt this mindset, you'll never revenge trade"],
        "scores": [0, 1, 0, 0],
    },
    {
        "text": "After a loss, you immediately open a chart on a pair you've NEVER traded before. Be honest — what's really happening?",
        "options": ["Exploring new opportunities — diversification is smart", "Your brain is trying to escape from the pain of the familiar pair by seeking novelty", "Maybe a fresh chart will give you a fresh perspective", "You're expanding your trading universe, which is long-term positive"],
        "scores": [0, 1, 0, 0],
    },
    {
        "text": "You read a quote: 'Your best trading day and worst trading day should look identical — same process, same emotions.' You find this…",
        "options": ["Unrealistic — humans have emotions and pretending otherwise is dangerous", "The goal — not to be emotionless, but to have processes so robust that emotions don't alter behavior", "Only possible for algorithmic traders, not discretionary ones", "Inspirational but impractical in real-world trading"],
        "scores": [0, 1, 0, 0],
    },
    {
        "text": "You are in a losing streak and a newer trader in your group asks for advice. You notice you're giving them advice you're not following yourself. This gap between your knowledge and actions indicates…",
        "options": ["You understand the concepts but your emotional execution lags behind — this is the #1 growth area", "Everyone gives better advice than they follow — it's normal", "You should focus on teaching since you're better at the theory", "You know the right answers, you just need more willpower"],
        "scores": [1, 0, 0, 0],
    },
    {
        "text": "Your drawdown has lasted 6 weeks. You haven't revenge traded ONCE. But you notice you've become extremely passive — skipping valid setups out of fear. Is this better than revenge trading?",
        "options": ["Yes — at least you're not losing more money", "No — fear-based avoidance is the OTHER side of the same emotional coin as revenge trading", "It's much better — protecting capital is always smart during drawdowns", "Yes — missing trades costs nothing, revenge trading costs everything"],
        "scores": [0, 1, 0, 0],
    },
    {
        "text": "You have 2 trading accounts. One is down 10%, one is up 5%. You find yourself risk-seeking on the down account and conservative on the up one. This is an example of…",
        "options": ["Good portfolio management — aggressive where you need to catch up, conservative to protect gains", "Mental accounting bias — money is money, and you're treating identical dollars differently across accounts", "Natural human behavior that doesn't affect you since the total portfolio is still positive", "Efficient capital allocation across different risk profiles"],
        "scores": [0, 1, 0, 0],
    },
    {
        "text": "After blowing your monthly target, you consider switching from manual to automated trading to 'remove emotions.' This switch would likely…",
        "options": ["Solve the emotional trading problem completely", "Move the emotional problem from execution to system management — you'll override the bot during drawdowns", "Be a good long-term solution if the algorithm is properly tested", "Work if combined with deleting your manual broker login"],
        "scores": [0, 1, 0, 0],
    },
    {
        "text": "You traded drunk last night, lost $800, and woke up ashamed. Besides the financial loss, the REAL damage is…",
        "options": ["The $800 — money lost is money lost", "The trust you just broke with yourself — every future commitment to your rules is now weaker", "The bad trade data in your journal that will skew your stats", "The hangover that prevents good trading today"],
        "scores": [0, 1, 0, 0],
    },
    {
        "text": "You've identified that revenge trading costs you ~$3,000 per year based on your journal data. You could spend $500 on a trading psychology course. Is this a good investment?",
        "options": ["Yes — if it reduces revenge trading by even 20%, the ROI is massive", "Maybe — but courses rarely change deep behavioral patterns", "No — you could just write better rules for free", "Only if the course specifically addresses revenge trading, not general 'mindset'"],
        "scores": [1, 0, 0, 0],
    },
    {
        "text": "You just set a new personal record for consecutive losses: 11. Your system's backtested maximum was 9. You're now in uncharted territory. You should…",
        "options": ["Stop live trading and run a new backtest to verify the system still works", "Recognize 11 vs 9 is within normal statistical variance — continue with reduced size", "Switch to demo until the streak breaks", "Question whether market conditions have fundamentally changed for your system"],
        "scores": [0, 0, 0, 1],
    },
    {
        "text": "You catch yourself thinking 'I'll just scalp for small gains to recover.' You're normally a swing trader. This urge is…",
        "options": ["Practical — small gains add up and improve confidence", "Dangerous — you're not a scalper and this is desperation disguised as strategy adaptation", "Fine on a demo account to rebuild confidence", "Worth trying as long as you use your normal risk per trade"],
        "scores": [0, 1, 0, 0],
    },
    {
        "text": "Your trading coach asks: 'On a scale of 1-10, how much do individual losses affect your next trade?' You answer 3. Your journal data shows it's actually 7. This gap means…",
        "options": ["You have a positive self-image, which is important for trading confidence", "You lack self-awareness about your emotional patterns, which is more dangerous than the revenge trading itself", "Your perception of your own resilience is off — use the data, not your feelings", "The journal data is probably wrong — you record more after bad trades, skewing the data"],
        "scores": [0, 0, 1, 0],
    },
    {
        "text": "You've been in a drawdown for 3 months. Slowly, you start thinking about quitting trading entirely. Is this thought productive?",
        "options": ["Yes — maybe trading isn't for you and quitting is the smart move", "It's worth examining — if you have a tested edge AND the capital AND the stomach for drawdowns, quitting is emotional", "3 months is a reasonable time to evaluate whether to continue", "Quitting during a drawdown means you'll never know if your system works long-term"],
        "scores": [0, 1, 0, 0],
    },
    {
        "text": "You're tempted to check your P&L after every trade. Your mentor says 'only check P&L once per week.' This advice is…",
        "options": ["Impractical — you need to know your P&L for position sizing", "Directionally correct — the more you focus on P&L, the more emotional your trading becomes", "Only useful for beginners — experienced traders can handle frequent P&L checks", "Good advice that should be followed literally"],
        "scores": [0, 1, 0, 0],
    },
    {
        "text": "A trade goes against you and you add to the losing position because 'the entry is even better now.' You…",
        "options": ["Are cost-averaging intelligently — the setup is even more attractive at this price", "Need to check if adding to losers is actually in your trading plan, and if not, you just made a fear-based decision", "Should only add to losers at predefined levels, not impulsively", "Are managing risk by getting a better average entry"],
        "scores": [0, 1, 0, 0],
    },
    {
        "text": "End of the week: -3 trades, +2 trades, net negative. You describe the week as 'terrible.' A psychologically healthy framing would be…",
        "options": ["'3 losses is bad — I need to improve my win rate'", "'I executed my process 5 times. Let me evaluate the QUALITY of those executions, not the outcomes'", "'Net negative is net negative — no point sugarcoating it'", "'Not bad for a learning week — every loss teaches something'"],
        "scores": [0, 1, 0, 0],
    },
    {
        "text": "You discover that your revenge trading always happens on mobile, never on desktop. Best use of this info?",
        "options": ["Delete the trading app from your phone entirely", "Create a rule: no trading from mobile, especially after losses, and uninstall the app during drawdowns", "It's just a coincidence — the platform isn't the problem", "Use mobile trading but only for take-profit, never entries"],
        "scores": [0, 1, 0, 0],
    },
    {
        "text": "You're reading about 'loss aversion' — the psychological principle that losses feel 2x more painful than equivalent gains feel good. How should this affect your trading?",
        "options": ["It shouldn't — knowing about the bias eliminates it", "It means you should use wider take-profits than stop-losses to make winners feel bigger", "Understanding it helps, but you need SYSTEMS (rules, limits, breaks) because awareness alone doesn't prevent emotional reactions", "It explains why trading is hard but doesn't change anything practically"],
        "scores": [0, 0, 1, 0],
    },
    {
        "text": "Your friend blew his account revenge trading and quit. He says 'trading isn't possible for normal people.' You think…",
        "options": ["He might be right — 90% of retail traders lose money", "He failed to build the psychological systems needed, not because trading is impossible", "He didn't have a good enough strategy", "Some people aren't cut out for trading — it's not for everyone"],
        "scores": [0, 1, 0, 0],
    },
    {
        "text": "You're considering hiring a therapist who specializes in performance psychology (used by athletes, surgeons, etc.). Is this overkill for a trader?",
        "options": ["Yes — trading psychology can be solved with better rules", "No — trading is a high-performance endeavor and professional support is a legitimate edge", "Only if you have serious emotional control issues", "Spend the money on a trading mentor instead — they understand the specific context better"],
        "scores": [0, 1, 0, 0],
    },
    {
        "text": "You've been revenge-free for 60 days. Then one terrible Tuesday, you snap and lose 4% chasing trades. This setback means…",
        "options": ["You're back to square one — 60 days of discipline meant nothing", "The 60 days proved you CAN do it — one slip doesn't erase progress, but it needs forensic analysis", "Your system isn't robust enough if one bad day can break it", "Trading psychology is a lifelong battle you'll never fully win"],
        "scores": [0, 1, 0, 0],
    },
    {
        "text": "A neuroscientist explains that after a financial loss, your amygdala activates the same threat response as physical danger. This means…",
        "options": ["Your revenge trades are literally 'fight or flight' responses — not rational decisions", "You should meditate more to calm the amygdala", "Trading is too stressful for the human brain", "Understanding the science makes you immune to the effect"],
        "scores": [1, 0, 0, 0],
    },
    {
        "text": "You create a 'red card' protocol: a physical red card sits on your desk. When you feel emotional, you turn it face-up. If the card is face-up, you're banned from entering ANY trades. How effective is this likely to be?",
        "options": ["Not effective — you'll just ignore the card when you're emotional", "Surprisingly effective — physical objects create psychological anchors, but ONLY if you pre-commit to honoring it", "Silly — professional traders don't need physical gimmicks", "Only useful as a short-term training tool"],
        "scores": [0, 1, 0, 0],
    },
    {
        "text": "After your worst revenge episode, you write down: 'I will NEVER revenge trade again.' Can you trust this commitment?",
        "options": ["Yes — hitting bottom creates lasting change", "No — commitments made during emotional peaks (positive or negative) rarely stick without structural changes", "Maybe — it depends on how painful the episode was", "Yes — if you write it down and sign it, it creates accountability"],
        "scores": [0, 1, 0, 0],
    },
    {
        "text": "You realize you enjoy the RUSH of revenge trading — the risk, the adrenaline, the potential for a big recovery. Is this enjoyment a problem?",
        "options": ["No — enjoying what you do improves performance", "Yes — you're not addicted to trading, you're addicted to gambling, and they're very different things", "Only if the enjoyment overrides your logic", "It's fine as long as your account is profitable overall"],
        "scores": [0, 1, 0, 0],
    },
    {
        "text": "You implement a rule: after ANY loss, you write 3 sentences in your journal before your next trade. After a month, you realize the rule has reduced your revenge trades by 70%. Why?",
        "options": ["Writing calms the mind", "The forced pause interrupts the amygdala's fight response and re-engages the prefrontal cortex", "Three sentences is the perfect amount of reflection", "You found a magic hack that works for everyone"],
        "scores": [0, 1, 0, 0],
    },
    {
        "text": "If you could pass ONE piece of advice about revenge trading to your trading past self, it would be…",
        "options": ["'The money you save by NOT revenge trading is more than you'll ever make from it'", "'Build systems that make revenge trading physically impossible, not just psychologically difficult'", "'Every revenge trade you take steals from future you'", "All three are equally valuable — pick the one that resonates with your specific trigger pattern"],
        "scores": [0, 0, 0, 1],
    },
    {
        "text": "You're on a 5-trade win streak. You feel invincible. You know intellectually that overconfidence is coming. What preemptive step can you take?",
        "options": ["Nothing — just keep trading normally until you naturally cool off", "Reduce position size slightly after a win streak as a counter-weight to overconfidence", "Take a break at 5 wins just like you would at 3 losses", "Remind yourself that win streaks end, then continue trading"],
        "scores": [0, 0, 1, 0],
    },
    {
        "text": "Your P&L for the year is breakeven. You feel 'stuck.' This emotional stuckness is making you consider taking bigger risks. The reality is…",
        "options": ["Breakeven in the first year of live trading is actually above average — most are negative", "Being stuck is a phase — bigger risks will accelerate you in one direction", "Breakeven means your system doesn't have an edge", "A year of data is enough to evaluate whether to continue"],
        "scores": [1, 0, 0, 0],
    },
    {
        "text": "You're in a group chat where someone just posted a $10,000 single-trade win. You're in a drawdown. The correct internal response?",
        "options": ["Congratulate them and move on — other people's results don't affect your edge", "Feel genuine happiness for them while recognizing that comparison is the thief of joy", "Leave the group temporarily — seeing big wins during a drawdown is unhealthy", "Use it as motivation to work harder on your own trading"],
        "scores": [0, 1, 0, 0],
    },
    {
        "text": "You've had a great 3 months and your confidence is high. You notice you're taking trades that 'almost' meet your criteria. The word 'almost' in trading usually means…",
        "options": ["Close enough — flexibility is a sign of experience", "The setup DOESN'T meet your criteria and 'almost' is overconfidence talking", "It qualifies as a B-setup, which can be taken at reduced risk", "Your eye for setups is improving and you see things you didn't before"],
        "scores": [0, 1, 0, 0],
    },
    {
        "text": "You revenge traded and then couldn't sleep. At 3am you're staring at the ceiling replaying the trade. The SINGLE most important thing to do tomorrow morning is…",
        "options": ["NOT TRADE — sleep deprivation combined with yesterday's emotional damage is a lethal combination", "Trade as normal — routine heals", "Journal the feelings and then trade smaller than usual", "Move yesterday's loss to 'tuition paid' column and start fresh"],
        "scores": [1, 0, 0, 0],
    },
    {
        "text": "An academic study shows that traders who take a mandatory 2-minute pause before every trade (winners or losers) outperform by 20%. You find this…",
        "options": ["Impractical — 2 minutes could mean missing the entry", "Completely believable — forced pauses prevent impulsivity, which IS the main edge destroyer", "Only relevant for scalpers — swing traders already have built-in pauses", "Interesting but academic research doesn't apply to real-world trading"],
        "scores": [0, 1, 0, 0],
    },
    {
        "text": "You set up your workspace to reduce revenge trading: clean desk, no phone, classical music, only your 4 charts visible. A friend laughs at the ritual. You should…",
        "options": ["Ignore him — environment design is used by every high performer from athletes to surgeons", "Acknowledge it seems excessive but it works for you", "Keep the setup but don't tell other traders about it", "Maybe he's right — if you need so many crutches, you're not psychologically ready to trade"],
        "scores": [1, 0, 0, 0],
    },
]
