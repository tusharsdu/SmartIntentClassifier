import streamlit as st
import joblib
import random
from pathlib import Path
import sys
sys.path.append(str(Path(__file__).resolve().parents[1]))
from src.intent_responses import responses

st.set_page_config(page_title="AI Chatbot", page_icon="🤖")
st.title("🤖 Intent Classification Chatbot")

MODEL_PATH = Path(__file__).resolve().parents[1] / "models" / "intent_classifier.pkl"

@st.cache_resource
def load_model():
    if MODEL_PATH.exists():
        return joblib.load(MODEL_PATH)
    return None

model = load_model()

if "history" not in st.session_state:
    st.session_state.history = []

user_input = st.text_input("You:", "")

if st.button("Send"):
    if user_input.strip():
        if model:
            intent = model.predict([user_input])[0]
        else:
            intent = "oos"
        reply = random.choice(responses.get(intent, ["Sorry, I don't understand."]))
        st.session_state.history.append(("You", user_input))
        st.session_state.history.append(("Bot", f"[{intent}] {reply}"))

for speaker, msg in st.session_state.history:
    st.markdown(f"**{speaker}:** {msg}")
