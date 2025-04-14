import random

responses = {
    "hello": "Hi there!",
    "how are you": "I'm just a bunch of code, but I'm doing great!",
    "bye": "Goodbye! Have a great day!",
    "default": "I'm not sure how to respond to that."
}

def chatbot_response(user_input):
    user_input = user_input.lower()
    return responses.get(user_input, responses["default"])

while True:
    user_input = input("You: ")
    if user_input.lower() == "exit":
        print("Chatbot: Goodbye!")
        break
    print("Chatbot:", chatbot_response(user_input))
