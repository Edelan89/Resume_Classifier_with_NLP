# 📄 Resume Classifier with NLP  

An intelligent resume classifier built with **Natural Language Processing (NLP)** and **Machine Learning**.  
The app allows users to upload a CV in **PDF or DOCX** format and automatically predicts the most likely professional category.  

---

## 🚀 Live Demo
👉 (Coming soon on Streamlit Cloud)  

---

## 📌 Key Features
- ✅ Reads resumes in **.docx** and **.pdf** formats  
- ✅ Text cleaning & normalization (tokenization, stopwords removal, etc.)  
- ✅ Transforms text into numerical vectors using **TF-IDF**  
- ✅ Trained & compared models:  
  - Naive Bayes  
  - Logistic Regression  
  - Random Forest (final selected model)  
- ✅ User-friendly **Streamlit** web interface:  
  - Resume text preview  
  - Predicted job category  
  - Top-3 prediction probabilities in a bar chart  

---

## 📊 Model Performance

| Model               | Accuracy | Macro F1 |
|----------------------|----------|----------|
| Naive Bayes          | 0.69     | 0.62     |
| Logistic Regression  | 0.81     | 0.81     |
| Random Forest        | **0.90** | **0.90** |

📌 The **Random Forest** model was chosen for the final version due to its higher performance.  

---

## 🛠️ Tech Stack
- **Python 3.11**  
- **NLTK** (text preprocessing)  
- **scikit-learn** (ML models & evaluation metrics)  
- **Streamlit** (web app)  
- **PyPDF2** & **python-docx** (file parsing)  
- **Joblib** (model persistence)  

---

## 📂 Project Structure
📦 resume-classifier-nlp
┣ 📜 app.py # Streamlit web application
┣ 📜 Resume_Classifier_with_NLP.ipynb # Jupyter notebook with analysis
┣ 📜 random_forest_model.pkl # Trained ML model
┣ 📜 tfidf_vectorizer.pkl # TF-IDF vectorizer
┣ 📜 requirements.txt # Project dependencies
┗ 📜 README.md # Documentation

## ⚡ Installation & Usage

1. Clone the repository:
   ```bash
   git clone https://github.com/Edelan89/Resume_Classifier_with_NLP.git
   cd Resume_Classifier_with_NLP

2. Create and activate a virtual environment

python -m venv .venv
source .venv/bin/activate   # Linux/Mac
.venv\Scripts\activate      # Windows

3. Install dependencies:

pip install -r requirements.txt

4. Run the app:

streamlit run app.py

👨‍💻 Author

Maximiliano M. Pérez Fernández
📍 Data Analyst & NLP Enthusiast
🔗 [LinkedIn](https://www.linkedin.com/in/maximiliano-mauricio-perez-fernandez-a24878a4/) | [GitHub](https://github.com/Edelan89)


🌟 Contributions

Contributions, issues, and suggestions are welcome.
If you like this project, please give it a ⭐ on GitHub!