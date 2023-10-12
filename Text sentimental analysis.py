import nltk
from nltk.sentiment.vader import SentimentIntensityAnalyzer

nltk.download("vader_lexicon")  # Download the VADER lexicon if not already done

# Create a SentimentIntensityAnalyzer object
sia = SentimentIntensityAnalyzer()

# Get user input or text to analyze
user_input = input("Enter text for sentiment analysis: ")

# Perform sentiment analysis
sentiment_scores = sia.polarity_scores(user_input)

# Determine sentiment based on the compound score
compound_score = sentiment_scores["compound"]

if compound_score >= 0.05:
    sentiment = "Positive"
elif compound_score <= -0.05:
    sentiment = "Negative"
else:
    sentiment = "Neutral"

print(f"Sentiment: {sentiment}")
print("Sentiment Scores:", sentiment_scores)
