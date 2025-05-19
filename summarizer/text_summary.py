from textblob import TextBlob
import nltk
nltk.download('punkt_tab')

def summarize_text(text):
    blob = TextBlob(text)
    sentences = blob.sentences

    # Basic summary: first 3 and last sentence
    summary = ' '.join(str(s) for s in (sentences[:3] + sentences[-1:])) if len(sentences) > 3 else text
    return summary

def analyze_sentiment(text):
    blob = TextBlob(text)
    polarity = blob.sentiment.polarity
    if polarity > 0:
        return 'Positive'
    elif polarity < 0:
        return 'Negative'
    return 'Neutral'
