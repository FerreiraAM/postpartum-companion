import json
import random
import streamlit as st

st.set_page_config(page_title="Postpartum Companion", page_icon="💛", layout="centered")

with open("messages.json", encoding="utf-8") as f:
    VALIDATIONS = json.load(f)

MOOD_EMOJIS = {
    "Overwhelmed": "😣",
    "Exhausted": "😴",
    "Anxious": "😟",
    "Lonely": "🥺",
    "Good Day": "😊",
}
MOODS = list(VALIDATIONS.keys())

NEED_ICONS = {
    "Validation": "💗",
    "Encouragement": "🌱",
    "Perspective": "☀️",
    "Self-compassion": "🫶",
}
NEEDS = list(NEED_ICONS.keys())

st.markdown(
    """
    <style>
    .stApp {
        background: linear-gradient(180deg, #fdf3ef 0%, #fbeee8 100%);
    }
    h1, h2, h3 {
        font-family: Georgia, 'Times New Roman', serif;
        color: #5b3a52;
    }
    .subtitle {
        color: #9b8a93;
        font-size: 1rem;
        margin-top: -0.5rem;
        margin-bottom: 1.5rem;
    }
    div.stButton > button {
        width: 100%;
        border-radius: 12px;
        border: 1px solid #f1d9d3;
        background-color: #fffaf8;
        color: #5b3a52;
        padding: 0.6rem 0.5rem;
        font-weight: 500;
        transition: all 0.15s ease;
    }
    div.stButton > button:hover {
        border-color: #e8a4a4;
        background-color: #fdeae6;
        color: #5b3a52;
    }
    div.stButton > button:focus:not(:active) {
        border-color: #d98a8a;
        color: #5b3a52;
    }
    div.stButton > button[kind="primary"] {
        background-color: #f6c9c4;
        border-color: #e8a4a4;
        color: #5b3a52;
    }
    div.stButton > button[kind="primary"]:hover {
        background-color: #f3b9b3;
        border-color: #e29696;
        color: #5b3a52;
    }
    div.stButton > button[kind="primary"]:focus:not(:active) {
        background-color: #f6c9c4;
        border-color: #e29696;
        color: #5b3a52;
    }
    .st-key-get_support {
        display: flex !important;
        justify-content: center !important;
    }
    .st-key-get_support button {
        background-color: #c97b87 !important;
        border-color: #c97b87 !important;
        color: #ffffff !important;
        font-size: 1rem !important;
        font-weight: 600 !important;
        padding: 0.7rem 1.25rem !important;
        border-radius: 999px !important;
        width: auto !important;
        white-space: nowrap !important;
        display: flex !important;
        justify-content: center !important;
        align-items: center !important;
    }
    .st-key-get_support button:hover {
        background-color: #b96874 !important;
        border-color: #b96874 !important;
        color: #ffffff !important;
    }
    .st-key-get_support button:hover {
        background-color: #b96874;
        border-color: #b96874;
        color: #ffffff;
    }
    .result-card {
        background-color: #ffffff;
        border-radius: 16px;
        padding: 1.5rem 1.75rem;
        margin-top: 1.5rem;
        border: 1px solid #f5e1dc;
        box-shadow: 0 2px 10px rgba(180, 130, 130, 0.08);
        font-size: 1.1rem;
        color: #5b3a52;
        line-height: 1.6;
    }
    </style>
    """,
    unsafe_allow_html=True,
)

st.markdown("# Postpartum Companion")
st.markdown(
    "<p class='subtitle'>You're doing better than you think.</p>",
    unsafe_allow_html=True,
)

if "mood" not in st.session_state:
    st.session_state.mood = None
if "need" not in st.session_state:
    st.session_state.need = None

st.markdown("### How are you feeling right now?")
mood_cols = st.columns(len(MOODS))
for col, mood in zip(mood_cols, MOODS):
    with col:
        is_selected = st.session_state.mood == mood
        if st.button(
            f"{MOOD_EMOJIS[mood]}\n{mood}",
            key=f"mood_{mood}",
            type="primary" if is_selected else "secondary",
        ):
            st.session_state.mood = mood
            st.rerun()

st.markdown("### What do you need today?")
need_cols = st.columns(len(NEEDS))
for col, need in zip(need_cols, NEEDS):
    with col:
        is_selected = st.session_state.need == need
        if st.button(
            f"{NEED_ICONS[need]} {need}",
            key=f"need_{need}",
            type="primary" if is_selected else "secondary",
        ):
            st.session_state.need = need
            st.rerun()

st.write("")

support_cols = st.columns(len(MOODS))
with support_cols[2]:
    get_support_clicked = st.button("✨ Get support ✨", key="get_support")

if get_support_clicked:
    if st.session_state.mood and st.session_state.need:
        message = random.choice(VALIDATIONS[st.session_state.mood][st.session_state.need])
        st.markdown(f"<div class='result-card'>{message}</div>", unsafe_allow_html=True)
    else:
        st.warning("Please select both a mood and a need first.")
