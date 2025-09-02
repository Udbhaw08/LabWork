def chatbot():
    print("Chatbot: Hello! I am a simple Python chatbot. What is your name?")
    name = input("You: ")
    print(f"Chatbot: Nice to meet you, {name}! How can I help you today?")
    
    while True:
        user_input = input(f"{name}: ").lower()

        if "bye" in user_input:
            print(f"Chatbot: Goodbye, {name}! Have a great day.")
            break
        elif "hello" in user_input or "hi" in user_input:
            print(f"Chatbot: Hello there, {name}!")
        elif "how are you" in user_input:
            print("Chatbot: I'm just a program, but I'm doing great! Thanks for asking.")
        elif "your name" in user_input:
            print("Chatbot: You can call me PyBot.")
        elif "weather" in user_input:
            print("Chatbot: I can't check the weather, but I hope it's nice where you are!")
        else:
            print("Chatbot: I'm not sure how to respond. You can ask me my name or how I am.")

chatbot()
