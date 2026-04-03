import random
import datetime

LOG_FILE = "chat_history.txt"

user_data = {
    "name": None
}

# Knowledge base
knowledge_base = {
    "python": "Python is a powerful programming language used in AI, web, and automation.",
    "ai": "AI stands for Artificial Intelligence.",
    "chatbot": "A chatbot is a program that simulates conversation.",
    "cloud": "Cloud computing allows storing and accessing data over the internet.",
    "iot": "IoT means Internet of Things, connecting devices to the internet."
}

# More intents added
intents = {
    "greeting": {
        "patterns": ["hi", "hello", "hey", "hii", "heyy", "good morning", "good evening", "good afternoon"],
        "responses": ["Hello!", "Hi there!", "Hey! Nice to meet you!"]
    },
    "farewell": {
        "patterns": ["bye", "goodbye", "see you", "see you later", "talk to you later", "exit"],
        "responses": ["Goodbye!", "See you soon!", "Take care!"]
    },
    "help": {
        "patterns": ["help", "can you help me", "i need help", "what can you do", "support"],
        "responses": ["I can chat, answer questions, remember your name, tell time, and more!"]
    },
    "smalltalk": {
        "patterns": ["how are you", "how are you doing", "what's up", "how's it going"],
        "responses": ["I'm doing great!", "All good! What about you?"]
    },
    "thanks": {
        "patterns": ["thanks", "thank you", "thx", "thanks a lot", "thank you so much"],
        "responses": ["You're welcome!", "No problem!", "Happy to help!"]
    },
    "creator": {
        "patterns": ["who made you", "who created you", "who is your developer", "who built you"],
        "responses": ["I was created by a smart developer like you!"]
    },
    "age": {
        "patterns": ["your age", "how old are you", "what is your age"],
        "responses": ["I don't have an age, I'm just code!"]
    },
    "joke": {
        "patterns": ["tell me a joke", "joke", "make me laugh", "say something funny"],
        "responses": [
            "Why do programmers prefer dark mode? Because light attracts bugs!",
            "Why did the computer go to the doctor? Because it caught a virus!"
        ]
    },
    "study": {
        "patterns": ["study", "exam", "how to study", "study tips", "prepare for exam"],
        "responses": ["Stay consistent, revise daily, and practice problems. You will succeed!"]
    },
    "time": {
        "patterns": ["time", "current time", "what time is it", "tell me time"],
        "responses": []
    }
}


# Logging
def log_conversation(user, bot):
    with open(LOG_FILE, "a", encoding="utf-8") as f:
        f.write(f"{datetime.datetime.now()}\nUser: {user}\nBot: {bot}\n\n")

# Response logic
def get_response(user_input):
    user_input = user_input.lower()

    # Name storing
    if "my name is" in user_input:
        name = user_input.replace("my name is", "").strip().title()
        user_data["name"] = name
        return f"Nice to meet you, {name}!"

    # Name recall
    if "what is my name" in user_input:
        if user_data["name"]:
            return f"Your name is {user_data['name']}!"
        else:
            return "I don't know your name yet."

    # Time
    if "time" in user_input:
        return "Current time is " + datetime.datetime.now().strftime("%H:%M:%S")

    # Intent matching
    for intent in intents:
        for pattern in intents[intent]["patterns"]:
            if pattern in user_input:
                return random.choice(intents[intent]["responses"])

    # Knowledge base
    for key in knowledge_base:
        if key in user_input:
            return knowledge_base[key]

    return "Sorry, I didn't understand that."

# Start chatbot
print("Chatbot started! Type 'exit' to stop.\n")

while True:
    user_input = input("You: ")

    if user_input.lower() in ["exit", "bye", "quit"]:
        print("Bot: Goodbye!")
        log_conversation(user_input, "Goodbye!")
        break

    response = get_response(user_input)
    print("Bot:", response)

    log_conversation(user_input, response)

