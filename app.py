import streamlit as st
import joblib

# Set page configuration for a professional look
st.set_page_config(page_title="AI Phishing Detector", page_icon="🛡️", layout="centered")

# 1. Load Model and Vectorizer
model = joblib.load('model.pkl')
vectorizer = joblib.load('vectorizer.pkl')

# 2. Enterprise Header
st.title("🛡️ Enterprise AI Phishing Detector")
st.subheader("Predictive Email Security Analysis")
st.write("Analyze incoming email payloads for linguistic indicators of fraud, urgency, and social engineering.")

st.markdown("---")

# 3. User Input Field
user_input = st.text_area(
    label="Email Content Analysis", 
    placeholder="Paste the raw email body or text here to analyze...",
    height=200
)

# 4. Action Button and Logic
if st.button("Scan Email Payload", use_container_width=True):
    if user_input.strip():
        # Transform the raw text using the trained vectorizer
        data = vectorizer.transform([user_input])
        prediction = model.predict(data)
        
        # Display professional security alerts
        if prediction[0] == 1:
            st.error("🚨 **Security Alert:** This email shows high-probability patterns of a **Phishing Attack**.")
            st.warning("**Recommendation:** Do not click any links, open attachments, or reply to this sender.")
        else:
            st.success("✅ **Scan Clean:** No immediate phishing or social engineering patterns detected.")
            st.info("**Note:** Always practice caution if the sender address looks unfamiliar.")
    else:
        st.warning("Input Required: Please paste email content to initiate the security scan.")