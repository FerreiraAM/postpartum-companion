import json
import random
import streamlit as st

st.set_page_config(page_title="Postpartum Companion", page_icon="💛", layout="centered")

with open("messages.json", encoding="utf-8") as f:
    VALIDATIONS = json.load(f)

MOOD_ICONS = {
    "Overwhelmed": "assets/overwhelmed.svg",
    "Exhausted": "assets/exhausted.svg",
    "Anxious": "assets/anxious.svg",
    "Lonely": "assets/lonely.svg",
    "Good Day": "assets/good_day.svg",
}
MOOD_COLORS = {
    "Overwhelmed": "#fbd9d9",
    "Exhausted": "#e3def4",
    "Anxious": "#fbe6c2",
    "Lonely": "#cfe7ee",
    "Good Day": "#d9ecd4",
}
MOODS = list(VALIDATIONS.keys())

NEED_ICONS = {
    "Validation": "💗",
    "Encouragement": "🌱",
    "Perspective": "☀️",
    "Self-compassion": "🫶",
}
NEED_COLORS = {
    "Validation": "#fbd9d9",
    "Encouragement": "#d9ecd4",
    "Perspective": "#fbe6c2",
    "Self-compassion": "#e3def4",
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
        border: none;
        background-color: transparent;
        color: #5b3a52;
        padding: 0.3rem 0.5rem;
        font-weight: 500;
        text-align: center;
        justify-content: center;
        transition: all 0.15s ease;
    }
    div.stButton > button:hover {
        color: #5b3a52;
        text-decoration: underline;
    }
    div.stButton > button:focus:not(:active) {
        color: #5b3a52;
    }
    div.stButton > button[kind="primary"] {
        font-weight: 700;
    }
    div[class*="st-key-mood_card_"], div[class*="st-key-need_card_"] {
        border-radius: 14px;
        border: 1px solid #f1d9d3;
        padding: 0.75rem 0.5rem 0.25rem 0.5rem;
        text-align: center;
        transition: all 0.15s ease;
        position: relative;
    }
    div[class*="st-key-mood_card_"] [data-testid="stImage"],
    div[class*="st-key-mood_card_"] [data-testid="stImage"] > div,
    div[class*="st-key-need_card_"] [data-testid="stImage"],
    div[class*="st-key-need_card_"] [data-testid="stImage"] > div {
        display: flex;
        justify-content: center;
        pointer-events: none;
    }
    div[class*="st-key-mood_card_"] [data-testid="stImage"] img {
        margin: 0 auto;
    }
    div[class*="st-key-mood_card_"] div.stButton,
    div[class*="st-key-need_card_"] div.stButton {
        position: absolute;
        inset: 0;
    }
    div[class*="st-key-mood_card_"] div.stButton > button,
    div[class*="st-key-need_card_"] div.stButton > button {
        height: 100%;
        align-items: flex-end;
        padding-bottom: 0.5rem;
        cursor: pointer;
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
        slug = mood.replace(" ", "_").lower()
        border = "2px solid #c97b87" if is_selected else "1px solid #f1d9d3"
        shadow = "0 2px 8px rgba(201, 123, 135, 0.25)" if is_selected else "none"
        st.markdown(
            f"""
            <style>
            div[class*="st-key-mood_card_{slug}"] {{
                background-color: {MOOD_COLORS[mood]}55;
                border: {border};
                box-shadow: {shadow};
            }}
            </style>
            """,
            unsafe_allow_html=True,
        )
        with st.container(key=f"mood_card_{slug}"):
            st.image(MOOD_ICONS[mood])
            if st.button(
                mood,
                key=f"mood_{slug}",
                type="primary" if is_selected else "secondary",
            ):
                st.session_state.mood = mood
                st.rerun()

st.markdown("### What do you need today?")
need_cols = st.columns(len(NEEDS))
for col, need in zip(need_cols, NEEDS):
    with col:
        is_selected = st.session_state.need == need
        slug = need.replace(" ", "_").replace("-", "_").lower()
        border = "2px solid #c97b87" if is_selected else "1px solid #f1d9d3"
        shadow = "0 2px 8px rgba(201, 123, 135, 0.25)" if is_selected else "none"
        st.markdown(
            f"""
            <style>
            div[class*="st-key-need_card_{slug}"] {{
                background-color: {NEED_COLORS[need]}55;
                border: {border};
                box-shadow: {shadow};
            }}
            </style>
            """,
            unsafe_allow_html=True,
        )
        with st.container(key=f"need_card_{slug}"):
            if st.button(
                f"{NEED_ICONS[need]} {need}",
                key=f"need_{slug}",
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
