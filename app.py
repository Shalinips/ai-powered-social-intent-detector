import streamlit as st
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression

# ----------------------------
# DATASET (Simulated but Valid)
# ----------------------------
data = {
    "text": [
        "Wow, you really did an amazing job ruining everything",
        "Sure, that was a brilliant idea",
        "Please let me know if you need any help",
        "Thank you for your support, I appreciate it",
        "Click this link to claim your free reward",
        "You have won a prize, act fast to receive it",
        "Okay, noted",
        "I understand your concern",
        "Oh great, another perfect decision",
        "Can you please assist me with this task"
    ],
    "intent": [
        "Sarcasm",
        "Sarcasm",
        "Polite",
        "Polite",
        "Manipulative",
        "Manipulative",
        "Neutral",
        "Neutral",
        "Sarcasm",
        "Polite"
    ]
}

df = pd.DataFrame(data)

# ----------------------------
# MODEL TRAINING
# ----------------------------
vectorizer = TfidfVectorizer()
X = vectorizer.fit_transform(df["text"])
y = df["intent"]

model = LogisticRegression()
model.fit(X, y)

# ----------------------------
# STREAMLIT UI
# ----------------------------
st.set_page_config(page_title="AI Social Intent Detector", layout="centered")

st.title("🧠 AI-Powered Social Intent Detector")
st.subheader("Detecting Hidden Intentions in Conversations")

st.write(
    "This system goes beyond traditional sentiment analysis by identifying "
    "hidden social intentions such as sarcasm, manipulation, politeness, or neutrality."
)

user_input = st.text_area("💬 Enter a message:", height=120)

if st.button("Analyze Intent"):
    if user_input.strip() == "":
        st.warning("Please enter a message to analyze.")
    else:
        input_vector = vectorizer.transform([user_input])
        prediction = model.predict(input_vector)[0]
        confidence = model.predict_proba(input_vector).max()

        st.success(f"🧭 **Detected Intent:** {prediction}")
        st.info(f"📊 **Confidence Score:** {confidence:.2f}")
