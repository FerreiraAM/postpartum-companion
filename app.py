import json
import random
import streamlit as st

st.set_page_config(page_title="Postpartum Companion", page_icon="💛")

with open("messages.json", encoding="utf-8") as f:
    VALIDATIONS = json.load(f)

MOODS = list(VALIDATIONS.keys())
NEEDS = ["Validation", "Encouragement", "Perspective", "Self-compassion"]

st.title("💛 Postpartum Companion")
st.write("Select how you're feeling right now.")

mood = st.selectbox("How are you feeling?", MOODS)
need = st.selectbox("What do you need today?", NEEDS)

if st.button("Get support"):
    st.success(random.choice(VALIDATIONS[mood][need]))
