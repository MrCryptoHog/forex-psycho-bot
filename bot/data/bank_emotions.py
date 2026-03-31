"""
Question Bank — Part 5: Emotional Control & Awareness (100 questions)
"""

QUESTIONS_EMOTIONS = [
    {
        "text": "You feel euphoric after 5 consecutive wins. Your next setup looks 'perfect.' The emotionally intelligent response is…",
        "options": ["Trust the euphoria — you're in the zone and seeing clearly", "Recognize euphoria as a signal that your risk assessment is compromised — treat the next trade with EXTRA scrutiny", "Ride the wave — momentum in confidence is real", "Take the trade but at half size to account for potential overconfidence"],
        "scores": [0, 1, 0, 0],
    },
    {
        "text": "You wake up angry about something unrelated to trading (argument with a family member). You sit down to trade the London open. Honestly, your decision-making is…",
        "options": ["Unaffected — I compartmentalize well", "Almost certainly compromised — anger narrows attention and increases risk-taking in ALL domains, not just the source", "Maybe slightly affected, but once I see a chart I focus", "Better when angry — the intensity sharpens my analysis"],
        "scores": [0, 1, 0, 0],
    },
    {
        "text": "Mid-trade, you feel your heart racing and palms sweating. This is happening because your position is at -0.8R. These physical symptoms tell you…",
        "options": ["You're in a high-stakes situation — stay focused and ride it out", "Your sympathetic nervous system is activated, meaning your brain is in threat mode. Decision-making quality is degraded RIGHT NOW", "It's normal adrenaline — all traders feel this", "You need to close the trade immediately to stop the stress"],
        "scores": [0, 1, 0, 0],
    },
    {
        "text": "You traded perfectly today: 2 winners, process was flawless. But you feel EMPTY instead of satisfied. This emotional blunting might indicate…",
        "options": ["You've achieved the ideal state — emotional detachment from results", "Burnout or emotional exhaustion from trading — even good days feel hollow when you've been grinding too hard", "Nothing — not every win needs to feel exciting", "You expected bigger wins and are subconsciously disappointed"],
        "scores": [0, 1, 0, 0],
    },
    {
        "text": "You notice that on Mondays you feel anxious about the week ahead, and on Fridays you feel pressure to 'finish strong.' These patterns suggest…",
        "options": ["Normal weekly emotional cycles — everyone has them", "Your emotional state is being driven by the calendar rather than market conditions, which adds noise to your trading", "Nothing actionable — feelings come and go", "You should only trade mid-week when you're most neutral"],
        "scores": [0, 1, 0, 0],
    },
    {
        "text": "Your trading mentor says: 'The goal isn't to eliminate emotions — it's to prevent emotions from altering your behavior.' This means…",
        "options": ["Feel the fear and trade anyway", "You can be scared, frustrated, or excited — but your ACTIONS (entries, exits, sizing) must remain consistent regardless", "Suppress your emotions during market hours", "Emotions are information — use them to make better trades"],
        "scores": [0, 1, 0, 0],
    },
    {
        "text": "After a big loss, you find yourself snapping at your partner, eating junk food, and staying up late. These behaviors suggest…",
        "options": ["You had a bad day — everyone copes differently", "Trading losses are spilling into your personal life, which means your risk is beyond your emotional capacity", "Unrelated — sometimes people have bad nights", "You need better work-life boundaries"],
        "scores": [0, 1, 0, 0],
    },
    {
        "text": "You keep a daily mood score (1-10) in your trading journal. After 6 months, you discover you lose money on days when your mood is above 8 OR below 4. This data suggests…",
        "options": ["Only trade when your mood is between 4-8 — extreme emotional states impair trading", "Mood doesn't affect trading — correlation isn't causation", "You should always aim for a mood of 6-7 before trading", "High mood days should be traded at reduced risk"],
        "scores": [1, 0, 0, 0],
    },
    {
        "text": "You're managing a trade and feel the URGE to check it every 30 seconds. This compulsive checking behavior is driven by…",
        "options": ["Responsible trade management — you should monitor open positions", "Anxiety — the frequent checking doesn't change the outcome, it just feeds your nervous system's need for information during uncertainty", "Normal behavior for short-term trades", "Fear of a sudden adverse move — better safe than sorry"],
        "scores": [0, 1, 0, 0],
    },
    {
        "text": "You just had a trade go from -1R to +3R in minutes. The emotional whiplash (despair → euphoria) leaves you feeling wired. Before your next trade, you should…",
        "options": ["Trade immediately — you're energized and might catch the next move", "Wait at least 15-30 minutes — emotional whiplash puts your nervous system in a reactive state that impairs judgment", "Open the next trade at normal size — the previous trade is over", "Take a shorter break — 5 minutes is enough"],
        "scores": [0, 1, 0, 0],
    },
    {
        "text": "You overhear a conversation: 'Real traders don't feel anything. If you're emotional, you're not cut out for this.' Your response?",
        "options": ["He's right — emotional control means feeling nothing", "That's toxic nonsense — even the best traders feel emotions. The skill is having systems that prevent emotions from altering behavior", "Partially true — you need to become numb to losses over time", "Agree — if you can't control your emotions, find a different career"],
        "scores": [0, 1, 0, 0],
    },
    {
        "text": "You notice you trade better after exercise. Your best months all followed periods of consistent gym activity. This connection exists because…",
        "options": ["Coincidence — exercise and trading are unrelated", "Exercise improves prefrontal cortex function, reduces cortisol, and increases emotional regulation — it literally upgrades your trading hardware", "You feel more confident after working out, and confidence helps trading", "The routine of exercise transfers to trading discipline"],
        "scores": [0, 1, 0, 0],
    },
    {
        "text": "A trade you've been planning all week finally sets up. You enter and immediately feel doubt. 'What if I'm wrong?' This doubt is…",
        "options": ["A warning signal — maybe your analysis is flawed", "Normal — doubt after entry is universal. The key is whether it changes your behavior or you follow the plan regardless", "A sign you should have waited for more confirmation", "Your subconscious detecting something you missed"],
        "scores": [0, 1, 0, 0],
    },
    {
        "text": "You've been staring at charts for 6 hours straight. Your eyes are tired, you've missed lunch, and you're irritable. The quality of your analysis right now is…",
        "options": ["Fine — you're experienced enough to trade through fatigue", "Significantly degraded — cognitive fatigue reduces pattern recognition, impulse control, and emotional regulation", "Slightly lower but you can compensate by being more careful", "Actually better — extended focus creates 'flow state'"],
        "scores": [0, 1, 0, 0],
    },
    {
        "text": "You feel RELIEF after closing a trade, even when it's a winner. If closing trades always brings relief rather than satisfaction, it might mean…",
        "options": ["You're managing risk well — relief means you were aware of the risk", "Your position size or trading style creates more anxiety than enjoyment — the activity is emotionally net-negative", "Relief is a normal emotion after uncertainty resolves", "You're not passionate enough about trading"],
        "scores": [0, 1, 0, 0],
    },
    {
        "text": "You meditate for 10 minutes before trading each morning. Some days you skip it. You notice your win rate is 12% higher on meditation days. This is likely because…",
        "options": ["Meditation magically improves trading", "Meditation reduces amygdala reactivity and improves prefrontal cortex engagement — you literally make better decisions", "You trade more cautiously after meditation, which biases toward winners", "Correlation — the meditation days might just be calmer market days too"],
        "scores": [0, 1, 0, 0],
    },
    {
        "text": "Your significant other says: 'You're a different person when you're losing in the market.' This feedback is…",
        "options": ["An exaggeration — trading doesn't change who you are", "Critical data — if losses change your personality visibly, the emotional impact is way beyond what your risk management should allow", "Normal — everyone gets stressed about money", "A sign you should keep trading results private"],
        "scores": [0, 1, 0, 0],
    },
    {
        "text": "You feel BORED during a profitable month because the trades are slow and predictable. Boredom makes you want to trade more. Boredom in trading is…",
        "options": ["A sign you need more excitement — consider a faster trading style", "A sign of doing it RIGHT — profitable trading SHOULD be boring. The desire for excitement is a threat to your P&L", "Normal — just find other activities to stay stimulated", "Dangerous — bored traders make mistakes"],
        "scores": [0, 1, 0, 0],
    },
    {
        "text": "You're reviewing your journal and notice an emotional pattern: hope → anxiety → regret → revenge → hope. This cycle occurs every losing streak. To break it, you need to…",
        "options": ["Identify the transition point between 'anxiety' and 'regret' — that's where the behavioral trigger lives", "Address each emotion separately with a different strategy", "Accept that the cycle is natural and just manage the 'revenge' stage", "Stop trading during losing streaks entirely"],
        "scores": [1, 0, 0, 0],
    },
    {
        "text": "You feel GUILTY for making money on a trade that went against what most people expected. This guilt is…",
        "options": ["A sign of empathy — it shows you care about others' outcomes", "Irrational — trading is a zero-sum game and your profit doesn't cause others' losses in forex", "Worth exploring — guilt can prevent you from taking full advantage of your edge", "Normal for ethical traders who think about market impact"],
        "scores": [0, 0, 1, 0],
    },
    {
        "text": "You just made $5,000 on a single trade. You feel invincible. A psychologically mature trader would…",
        "options": ["Celebrate and use the confidence for the next trade", "Acknowledge the feeling of invincibility, recognize it as a RISK FACTOR, and follow the exact same process on the next trade", "Scale up position size while the hot streak lasts", "Take the rest of the day off to lock in the win"],
        "scores": [0, 1, 0, 0],
    },
    {
        "text": "You notice you make your worst decisions between 2-4pm (your local time). This time-based pattern could be caused by…",
        "options": ["Market conditions are worse in the afternoon", "Post-lunch cortisol dip combined with decision fatigue from the morning session — your biology is working against you", "Coincidence — time of day doesn't affect decision quality", "You're rushed to finish before market close"],
        "scores": [0, 1, 0, 0],
    },
    {
        "text": "You feel NOTHING after a loss. Complete flatline. You tell yourself this is 'emotional mastery.' But it could also be…",
        "options": ["True emotional mastery — you've trained yourself to be stoic", "Emotional suppression or dissociation — you're not processing losses, you're burying them, which will erupt later", "The sign of an experienced trader who's seen enough losses", "The ideal state — no emotions means no emotional trading errors"],
        "scores": [0, 1, 0, 0],
    },
    {
        "text": "Your trading performance drops significantly when you're sleep-deprived (less than 6 hours). This is because…",
        "options": ["You're just not a morning person", "Sleep deprivation impairs the prefrontal cortex while amplifying amygdala reactivity — rational control decreases while emotional reactivity increases", "Less sleep means less focus on charts", "Everyone performs worse when tired — it's not specific to trading"],
        "scores": [0, 1, 0, 0],
    },
    {
        "text": "You feel ENVIOUS of traders who seem to make money effortlessly. This envy, if unexamined, will likely lead you to…",
        "options": ["Work harder to match their results — healthy motivation", "Strategy-hop, copy others' trades, and abandon your own edge — all in pursuit of their perceived ease", "Push yourself to improve, which is positive", "Nothing — envy is a passing emotion"],
        "scores": [0, 1, 0, 0],
    },
    {
        "text": "You started trading to escape a job you hate. On losing days, you think 'I'll never escape.' This emotional connection between trading and freedom creates…",
        "options": ["Healthy motivation to succeed", "Excessive emotional attachment to outcomes — every loss feels like losing your dream, not just money", "A powerful 'why' that drives discipline", "Normal pressure that comes with ambitious goals"],
        "scores": [0, 1, 0, 0],
    },
    {
        "text": "A friend sends you a screenshot of his massive loss and says 'I feel fine.' He immediately enters another trade. He probably…",
        "options": ["Has strong emotional control", "Is in emotional denial — 'feeling fine' immediately after a massive loss is a red flag for suppression, not mastery", "Has developed healthy detachment from outcomes", "Has a big enough account that the loss doesn't matter"],
        "scores": [0, 1, 0, 0],
    },
    {
        "text": "You create a 'feelings log' that tracks emotions before, during, and after each trade. After 100 entries, the most actionable insight is likely…",
        "options": ["Which emotions correlate with your best trades", "The specific emotional STATE that precedes your worst decisions — giving you a personal early warning system", "How your emotions change throughout the day", "Whether positive or negative emotions produce better results"],
        "scores": [0, 1, 0, 0],
    },
    {
        "text": "You realize your BEST trades happen when you feel slightly nervous but not panicked. Your WORST trades happen when you feel either very confident or very anxious. This is an example of…",
        "options": ["The Yerkes-Dodson law — performance peaks at moderate arousal, not at extremes", "Coincidence — emotions don't have that precise an effect", "Your specific psychological profile — everyone is different", "Normal variation in trading outcomes"],
        "scores": [1, 0, 0, 0],
    },
    {
        "text": "You're having a fantastic day: +3 winning trades. You feel great. Then the 4th trade loses -1R. The loss feels MUCH worse than a normal -1R loss. This amplified pain is because…",
        "options": ["The loss broke your streak — streak-breaking losses always feel worse", "Contrast effect — the emotional high from 3 wins created a baseline from which the loss feels like a bigger drop", "You expected the streak to continue and the loss felt 'unfair'", "-1R is a meaningful amount of money to you"],
        "scores": [0, 1, 0, 0],
    },
    {
        "text": "You trade better when listening to specific music. This isn't coincidence — what's actually happening?",
        "options": ["Music improves pattern recognition", "Music regulates your arousal level — the right music puts you in an optimal emotional state for decision-making", "You just enjoy trading more with music, and enjoyment improves focus", "The music drowns out distracting thoughts"],
        "scores": [0, 1, 0, 0],
    },
    {
        "text": "After a loss, you feel the urge to tell someone about it. You text a trading friend: 'Just got stopped out.' This urge to share serves what psychological purpose?",
        "options": ["Seeking validation that the loss wasn't your fault", "Emotional co-regulation — sharing distressing experiences with others helps your nervous system return to baseline", "Building accountability in your trading group", "Procrastinating before having to analyze the loss"],
        "scores": [0, 1, 0, 0],
    },
    {
        "text": "You've been trading for 3 years and notice you no longer feel excited about wins OR upset about losses. Everything is flat. Is this good or bad?",
        "options": ["Good — emotional neutrality is the goal", "Worth examining — complete emotional flatness could indicate healthy desensitization OR it could indicate depression, burnout, or loss of passion. Know the difference", "Bad — you should still feel something", "Good for trading, potentially bad for life"],
        "scores": [0, 1, 0, 0],
    },
    {
        "text": "You feel ANXIOUS about entering a valid setup even though your system has a proven edge. The anxiety likely comes from…",
        "options": ["A healthy respect for risk", "Uncertainty aversion — your brain craves certainty and trading can never provide it, so entry always feels threatening", "Your position size being too large", "Fear of a losing streak continuing"],
        "scores": [0, 1, 0, 0],
    },
    {
        "text": "You notice your mood directly mirrors your open P&L throughout the day. Up = happy, down = anxious. This means…",
        "options": ["You're emotionally invested in your trading, which drives performance", "Your emotional state is being outsourced to the market. This is unsustainable and leads to reactive decision-making", "It's natural to feel good when winning and bad when losing", "You need to check P&L less frequently"],
        "scores": [0, 1, 0, 0],
    },
    {
        "text": "A book recommends 'deep breathing exercises' before every trade entry. This seems silly for a 'serious' trader. Actually, it works because…",
        "options": ["The breathing calms you down", "Controlled breathing activates the parasympathetic nervous system, literally shifting your brain from 'reactive' to 'analytical' mode", "It forces a pause between analysis and execution", "The placebo effect — if you believe it works, it works"],
        "scores": [0, 1, 0, 0],
    },
    {
        "text": "You're in a trade that's at +2R. You feel FEAR that you'll give back the gains. This 'fear of giving back' is…",
        "options": ["Smart — lock in the profit before it disappears", "Loss aversion activated on unrealized gains — you're treating paper profit as 'yours' and the prospect of losing it triggers the same fear as real loss", "A valid reason to close the trade early", "Normal and manageable — just follow your plan"],
        "scores": [0, 1, 0, 0],
    },
    {
        "text": "You find yourself 'negotiating' with the market: 'If this trade works out, I'll follow my rules from now on.' This bargaining is…",
        "options": ["Harmless self-talk — everyone does it", "A sign of magical thinking and desperation. The market doesn't negotiate. This mindset delays the real work of building discipline", "A way of making commitments during emotional moments", "Motivational — conditional promises can drive behavior change"],
        "scores": [0, 1, 0, 0],
    },
    {
        "text": "You feel SHAME after a losing trade, even when it was a valid setup executed perfectly. The shame comes from…",
        "options": ["Taking responsibility for your losses — admirable trait", "Linking your self-worth to trade outcomes rather than trade PROCESS — this is a toxic belief system that must be dismantled", "Natural disappointment that your analysis was wrong", "Caring deeply about your performance"],
        "scores": [0, 1, 0, 0],
    },
    {
        "text": "Your dog died yesterday. Today you 'need' to trade to distract yourself from grief. Trading as a distraction from grief is…",
        "options": ["Healthy — keeping busy helps with grieving", "Dangerous — grief impairs cognitive function, emotional regulation, and attention. You're seeking distraction, not making good trades", "Fine if you reduce position size", "A personal decision — some people process grief better when active"],
        "scores": [0, 1, 0, 0],
    },
    {
        "text": "You feel COMFORTABLE taking trades but UNCOMFORTABLE during drawdowns. This distinction reveals…",
        "options": ["Normal risk tolerance — entries feel good, losses feel bad", "You've mastered entry discipline but haven't built the emotional infrastructure for sustained adversity", "Good self-awareness — most traders feel the same", "Nothing unusual — drawdowns are universally uncomfortable"],
        "scores": [0, 1, 0, 0],
    },
    {
        "text": "After reading about cognitive biases in trading, you believe you're now immune to them because you 'know about them.' The truth is…",
        "options": ["Knowledge IS power — knowing about biases helps you avoid them", "Knowing about biases reduces their effect by maybe 20%. The remaining 80% requires SYSTEMS (rules, automation, external checks) because biases are neurological, not intellectual", "Understanding biases is the most important step — practice follows naturally", "You can't really overcome biases, just manage them"],
        "scores": [0, 1, 0, 0],
    },
    {
        "text": "You feel ANGRY at yourself for a rule violation. You punish yourself by 'sitting out' the next 3 trading days. Self-punishment as a discipline tool is…",
        "options": ["Effective — consequences teach lessons", "Counterproductive — anger at yourself creates shame spirals. Structured logical consequences (like reduced size) are better than emotional punishment", "The right amount of severity — 3 days is fair", "Necessary sometimes — people need to learn from pain"],
        "scores": [0, 1, 0, 0],
    },
    {
        "text": "You feel GRATITUDE on winning days and VICTIMHOOD on losing days. This polarized emotional response means…",
        "options": ["You're just honest about your feelings", "You're attributing wins to your skill and losses to external factors — a bias called self-serving attribution that prevents learning", "Normal — everyone feels this way", "At least you feel grateful for wins — many traders don't"],
        "scores": [0, 1, 0, 0],
    },
    {
        "text": "A therapist tells you to 'name your emotions while trading.' She says: 'I feel anxious' instead of just feeling anxious without labeling it. This technique works because…",
        "options": ["It's just mindfulness jargon — doesn't change anything", "Naming an emotion activates the prefrontal cortex and reduces amygdala activity — putting feelings into words literally changes brain chemistry", "It forces you to pause, which is the real benefit", "It's only useful for people who struggle with emotional awareness"],
        "scores": [0, 1, 0, 0],
    },
    {
        "text": "You feel LONELY as a solo trader. No office, no colleagues, no feedback. This loneliness affects your trading by…",
        "options": ["It doesn't — trading is inherently solitary", "Increasing the emotional weight of each trade because there's no social support system for processing wins and losses", "Forcing you to be more self-reliant, which is good", "Making you trade more frequently to 'feel connected' to the market"],
        "scores": [0, 1, 0, 0],
    },
    {
        "text": "You're EXCITED about a new setup forming. Excitement before a trade entry is…",
        "options": ["Great — passion drives performance", "A yellow flag — excitement can impair your ability to objectively evaluate the setup's weaknesses", "Evidence that you love your job", "Neither good nor bad — just acknowledge it and proceed"],
        "scores": [0, 1, 0, 0],
    },
    {
        "text": "You have trouble sleeping on nights when you have an open trade. This sleep disruption is your body telling you…",
        "options": ["You're a dedicated trader — it means you care about your positions", "Your position is too large, or your risk management plan doesn't adequately address overnight risk", "It's normal trading anxiety that passes with experience", "Set tighter stop losses to reduce overnight worry"],
        "scores": [0, 1, 0, 0],
    },
    {
        "text": "The concept of 'emotional granularity' means distinguishing between 'I feel bad' and more specific labels like 'frustrated, disappointed, anxious, fearful.' In trading, this skill helps because…",
        "options": ["More labels doesn't change the underlying feeling", "Different emotions require different management strategies — anxiety needs different interventions than frustration, and lumping them all as 'bad' prevents targeted solutions", "It's academic psychology that doesn't apply to real trading", "Being able to name emotions precisely is a nice-to-have, not essential"],
        "scores": [0, 1, 0, 0],
    },
    {
        "text": "You feel REGRET about a trade you DIDN'T take that would have won. Studies show this 'regret of omission' is psychologically AS painful as losing money. The healthy response is…",
        "options": ["Use the regret as fuel to take the next setup without hesitation", "Acknowledge the feeling, journal it, and recognize that missed trades are PART of your system — you'll miss some winners by design", "Adjust your entry criteria to capture more of these trades", "Don't look back at trades you didn't take — it serves no purpose"],
        "scores": [0, 1, 0, 0],
    },
    {
        "text": "You're noticing that when you feel RUSHED, you make significantly worse trading decisions. This is because…",
        "options": ["Rushed execution leads to errors — slow down", "Time pressure shifts decision-making from deliberate (System 2 thinking) to instinctive (System 1 thinking), which relies on heuristics and biases", "You're not experienced enough to trade quickly", "Rushing means you skip checklist items"],
        "scores": [0, 1, 0, 0],
    },
    {
        "text": "You feel HOPELESS about ever becoming consistently profitable after 18 months of trying. This feeling should be evaluated by asking…",
        "options": ["'Have I been systematically tracking, testing, and refining a specific method, or have I been randomly trying different things?'", "'Should I just give up?'", "'Am I emotionally suited for trading?'", "'Do I need a better strategy?'"],
        "scores": [1, 0, 0, 0],
    },
    {
        "text": "You receive unexpected good news (promotion, inheritance, birth of a child) during the trading day. You feel elated. You should NOT trade because…",
        "options": ["Good news only affects you in a positive way", "Extreme positive emotions impair judgment JUST AS MUCH as negative ones — elation increases risk tolerance and decreases analytical rigor", "There's no rule against trading when happy", "If anything, the positive mood should help your trading"],
        "scores": [0, 1, 0, 0],
    },
    {
        "text": "You find yourself JUSTIFYING a trade entry: 'well, it's kind of near support, and the RSI is sort of oversold, and this one trendline might apply.' When you're stacking justifications like this, it means…",
        "options": ["You're being thorough — multiple confluences confirm the trade", "You're talking yourself into a trade that doesn't meet your criteria — real setups don't need justifications, they fit clearly", "The more reasons, the better", "Some setups require creative analysis to identify"],
        "scores": [0, 1, 0, 0],
    },
    {
        "text": "You feel more ATTACHED to trades you spent a long time analyzing vs. ones you spotted quickly. This attachment bias means…",
        "options": ["Detailed analysis creates conviction, which is good", "Sunk cost fallacy — the time invested in analysis makes you reluctant to cut the trade even when it's wrong", "Natural — more effort deserves more commitment", "You should probably spend more time on each trade"],
        "scores": [0, 1, 0, 0],
    },
    {
        "text": "Your emotional journey after 3 years of trading: Year 1 = excitement, Year 2 = frustration, Year 3 = acceptance. What does Year 4 look like for most who persist?",
        "options": ["Mastery — everything clicks", "Refinement — you've accepted the reality and now you're quietly optimizing processes without emotional peaks or valleys", "More frustration — the market always finds new ways to test you", "Boredom — everything becomes routine"],
        "scores": [0, 1, 0, 0],
    },
    {
        "text": "You catch yourself thinking: 'The market is out to get me.' This paranoid thinking…",
        "options": ["Is understandable when you've had many stop-outs", "Reveals you're personalizing random market movements, which leads to emotional trading, revenge, and eventual account damage", "Might have some truth — markets DO target retail stops", "Shows you need a break from trading"],
        "scores": [0, 1, 0, 0],
    },
    {
        "text": "A study shows that traders who write about their emotions for 15 minutes after trading perform better the next session. This 'expressive writing' effect works because…",
        "options": ["Writing helps organize thoughts", "It externalizes unprocessed emotions that would otherwise linger in working memory and contaminate future decisions", "It's journaling, which all traders should do anyway", "The 15-minute break between sessions is the real benefit"],
        "scores": [0, 1, 0, 0],
    },
    {
        "text": "You feel PRIDE in your trading identity. 'I am a trader.' What's the hidden danger of this strong identity attachment?",
        "options": ["No danger — identifying as a trader creates commitment", "When your identity IS 'trader,' losses feel like attacks on your SELF, not just your account — making emotional recovery much harder", "Strong identity drives discipline and consistency", "Only dangerous if you don't have another source of identity"],
        "scores": [0, 1, 0, 0],
    },
    {
        "text": "You feel CALM before a trade, anxious during, and relieved after. This pattern suggests…",
        "options": ["Normal — the uncertainty of an open trade creates anxiety", "Your brain treats each trade like a threat event. The calm-anxious-relieved pattern mirrors fight-or-flight. Consider if your sizing or approach creates excessive stress", "Nothing wrong — all 3 emotions are appropriate for their timing", "You should practice mindfulness during open trades"],
        "scores": [0, 1, 0, 0],
    },
    {
        "text": "Your internal dialogue after a loss: 'I knew it! I should have waited. Why am I so stupid?' This type of self-talk is…",
        "options": ["Honest self-assessment — you should listen to it", "Hindsight bias wrapped in self-criticism. You didn't 'know it.' You felt uncertain, made a decision, and now your brain is rewriting history", "Motivating — it'll make you more careful next time", "A sign of high standards — most traders don't self-reflect this honestly"],
        "scores": [0, 1, 0, 0],
    },
    {
        "text": "You notice you trade DIFFERENTLY when someone is watching your screen vs. when you're alone. When observed, you…",
        "options": ["Perform better due to accountability", "Change your behavior to manage the observer's perception — which means your decisions are partly social, not purely analytical", "Trade more conservatively, which is good", "Both benefit and suffer depending on the observer's reactions"],
        "scores": [0, 1, 0, 0],
    },
    {
        "text": "Your HAPPIEST trading day ever was a day you made zero money but followed every single rule perfectly during difficult conditions. Why does this matter?",
        "options": ["It shows your priorities are aligned with process over outcome — this is the foundation of long-term success", "It doesn't matter — profitability is what counts", "It's nice but you need to make money eventually", "Process satisfaction is important but shouldn't replace profit goals"],
        "scores": [1, 0, 0, 0],
    },
    {
        "text": "You feel IMPATIENT for the market to move to your target price. You've been in the trade for 2 hours and it's barely moved. This impatience typically leads to…",
        "options": ["Closing early out of boredom", "One of two mistakes: either exiting too early or moving the target further to 'make the wait worthwhile' — both are emotional, not analytical", "Nothing if you have a hard SL and TP set", "Looking for other trades to compensate for the slow mover"],
        "scores": [0, 1, 0, 0],
    },
    {
        "text": "You feel OBLIGATED to trade every day because 'traders trade.' The reality is…",
        "options": ["Consistency is key — daily trading builds skill", "Some of the most profitable days are days you trade ZERO. Feeling obligated to trade guarantees overtrading", "You need screen time to develop pattern recognition", "Professional traders DO trade daily — that's what makes them professional"],
        "scores": [0, 1, 0, 0],
    },
    {
        "text": "The emotional progression of a typical losing trade for you: denial → hope → bargaining → acceptance. This looks remarkably like grief stages because…",
        "options": ["Financial loss triggers a grief response — you're mourning money", "Your brain processes financial loss through the SAME neural pathways as other forms of loss — it IS a mini grief cycle each time", "It's a coincidence — trading isn't the same as grief", "Loss is loss — the brain doesn't distinguish between types"],
        "scores": [0, 1, 0, 0],
    },
    {
        "text": "If you could train ONE emotional skill to maximize your trading performance, it should be…",
        "options": ["Confidence — believing in yourself", "Equanimity — the ability to maintain psychological balance regardless of external circumstances", "Patience — waiting for the right setup", "Detachment — not caring about money"],
        "scores": [0, 1, 0, 0],
    },
    {
        "text": "You feel confident entering trades but terrified managing them. The entry feels controlled but the open trade feels chaotic. This suggests…",
        "options": ["Your entry criteria are solid but your trade management rules are vague — uncertainty about 'what to do next' creates anxiety", "This is normal — entries are one-time decisions, management is ongoing", "You should use 'set and forget' trading to eliminate management anxiety", "Your position sizes are appropriate for entry but feel too large once at risk"],
        "scores": [1, 0, 0, 0],
    },
    {
        "text": "You've been consistently profitable for 6 months. Suddenly, you feel IMPOSTER SYNDROME — 'Maybe I've just been lucky.' This feeling…",
        "options": ["Is your realistic assessment — maybe you ARE lucky", "Is common and dangerous because it can make you abandon a working system. Use data, not feelings, to evaluate performance", "Shows humility, which is healthy for a trader", "Is a sign you should prove yourself with a larger account"],
        "scores": [0, 1, 0, 0],
    },
    {
        "text": "You realize that FEAR and GREED are actually the SAME emotion (arousal) with different labels depending on context. This understanding changes your approach because…",
        "options": ["It doesn't — fear and greed feel different", "It means you need ONE arousal management system (breathing, breaks, sizing), not separate strategies for fear and greed", "It simplifies your emotional tracking in the journal", "Interesting theory but not practically useful"],
        "scores": [0, 1, 0, 0],
    },
    {
        "text": "You keep thinking about a past trade that went horribly wrong, even though it was 6 months ago. This 'rumination' affects current trading by…",
        "options": ["It doesn't — past trades are past trades", "Creating a persistent background anxiety that makes you hesitant, second-guess signals, and subconsciously avoid similar setups", "Keeping you cautious, which is protective", "Reminding you of lessons learned"],
        "scores": [0, 1, 0, 0],
    },
    {
        "text": "The most emotionally demanding phase of a trader's career is NOT the losing phase. It's actually…",
        "options": ["The beginning — everything is new and overwhelming", "The transition from inconsistent to consistent — where you can SEE the edge working but keep sabotaging it with emotional errors", "Drawdowns — losing money is always the hardest", "Going full-time — the pressure of trading for a living"],
        "scores": [0, 1, 0, 0],
    },
    {
        "text": "You feel COMPETITIVE with other traders in your community. You want to outperform them. Competition in trading is…",
        "options": ["Healthy motivation that drives improvement", "Largely counterproductive — your only competition is your own past self. Comparing to others introduces irrelevant variables", "Good as long as you don't take unnecessary risks to 'win'", "The lifeblood of trading — markets are competitive by nature"],
        "scores": [0, 1, 0, 0],
    },
    {
        "text": "You feel GRATEFUL for a losing trade that taught you an important lesson. This ability to find value in losses indicates…",
        "options": ["You're rationalizing a loss to feel better", "High emotional maturity — reframing losses as data rather than failures is the hallmark of professional development", "Every loss has a silver lining", "You're too positive — losses should motivate you, not make you grateful"],
        "scores": [0, 1, 0, 0],
    },
    {
        "text": "Your emotional 'tells' before impulsive trades: shallow breathing, leaning forward, clicking faster. Recognizing these tells helps because…",
        "options": ["Physical awareness is nice but doesn't prevent emotional trades", "You can intervene at the BODY level before the mind makes the decision — changing your physiology (sit back, breathe deep, slow down) literally interrupts the impulse", "It confirms you were emotional, which is useful for the journal", "Tells are unreliable — sometimes you have the same physiology on good trades"],
        "scores": [0, 1, 0, 0],
    },
    {
        "text": "You're asked: 'Would you rather win 80% of trades and feel amazing, or win 40% of trades and be more profitable overall?' Most people choose 80%. Why is this the wrong choice?",
        "options": ["80% win rate IS better — higher accuracy is always superior", "Because the question reveals we prioritize emotional comfort (feeling right) over financial results — and this preference causes traders to cut winners short", "Both could be equally profitable depending on R:R", "40% win rate requires too much psychological resilience for most people"],
        "scores": [0, 1, 0, 0],
    },
    {
        "text": "You feel CONFUSED — some days you trade well, other days terribly, and you can't figure out the pattern. The most likely missing variable is…",
        "options": ["Your strategy needs more work", "Your emotional state, which you probably aren't tracking systematically enough to see the correlation", "Market conditions vary — some days suit your style, others don't", "You need more experience to develop consistency"],
        "scores": [0, 1, 0, 0],
    },
    {
        "text": "If trading emotions were a weather system, the ideal forecast for optimal performance would be…",
        "options": ["Sunny — pure optimism and confidence", "Partly cloudy — enough caution to respect risk, enough clarity to act on genuine signals", "Overcast — cautious and conservative", "Clear skies — complete absence of emotional weather"],
        "scores": [0, 1, 0, 0],
    },
]
