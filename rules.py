# rules.py

rules = {
    # Positive
    "good": 2,
    "great": 3,
    "excellent": 4,
    "amazing": 4,
    "awesome": 3,
    "fast": 2,
    "love": 3,

    # Negative
    "bad": -2,
    "poor": -2,
    "worst": -4,
    "slow": -2,
    "terrible": -4,
    "hate": -3,

    # Special
    "not good": -1,
    "not bad": 1
}


def calculate_score(text):
    text = text.lower()
    score = 0

    for word, value in rules.items():
        if word in text:
            score += value

    return score


def get_sentiment(score):
    if score >= 3:
        return "Very Positive"
    elif score == 2:
        return "Positive"
    elif score == 1:
        return "Slightly Positive"
    elif score == 0:
        return "Neutral"
    elif score == -1:
        return "Slightly Negative"
    elif score == -2:
        return "Negative"
    else:
        return "Very Negative"