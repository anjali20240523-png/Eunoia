# WELLNESS BUDDY
# AI Emotional Wellness Friend
# Developed by [Anjali Joshi], Class 12F

import random
import streamlit as st
# 1. Emotion-based responses
responses = {
    "happy": [
        "That's wonderful! Keep smiling and sharing your joy 😊",
        "Happiness suits you! Spread that positivity 💖",
        "Glad to hear that! You’re doing amazing 🌸",
        "Your energy is contagious! Stay happy always 🌞"
    ],
    "sad": [
        "Hey, it’s okay to feel sad sometimes. Take your time 🕊️",
        "Remember, after every dark night comes a bright morning 🌅",
        "You’re stronger than you think. This feeling will pass 💪",
        "Sending you a virtual hug 🤗 You’re not alone."
    ],
    "neutral": [
        "Got it. Sounds like a calm day 🧘",
        "Alright. Stay balanced and hydrated 💧",
        "Noted! Sometimes normal is peaceful too 🌿",
        "Just another day, huh? Keep going 🌻"
    ],
    "angry": [
        "Take a deep breath. You deserve peace, not stress 🌬️",
        "Try writing down your thoughts; it helps a lot 📝",
        "Anger is valid—but don’t let it control you 🔥"
    ],
    "stressed": [
        "Pause for a moment. Inhale… exhale… you’re doing fine 🌸",
        "It’s okay to rest. You don’t have to do everything at once 🌤️",
        "Remember, your best is enough 💖 Take small steps."
    ]
    "facts" : [
    "That’s an interesting fact 🌍",
    "Good to know! Knowledge always adds perspective.",
    "Facts like these shape how we understand the world.",
    "That’s true — and it’s fascinating when you think about it.",
    "Noted! Would you like to reflect on how this connects to you?"
    ]
    "activity" : [
    "Nice — small routines keep life steady 🌱",
    "That sounds like a healthy habit.",
    "Daily actions may seem small, but they matter.",
    "Good going! Consistency builds balance.",
    "Simple moments like these keep us grounded."
    ]
    }

# 2. Function to detect emotion
def detect_emotion(text):
    text = text.lower()
    if any(word in text for word in ["happy", "joy", "great", "excited", "good","love","like"]):
        return "happy"
    elif any(word in text for word in ["sad", "depressed", "cry", "lonely", "upset","bad","worst"]):
        return "sad"
    elif any(word in text for word in ["angry", "mad", "furious", "annoyed","infuriating","insufferable"]):
        return "angry"
    elif any(word in text for word in ["stress", "tired", "nervous", "anxious", "pressure"]):
        return "stressed"
    elif any(word in text for word in ["brush", "eat", "study", "walk", "sleep", "homework", "exercise"]):
        return "activity"
    elif any(word in text for word in ["fact", "did you know", "information", "tell me"]):
        return "fact"
    else:
        return "neutral"

# 3. Main chat loop
st.title("EUNOIA 🌿")
st.subheader("Your AI Emotional Wellness Buddy")

user_input = st.text_input("How are you feeling today?")

if user_input:
    emotion = detect_emotion(user_input)
    reply = random.choice(responses[emotion])
    st.success(reply)
