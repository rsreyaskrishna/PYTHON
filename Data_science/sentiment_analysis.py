positive_words = [
    "good", "happy", "joy", "excellent", "fortunate", "correct", "superior",
    "love", "like", "amazing", "wonderful", "best", "great"
]
negative_words = [
    "bad", "sad", "angry", "poor", "unfortunate", "wrong", "inferior",
    "hate", "dislike", "awful", "terrible", "worst", "horrible"
]
def sentiment_analysis(text):
    text = text.lower()
    words = text.split()
    score = 0

    for word in words:
        if word in positive_words:
            score += 1
        elif word in negative_words:
            score -= 1

    if score > 0:
        return "Positive"
    elif score < 0:
        return "Negative"
    else:
        return "Neutral"
text = "I love travelling, it is amazing to explore places.it makes me happy"
result = sentiment_analysis(text)
print("The sentiment is: ",result)
