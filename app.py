import random
import streamlit as st

st.set_page_config(page_title="Postpartum Companion", page_icon="💛")

MOODS = ["😊 Happy", "😢 Sad", "😴 Exhausted", "😰 Anxious", "😡 Frustrated"]

VALIDATIONS = {
    "😊 Happy": [
        "It's wonderful that you're feeling good today. You deserve these moments of joy.",
        "Your happiness matters. Soak it in.",
        "You're doing great, and it shows.",
    ],
    "😢 Sad": [
        "It's okay to feel sad. Your emotions are valid, and this feeling will pass.",
        "You don't have to be okay all the time. Be gentle with yourself.",
        "Crying is not weakness — it's release. You're allowed to feel this.",
    ],
    "😴 Exhausted": [
        "Of course you're exhausted — you're doing one of the hardest jobs there is.",
        "Rest when you can. Your body is working incredibly hard.",
        "Being tired doesn't mean you're failing. It means you're human.",
    ],
    "😰 Anxious": [
        "Anxiety after birth is so common. You are not alone in this.",
        "It's okay to worry — it means you care deeply. Try to take one breath at a time.",
        "These feelings don't define you. They're a phase, not forever.",
    ],
    "😡 Frustrated": [
        "Frustration is a normal response to overwhelming change. You're allowed to feel it.",
        "You're allowed to feel angry without being a bad parent.",
        "It's hard, and it's okay to admit that. You're still doing your best.",
    ],
}

st.title("💛 Postpartum Companion")
st.write("Select how you're feeling right now.")

mood = st.selectbox("How are you feeling?", MOODS)

if st.button("Get support"):
    st.success(random.choice(VALIDATIONS[mood]))
