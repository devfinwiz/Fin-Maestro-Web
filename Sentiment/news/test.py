from NewsSentiment import TargetSentimentClassifier
tsc = TargetSentimentClassifier()

sentiment = tsc.infer_from_text("""""",
"Byju"
,"""

Byju's is weighing whether to wind down WhiteHat Jr, a coding platform that it acquired over two years ago at an enterprise value of $300 million, as the edtech group looks to cut expenses and eliminate a business unit that has drawn considerable criticism to the firm.

The Bengaluru-headquartered firm, India's most valuable startup at $22 billion valuation, has held conversations in recent weeks about shutting down what was once touted as one of its best acquisitions, three sources familiar with the matter told TechCrunch. It has not reached a decision yet, according to another person familiar with the matter.

The discussions come at a time when Byju's is cutting costs across the company. The firm, which has laid off thousands of employees and pared back on marketing expenses in recent quarters, was until recently spending about $14 million a month on the coding platform, one of the sources said. WhiteHat Jr is not independently profitable, sources said.

A Byju's spokesperson declined to comment.

Byju's acquired WhiteHat Jr in 2020 at an enterprise value of $300 million. A considerable amount of the payout, however, was tied to future growth metrics, which meant that Byju's eventually spent less than $235 million on the acquisition deal, said one of the aforementioned sources who, like others, requested anonymity discussing private matters.

The coding unit has drawn criticism from many for its misleading claims, quality of teaching, and aggressive tactics to court students. WhiteHat Jr infamously also sued some of those critics, a move that attracted the firm even more backlash. It later withdrew the lawsuit. WhiteHat Jr founder Karan Bajaj (pictured above) left Byju's a year after the acquisition, and according to one of the sources, has engaged with investors in recent weeks to explore raising a funding round for his new startup. He couldn't be immediately reached for comment.

Byju's — which counts Sequoia India, Lightspeed Venture Partners, Tiger Global, B Capital, UBS and General Atlantic among its backers — has spent the past one year addressing many criticisms levelled at the firm. Byju's said last month that its sales people no longer visited students' homes to pitch to their parents and the firm now conducts a test to determine whether a kid's parents can afford to subscribe to the service before signing them up.


""")
print(sentiment[0])

sentiment = tsc.infer("that guy looks very sad and depressed.")
print(sentiment[0])
