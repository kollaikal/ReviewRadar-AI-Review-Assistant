from transformers import pipeline
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer

# Sentiment analysis using a pre-trained model
def analyze_sentiment(df):
    sentiment_model = pipeline("sentiment-analysis")
    if isinstance(df, pd.DataFrame):
        df["sentiment"] = df["review"].apply(lambda x: sentiment_model(x)[0]["label"])
        return df
    else:
        # Handle text directly (e.g., from PDFs or Word files)
        sentiment = sentiment_model(df["review"][0])[0]["label"]
        return sentiment

# Summarize reviews using a transformer model
def summarize_reviews(df):
    summarizer = pipeline("summarization")
    if isinstance(df, pd.DataFrame):
        df["summary"] = df["review"].apply(lambda x: summarizer(x, max_length=100, min_length=30, do_sample=False)[0]["summary_text"])
        return df
    else:
        # Summarize text directly (e.g., from PDFs or Word files)
        summary = summarizer(df["review"][0], max_length=100, min_length=30, do_sample=False)[0]["summary_text"]
        return summary

# Extract keywords using TF-IDF
def extract_keywords(df):
    vectorizer = TfidfVectorizer(stop_words='english')
    if isinstance(df, pd.DataFrame):
        X = vectorizer.fit_transform(df["review"].values)
        keywords = vectorizer.get_feature_names_out()
        
        # Convert the vector to dense form and then get the most relevant keywords
        dense_matrix = X.todense()
        keyword_df = pd.DataFrame(dense_matrix, columns=keywords)
        return keyword_df
    else:
        # For text, return top keywords
        X = vectorizer.fit_transform([df["review"][0]])
        keywords = vectorizer.get_feature_names_out()
        return keywords

# Fake Review Detection
def detect_fake_reviews(df):
    fake_reviews = df["review"].apply(lambda x: len(x.split()) < 5 or "amazing" in x.lower())
    df["is_fake"] = fake_reviews
    return df
