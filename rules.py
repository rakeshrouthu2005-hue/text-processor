RULES = {
    "great": 2,
    "good": 1,
    "excellent": 3,
    "amazing": 3,
    "bad": -2,
    "slow": -1,
    "poor": -2,
    "terrible": -3
}

def calculate_score(text):
    return sum(RULES.get(word, 0) for word in text.lower().split())

def get_sentiment(score):
    if score > 0:
        return "Positive"
    elif score < 0:
        return "Negative"
    return "Neutral"