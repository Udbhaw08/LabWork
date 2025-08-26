def chatbot():
    print(" Hello! I'm your friendly chatbot. Type 'exit' to end the chat.")
    
    while True:
            user_input = input("You: ").strip().lower()
            
            if user_input == "exit":
                print("Bot: Goodbye! Have a great day ")
                break
            elif user_input == "":
                print("Bot: Hmm, you didn’t say anything. Try again!")
            elif "hello" in user_input or "hi" in user_input:
                print("Bot: Hey there! How can I help you today?")
            elif "how are you" in user_input:
                print("Bot: I'm just code, but I'm running smoothly! What about you?")
            elif "joke" in user_input:
                print("Bot: Why don’t scientists trust atoms? Because they make up everything! ")
            else:
                print("Bot: I’m not sure how to respond to that. Try asking something else!")
chatbot()