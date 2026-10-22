
while True:
    message = input("You: ").lower()

    if message == "hello":
        print("Bot: Hello! How can I help you?")
    elif message == "what is ai":
        print("Bot: AI helps machines perform tasks that require intelligence.")
    elif message == "bye":
        print("Bot: Goodbye!")
        break
    else:
        print("Bot: Sorry, I don't understand that yet.")
