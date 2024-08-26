# sentiment_analysis.py
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
from textblob import TextBlob
import matplotlib.pyplot as plt
import io

def analyze_sentiment(sentence):
    sid_obj = SentimentIntensityAnalyzer()
    sentiment_dict = sid_obj.polarity_scores(sentence)
    
    # Add emotion detection
    blob = TextBlob(sentence)
    polarity = blob.sentiment.polarity
    subjectivity = blob.sentiment.subjectivity
    
    if polarity > 0.6:
        emotion = "Very Positive"
    elif polarity > 0.1:
        emotion = "Positive"
    elif polarity < -0.6:
        emotion = "Very Negative"
    elif polarity < -0.1:
        emotion = "Negative"
    else:
        emotion = "Neutral"
    
    if subjectivity > 0.7:
        emotion += " (Very Subjective)"
    elif subjectivity < 0.3:
        emotion += " (Very Objective)"
    
    sentiment_dict['emotion'] = emotion
    
    return sentiment_dict


def generate_sentiment_pie(sentiment_dict):
    labels = 'Negative', 'Neutral', 'Positive'
    sizes = [sentiment_dict['neg'], sentiment_dict['neu'], sentiment_dict['pos']]
    colors = ['red', 'gray', 'green']
    
    img_buffer = io.BytesIO()
    plt.figure(figsize=(5, 5))
    plt.bar(sizes, labels=labels, colors=colors, autopct='%1.1f%%', startangle=90)
    plt.title('Sentiment Distribution')
    plt.savefig(img_buffer, format='png')
    img_buffer.seek(0)
    return img_buffer
