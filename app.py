import streamlit as st
import joblib

st.set_page_config(page_title="AI Cybersecurity Threat Intelligence", page_icon="🛡️")

@st.cache_resource
def load_models():
    model = joblib.load("phishing_svm_model.pkl")
    tfidf = joblib.load("phishing_tfidf_vectorizer.pkl")
    return model, tfidf

model, tfidf = load_models()

st.title("🛡️ AI Cybersecurity Threat Intelligence")
st.subheader("Phishing Email Detector")

email = st.text_area("Paste email content here", height=200)

if st.button("Analyze Email"):
    if email.strip():
        features = tfidf.transform([email.lower().strip()])
        prediction = model.predict(features)[0]

        if prediction == 1:
            st.error("Potential phishing email")
        else:
            st.info("Predicted as class 0")
    else:
        st.warning("Please enter an email first.")

st.caption("Model predictions are not a security guarantee.")
