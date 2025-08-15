import streamlit as st
import joblib
import docx
import re
import string 
from nltk.corpus import stopwords

# Load the model and vectorizer
model = joblib.load("logistic_regression_model.pkl")
vectorizer = joblib.load("tfidf_vectorizer.pkl")

# Cleaning function
stop_words = set(stopwords.words('english'))

def clean_text(text):
    text = text.lower()  # Lowercase
    text = re.sub(r'\d+', '', text)  # Remove digits
    text = re.sub(r'\s+', ' ', text)  # Remove extra spaces
    text = text.translate(str.maketrans('', '', string.punctuation))  # Remove punctuation
    words = text.split()  # Tokenize
    words = [word for word in words if word not in stop_words]  # Remove stopwords
    return ' '.join(words)

# Reading and predicting function
def predict_resume(file):
    doc = docx.Document(file)
    text = " ".join([para.text for para in doc.paragraphs])
    cleaned = clean_text(text)
    X_new = vectorizer.transform([cleaned])
    prediction = model.predict(X_new)[0]
    probs = model.predict_proba(X_new)[0]
    return prediction, probs

# Streamlit app
