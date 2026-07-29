import streamlit as st
import pandas as pd
import re

from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB

# -----------------------------
# Page Configuration
# -----------------------------
st.set_page_config(
    page_title="Support Ticket Classifier",
    page_icon="🎫",
    layout="centered"
)

st.title("🎫 Support Ticket Classification & Prioritization")
st.write("Automatically classify customer support tickets using NLP and Machine Learning.")

# -----------------------------
# Load Dataset
# -----------------------------
@st.cache_data
def load_data():
    df = pd.read_csv("all_tickets_processed_improved_v3.xls")
    return df

df = load_data()

# -----------------------------
# Text Cleaning
# -----------------------------
def clean_text(text):
    text = text.lower()
    text = re.sub(r'[^a-zA-Z\s]', '', text)
    return text

df["Clean_Text"] = df["Document"].apply(clean_text)

# -----------------------------
# Train Model
# -----------------------------
X = df["Clean_Text"]
y = df["Topic_group"]

vectorizer = TfidfVectorizer(stop_words="english")

X_vector = vectorizer.fit_transform(X)

X_train, X_test, y_train, y_test = train_test_split(
    X_vector,
    y,
    test_size=0.2,
    random_state=42
)

model = MultinomialNB()
model.fit(X_train, y_train)

# -----------------------------
# Priority Function
# -----------------------------
def assign_priority(ticket):

    ticket = ticket.lower()

    high = [
        "urgent", "critical", "server", "down", "cannot","can't", "cant", "not working","login failed", "login issue","login"
                "failed","locked","password","error", "crash", "hack", "payment failed",
    ]

    medium = [
        "issue","problem","warning","slow","delay"
    ]

    for word in high:
        if word in ticket:
            return "🔴 High"

    for word in medium:
        if word in ticket:
            return "🟡 Medium"

    return "🟢 Low"

# -----------------------------
# Prediction
# -----------------------------
st.subheader("Enter Support Ticket")

ticket = st.text_area(
    "Ticket Description",
    placeholder="Example: My laptop crashes whenever I start Windows."
)

if st.button("Predict"):

    if ticket.strip() == "":
        st.warning("Please enter a support ticket.")
    else:

        cleaned = clean_text(ticket)

        vector = vectorizer.transform([cleaned])

        category = model.predict(vector)[0]

        priority = assign_priority(ticket)

        st.success("Prediction Complete")

        col1, col2 = st.columns(2)

        with col1:
            st.metric("Category", category)

        with col2:
            st.metric("Priority", priority)

# -----------------------------
# Footer
# -----------------------------
st.markdown("---")

st.write("Developed using Python, Streamlit, Scikit-learn and NLP")