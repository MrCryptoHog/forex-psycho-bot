"""
Question Bank — Part 6: Greed, Overconfidence & 'House Money' (80 questions)
"""

QUESTIONS_GREED = [
    {
        "text": "Your trade hits TP at +3R. You feel it could go further. You cancel the TP and hold. It reverses and you close at +1R. The key failure here was…",
        "options": ["Market reversal — nothing you could do", "Letting greed override a pre-planned exit. Once the TP is hit, the trade is OVER per your plan", "Setting the TP too conservatively in the first place", "Poor trade management after the TP was hit"],
        "scores": [0, 1, 0, 0],
    },
    {
        "text": "You're up 12% this month. Your average is 3-4%. You start thinking about how to make it 15% before month-end. This thinking is…",
        "options": ["Ambitious — always push for your best possible month", "Greed masquerading as ambition. 12% is 3-4x your average. Protecting it should be the priority", "Healthy goal-setting — reach for the next level", "Fine as long as you don't increase risk"],
        "scores": [0, 1, 0, 0],
    },
    {
        "text": "You discover a strategy that produces 8% per month on a demo account. You immediately max out your live account leverage to replicate it. The problem?",
        "options": ["Demo performance rarely translates 1:1 to live due to execution differences AND emotional factors. Start with 25% of demo size", "Nothing — if it works on demo, it should work live", "You should at least do 3 more months of demo first", "The strategy is too aggressive for live trading"],
        "scores": [1, 0, 0, 0],
    },
    {
        "text": "Your account has doubled in 6 months. You withdraw NOTHING. A mentor suggests withdrawing 30% of profits regularly. Why?",
        "options": ["No need — compounding is more powerful than withdrawing", "Withdrawals convert digital numbers into REAL money, which recalibrates your brain's understanding of what's at stake", "Withdrawals slow down account growth", "Only withdraw when you need the money"],
        "scores": [0, 1, 0, 0],
    },
    {
        "text": "A trade is in heavy profit. Your TP is 10 pips away. You think: 'Let me move the TP 20 pips higher — it has momentum.' This last-minute TP change is usually…",
        "options": ["Smart — momentum suggests it'll keep going", "A greed-driven decision that turns wins into smaller wins or breakevens. The original TP was set without emotional contamination", "Fine if momentum analysis supports it", "Acceptable if you trail your stop to protect most of the profit"],
        "scores": [0, 1, 0, 0],
    },
    {
        "text": "You've withdrawn profits and bought yourself a nice watch. Now you want to 'make the watch money back' from trading. This 'making back' mentality is…",
        "options": ["Motivated — gives you a clear target", "A form of mental accounting that treats withdrawn profits differently than account equity — it creates unnecessary pressure", "Normal — everyone wants to replace what they spent", "Smart — having concrete goals improves focus"],
        "scores": [0, 1, 0, 0],
    },
    {
        "text": "You size up to 3% risk on one particular trade because 'this setup is rare and I need to capitalize.' This logic fails because…",
        "options": ["3% is fine for rare, high-quality setups", "You don't know it's a winner in advance. The rarity of the setup doesn't change the probability that THIS instance could be the one that fails", "Rare setups should actually be traded at lower risk since you have less data on them", "You're overvaluing the setup due to recency bias"],
        "scores": [0, 1, 0, 0],
    },
    {
        "text": "You're in a trade group and everyone is posting massive gains from a news event. You missed it. You feel like you 'need to make up for lost opportunity.' This need is…",
        "options": ["Healthy FOMO that drives you to be more prepared next time", "Comparison-driven greed — those are THEIR trades, not yours. Missing opportunity has zero impact on your account", "Motivating — it shows you want to improve", "A sign you need a better news trading strategy"],
        "scores": [0, 1, 0, 0],
    },
    {
        "text": "Your strategy generates 3% monthly. You encounter a 'guru' selling a system that claims 15% monthly. You're tempted. The greed-check question to ask is…",
        "options": ["What's their verified track record?", "If 15% monthly were real and sustainable ($1,000 becomes $5.3M in 5 years), why are they selling a course instead of managing a hedge fund?", "How much does the course cost?", "Can I demo-test it before buying?"],
        "scores": [0, 1, 0, 0],
    },
    {
        "text": "Your trade is at +5R. You've NEVER had a +5R winner before. The round number psychology makes you want to hold for +6R to 'set a record.' This impulse is…",
        "options": ["A sign of ambition — new personal bests drive growth", "The market doesn't care about your personal records. Holding for ego-driven targets is greed dressed as ambition", "Reasonable if the trade is still showing momentum", "Fine if you move your stop to +4.5R to protect the profit"],
        "scores": [0, 1, 0, 0],
    },
    {
        "text": "You made $10,000 this month. Your monthly expenses are $3,000. Instead of withdrawing, you leave it all in the account because 'bigger account = bigger gains.' The risk is…",
        "options": ["No risk — compounding is the path to wealth", "A drawdown now risks not just profits but your LIVING EXPENSES. The extra capital creates lifestyle-dependent risk", "Minimal if your risk management is solid", "You should keep at least 3 months expenses outside the account — the rest can compound"],
        "scores": [0, 0, 0, 1],
    },
    {
        "text": "Your account hit $100,000 for the first time. You feel the urge to take a 'big trade' to celebrate. Celebration trades are…",
        "options": ["Fun — nothing wrong with a celebratory trade if it's a valid setup", "Emotionally motivated and violate the principle of identical execution regardless of account balance", "Fine at reduced risk", "A reward you've earned — take it"],
        "scores": [0, 1, 0, 0],
    },
    {
        "text": "You're scalping and up $500 for the day. Your plan says stop at 3 trades. You're at 3, all winners. 'One more' feels harmless. The 4th trade…",
        "options": ["Is fine — you're hot and the system is working", "Has the same probability as any other trade, but your decision to take it was driven by greed, not your system", "Is low risk since you have a $500 buffer", "Is smart — capitalize on positive momentum"],
        "scores": [0, 1, 0, 0],
    },
    {
        "text": "You allocate 70% of your savings to forex trading. A financial advisor would say this is excessive. Your response is 'but I'm a good trader.' This confidence is…",
        "options": ["Justified if you have consistent results over 2+ years", "Dangerous — even good traders have bad years. 70% allocation to a single volatile asset class is poor diversification", "Fine if your other 30% covers emergencies", "Your money, your decision — more capital means more profit"],
        "scores": [0, 1, 0, 0],
    },
    {
        "text": "You hold 3 positions overnight. Morning gap takes all 3 to profit. You feel 'lucky' and enter 3 MORE positions on the same day. Taking extra trades because you feel lucky is…",
        "options": ["Capitalizing on a good day", "The gambler's fallacy — luck isn't a resource that carries over from past trades to future ones", "Fine if the new setups are valid", "Smart — some days the market is just 'your day'"],
        "scores": [0, 1, 0, 0],
    },
    {
        "text": "Your funded account payout is $5,000. You were hoping for $10,000. Instead of being satisfied with $5,000, you feel disappointed. This is an example of…",
        "options": ["Low expectations — you should have performed better", "Hedonic adaptation and expectation anchoring — your brain moved the goalpost from '$0' to '$10,000', making $5,000 feel like a loss", "Normal — you're driven to achieve more", "A sign you should push harder next month"],
        "scores": [0, 1, 0, 0],
    },
    {
        "text": "You're breakeven after 6 months. A voice says 'I need to double my risk to make the account grow faster.' The voice of reason responds…",
        "options": ["Double the risk — breakeven at 1% means profitable at 2%", "Breakeven means your system WORKS but might need refinement. Doubling risk doesn't improve a system — it magnifies whatever it already does", "Try 1.5% as a middle ground", "If you're breakeven, the edge might not exist"],
        "scores": [0, 1, 0, 0],
    },
    {
        "text": "You see a pair move 200 pips in a day. You calculate: 'If I'd been in that with full leverage, I'd have made $20,000.' This kind of hypothetical calculation is…",
        "options": ["Useful for understanding potential", "Toxic — 'if only' math with full leverage ignores the 50% chance it goes the other way, and it normalizes unrealistic expectations", "Good motivation for catching the next big move", "A realistic assessment of the opportunity you missed"],
        "scores": [0, 1, 0, 0],
    },
    {
        "text": "You add a second income stream (copytrading subscribers). Now each trade affects not just your account but your subscribers' accounts. You notice you're…",
        "options": ["More careful — responsibility improves discipline", "Taking smaller risks to avoid subscriber complaints, which ironically reduces system performance", "Trading the same — a trade is a trade", "More stressed, which might hurt decision-making"],
        "scores": [0, 0, 0, 1],
    },
    {
        "text": "Your system generates 20 trades per month. You want more money, so you add 3 new pairs to trade, doubling to 40 trades. The issue is…",
        "options": ["More trades = more profit if the system works", "Adding pairs without backtesting dilutes your edge with unknown-expectancy trades. More trades ≠ more profit", "Your time and attention are now split across too many pairs", "40 trades is a reasonable monthly total"],
        "scores": [0, 1, 0, 0],
    },
    {
        "text": "You're consistently profitable at 3% monthly. Someone offers to give you $500,000 to trade for a 50/50 profit split. You should consider…",
        "options": ["Take it immediately — 50% of 3% monthly on $500K is $7,500/month", "WHETHER you can trade someone else's money with the same psychology. Many traders trade differently with OPM, and the pressure destroys their edge", "Only if they accept your drawdown parameters", "Negotiate a 70/30 split since YOU have the skill"],
        "scores": [0, 1, 0, 0],
    },
    {
        "text": "You're in profit on a trade and your broker shows the floating P&L in green. You feel good. Research shows that real-time P&L displays on trades…",
        "options": ["Are helpful — you need to know your position status", "Increase emotional attachment to the outcome and make traders more likely to exit early (to lock green) or hold too long (to avoid seeing red)", "Are neutral — professionals ignore them", "Should be checked frequently to manage risk"],
        "scores": [0, 1, 0, 0],
    },
    {
        "text": "You hit your annual target of +30% by October. 2 months remain. Your options: (A) stop trading for the year, (B) continue normally, (C) increase risk. The greed-free choice is…",
        "options": ["C — you're playing with house money now", "B — continue your normal process. The annual target is a milestone, not a signal to change behavior", "A — protect the gains and start fresh in January", "C — but only slightly increase risk"],
        "scores": [0, 1, 0, 0],
    },
    {
        "text": "You find yourself constantly checking your equity and mentally converting it to things you could buy. 'That's a new laptop. That's a vacation.' This habit…",
        "options": ["Motivates you — tangible goals are powerful", "Makes losses feel like losing the laptop or vacation, creating emotional pain that distorts trading decisions", "Keeps you grounded in what the money means in the real world", "Is fine as long as you don't withdraw impulsively"],
        "scores": [0, 1, 0, 0],
    },
    {
        "text": "A prop firm offers you a $200K account. Your current $20K account makes you 3% monthly ($600). On $200K at 3%, that's $6,000. You start imagining the $6,000. The danger is…",
        "options": ["No danger — it's basic math", "Fantasizing about the income creates performance pressure that may change your trading behavior on the funded account", "You should be excited — this is a great opportunity", "The only danger is not passing the challenge"],
        "scores": [0, 1, 0, 0],
    },
    {
        "text": "You're about to close a trade at +2R (your target). Suddenly the trade shoots up in your favor. You cancel the close and hold. It comes back to +1.5R and you finally close. What did greed cost you?",
        "options": ["Nothing significant — you still made +1.5R", "+0.5R on THIS trade, but more importantly, it reinforced the habit of canceling exits, which will cost much more over time", "It's just part of trade management — some go higher, some don't", "The TP was hit — you should have let the system handle it"],
        "scores": [0, 1, 0, 0],
    },
    {
        "text": "You're net profitable but notice that 90% of your worst trades have one thing in common: you sized up. This data tells you…",
        "options": ["Your sizing isn't the problem — those trades just happened to lose", "Sizing up changes your psychology. Larger positions create more emotional interference, degrading decision quality", "Stay at one size and your results will improve", "Only size up after extensive backtesting of variable sizing"],
        "scores": [0, 1, 0, 0],
    },
    {
        "text": "If greed had a trading journal entry, it would read…",
        "options": ["'Great analysis today — let's increase size for tomorrow since I'm on a roll'", "'The TP was too conservative. I changed it mid-trade because I KNEW it was going further. (It didn't.) But next time it will.'", "'Time to scale up — I've earned it'", "'One more trade won't hurt — I'm already in profit'"],
        "scores": [0, 1, 0, 0],
    },
    {
        "text": "You tell yourself: 'I'll trade aggressively until I hit $50K, then I'll trade conservatively.' The problem with this approach?",
        "options": ["Nothing — having a target for risk reduction is smart", "The aggressive phase will likely PREVENT you from reaching $50K because higher risk amplifies drawdowns that reset progress", "You might not be able to switch to conservative after being aggressive", "It's fine if you can handle the volatility"],
        "scores": [0, 1, 0, 0],
    },
    {
        "text": "You're reading about compound interest. 1% daily turns $1,000 into $1.4 million in 2 years. You think 'I just need 1% a day.' The reality is…",
        "options": ["Difficult but possible with the right strategy", "This math ignores drawdowns, variance, and the psychological impossibility of consistent daily gains. It's a fantasy that drives dangerous risk-taking", "Achievable with solid discipline and A+ setups only", "A good long-term target to work toward gradually"],
        "scores": [0, 1, 0, 0],
    },
    {
        "text": "You have a $10K account and want to make $100K from it this year. For that to happen at 1% risk per trade, you'd need roughly…",
        "options": ["To be very skilled — it's achievable", "To turn $10K into $100K (10x) in one year, which mathematically requires enormous risk or unrealistic consistency. This goal creates pressure for reckless trading", "A great strategy and strong discipline", "Full-time dedication and market access 24/5"],
        "scores": [0, 1, 0, 0],
    },
    {
        "text": "You're at a party and someone asks 'how much do you make trading?' You inflate the number or highlight your best month. Why is this socially-driven exaggeration harmful to YOUR trading?",
        "options": ["It's just socializing — everyone embellishes", "It creates an external identity you feel pressure to maintain, leading to risk-taking to match the inflated narrative", "It's harmless — what you say at parties doesn't affect trading", "It's good marketing if you want to attract investors"],
        "scores": [0, 1, 0, 0],
    },
    {
        "text": "You finally understand compounding, risk management, and psychology. You realize getting rich from trading is a 5-10 year process, not a 6-month sprint. You feel…",
        "options": ["Disappointed — you thought it would be faster", "Clarity — this realistic timeline actually reduces psychological pressure and improves decision-making by removing the urgency that fuels greed", "Motivated — long-term thinking is your edge", "Impatient — 5-10 years is a long time"],
        "scores": [0, 1, 0, 0],
    },
    {
        "text": "You're trading a funded account and your monthly profit reaches the payout threshold on the 15th. 15 days remain. You start 'playing it safe' to protect the payout. This behavior shift is…",
        "options": ["Smart — secure the payout and coast", "Changing your strategy mid-month based on P&L, which is the SAME behavioral problem as increasing risk when losing", "Conservative but prudent", "What any rational person would do"],
        "scores": [0, 1, 0, 0],
    },
    {
        "text": "Your unrealized profit just crossed $1,000 for the first time on a single trade. You feel a rush. The mature response to this rush is…",
        "options": ["Celebrate — you earned it", "Notice the feeling, log it, and follow your exit plan exactly as if the P&L said $100", "Lock in the profit — $1,000 is meaningful money", "Feel the rush and use the energy to find your next trade"],
        "scores": [0, 1, 0, 0],
    },
    {
        "text": "You just had your best quarter ever: +22%. A mentor helps you realize that 15% of that was from ONE outsized winning trade. Without it, you'd be at +7%. This matters because…",
        "options": ["It doesn't — a win is a win, and 22% is your result", "Relying on outlier trades for overall performance means your base system is producing 7% — the rest was luck, and planning for outliers is planning for disappointment", "+7% quarterly is still excellent — the outlier was a bonus", "Now you know what kind of trades to look for more of"],
        "scores": [0, 1, 0, 0],
    },
    {
        "text": "Every time you're about to exit at your planned TP, you think 'but Twitter/telegram traders say to let winners run.' This conflict between your plan and internet advice creates…",
        "options": ["A valid point — maybe your TPs are too tight", "Decision paralysis that usually ends in worse outcomes. YOUR plan was made without emotional interference; Twitter advice doesn't know your system", "A good reason to re-evaluate your exit strategy", "Helpful diverse perspective on trade management"],
        "scores": [0, 1, 0, 0],
    },
    {
        "text": "You notice that after withdrawal, you trade more aggressively because the account 'feels smaller.' This post-withdrawal aggression is…",
        "options": ["Your brain trying to 'rebuild' the account back to its pre-withdrawal level — treating your own withdrawals as losses", "Normal — smaller accounts need higher returns to produce the same dollar amount", "Not a problem if you quickly return to normal sizing", "A reason to withdraw less frequently"],
        "scores": [1, 0, 0, 0],
    },
    {
        "text": "You're offered a choice: (A) guaranteed $1,000 or (B) 50% chance of $2,500, 50% chance of $0. Most traders pick A even though B has higher expected value ($1,250). This preference reveals…",
        "options": ["A is the smarter choice — guaranteed money is always better", "Risk aversion with gains — you prefer certainty when money is on the table, even at the cost of EV", "B is too risky for most people", "A bird in the hand is worth two in the bush — old wisdom"],
        "scores": [0, 1, 0, 0],
    },
    {
        "text": "Now flip it: (A) guaranteed LOSS of $1,000 or (B) 50% chance of losing $2,500, 50% chance of losing $0. Most traders pick B. This reveals…",
        "options": ["B gives a chance to avoid the loss entirely — it's rational", "Risk-seeking with losses — the same person who was risk-averse with gains becomes a gambler to avoid a sure loss. This is why traders hold losers and cut winners", "A guaranteed loss should always be avoided if possible", "Both choices are bad — B at least gives hope"],
        "scores": [0, 1, 0, 0],
    },
    {
        "text": "The antidote to trading greed is NOT 'wanting less money.' It's actually…",
        "options": ["Contentment with moderate returns", "Having such clear position sizing and exit rules that greed literally has no mechanism to express itself in your trading", "Meditation and mindfulness", "Focusing on process instead of profits"],
        "scores": [0, 1, 0, 0],
    },
]
