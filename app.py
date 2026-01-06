# WELLNESS BUDDY
# AI Emotional Wellness Friend
# Developed by [Anjali Joshi], Class 12F

import random

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
}

# 2. Function to detect emotion
def detect_emotion(text):
  x  text = text.lower()
    if any(word in text for word in ["happy", "joy", "great", "excited", "good","love","like"]):
        return "happy"
    elif any(word in text for word in ["sad", "depressed", "cry", "lonely", "upset","bad","worst"]):
        return "sad"
    elif any(word in text for word in ["angry", "mad", "furious", "annoyed","infuriating","insufferable"]):
        return "angry"
    elif any(word in text for word in ["stress", "tired", "nervous", "anxious", "pressure"]):
        return "stressed"
    else:
        return "neutral"

# 3. Main chat loop
print("💬 Wellness Buddy 2.0 is here to talk to you 💬")
print("Type 'bye' anytime to end the chat.\n")

while True:
    user_input = input("You: ")
    if user_input.lower() == "bye":
        print("Wellness Buddy: Take care of yourself 💚 Bye!")
        break

    emotion = detect_emotion(user_input)
    reply = random.choice(responses[emotion])
    print(f"Wellness Buddy ({emotion.title()}): {reply}\n")# WELLNESS BUDDY
        "You’re stronger than you think. This feeling will pass 💪",
        "Sending you a virtual hug 🤗 You’re not alone.") 
    
