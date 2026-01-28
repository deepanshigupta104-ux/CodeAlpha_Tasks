print("🤖 Welcome to Simple Chatbot!")
print("You can talk to me. Type 'bye' to exit.\n")

# Dictionary of predefined responses
responses = {
    "hello": "Hello! 😄 How are you?",
    "how are you": "I'm good! 😎 What about you?",
    "i am fine": "Great to hear! 👍",
    "what is your name": "I'm Chatty 🤖, your mini friend!",
    "tell me a joke": "Why did the computer go to the doctor? 😅 Because it caught a virus!",
    "what can you do": "I can chat with you and tell jokes 😎",
    "how old are you": "Age is just a number 😉",
    "bye": "Bye! 👋 Have a nice day!"
}

while True:
    user_input = input("You:").lower().strip()  # Remove extra spaces and lowercase

    if user_input in responses:
        print(f"Bot: {responses[user_input]}")
        if user_input == "bye":
            break
    else:
        print("Bot: Sorry, I don't understand 😅 Try asking something else!")

