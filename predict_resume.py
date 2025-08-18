import os
import re, string
import joblib
import docx
from PyPDF2 import PdfReader
from nltk.corpus import stopwords

# Load model and vectorizer
model = joblib.load("logistic_regression_model.pkl")
vectorizer = joblib.load("tfidf_vectorizer.pkl")
stop_words = set(stopwords.words("english"))

# --- Helper: Clean text ---
def clean_text(text):
    text = text.lower()
    text = text.translate(str.maketrans("", "", string.punctuation))
    text = re.sub(r"\d+", "", text)
    text = re.sub(r"\s+", " ", text).strip()
    words = text.split()
    words = [word for word in words if word not in stop_words]
    return " ".join(words)

# --- Main function: Predict from file ---
def predict_resume(file):
    ext = os.path.splitext(file.name)[1].lower()

    if ext == ".docx":
        doc = docx.Document(file)
        text = " ".join([para.text for para in doc.paragraphs])

    elif ext == ".pdf":
        reader = PdfReader(file)
        text = " ".join([page.extract_text() for page in reader.pages if page.extract_text()])

    else:
        return "Unsupported file format. Please upload a .docx or .pdf file.", None, None

    # Clean and predict
    cleaned = clean_text(text)
    X_new = vectorizer.transform([cleaned])
    prediction = model.predict(X_new)[0]
    probs = model.predict_proba(X_new)[0]

    return prediction, probs, text  # <- also we get the raw text