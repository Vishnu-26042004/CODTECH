import nltk
import random
from nltk.tokenize import word_tokenize

nltk.download("punkt")

responses = {
    "greeting": ["Hello!", "Hi there!", "Hey!", "Hi! How can I help you?"],
    "farewell": ["Goodbye!", "See you later!", "Take care!"],
    "name": ["I'm a chatbot created using NLTK.", "You can call me ChatBot!"],
    "help": ["I can answer basic queries. Try asking about my name or greeting me!"],
    "default": ["I'm not sure how to respond to that.", "Can you rephrase your question?"]
}

patterns = {
    "greeting": ["hello", "hi", "hey"],
    "farewell": ["bye", "goodbye", "see you"],
    "name": ["your name", "who are you"],
    "help": ["help", "what can you do"]
}

def get_intent(user_input):
    tokens = word_tokenize(user_input.lower())
    for intent, keywords in patterns.items():
        if any(word in tokens for word in keywords):
            return intent
    return "default"

def chatbot():
    print("ChatBot: Hello! Type 'exit' to stop.")
    while True:
        user_input = input("You: ")
        if user_input.lower() == "exit":
            print("ChatBot:", random.choice(responses["farewell"]))
            break
        intent = get_intent(user_input)
        print("ChatBot:", random.choice(responses[intent]))

if __name__ == "__main__":
    chatbot()
