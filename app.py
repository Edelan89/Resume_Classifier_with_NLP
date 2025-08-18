import streamlit as st
import numpy as np
from predict_resume import predict_resume, model

st.set_page_config(page_title="Resume Classifier - Random Forest Model", page_icon="📄")

st.title("📄 Resume Classifier - Random Forest Model")

uploaded_file = st.file_uploader("Upload your resume", type=["docx", "pdf"])

if uploaded_file is not None:
    prediction, probs, raw_text = predict_resume(uploaded_file)

    if probs is not None:
        st.subheader("✅ Predicted Category:")
        st.success(prediction)

        # Mostrar preview del texto
        st.subheader("🔎 Extracted Text Preview:")
        st.text_area("Text Extracted from Resume", raw_text[:500] + "...", height=200)

        # Mostrar probabilidades
        st.subheader("📊 Top 3 Probabilities:")
        classes = model.classes_
        top3_idx = np.argsort(probs)[-3:][::-1]
        st.bar_chart({classes[i]: probs[i] for i in top3_idx})

    else:
        st.error(prediction)
