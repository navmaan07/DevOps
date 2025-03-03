# Simple Rule-based Chatbot

def chatbot_response(user_input):
    # Convert input to lowercase to make it case-insensitive
    user_input = user_input.lower()

    # Define responses based on user input patterns
    if "hello" in user_input or "hi" in user_input:
        return "Hello! How can I assist you today?"
    
    elif "how are you" in user_input:
        return "I'm just a bot, but I'm doing great! How about you?"
    
    elif "bye" in user_input or "goodbye" in user_input:
        return "Goodbye! Have a great day!"
    
    elif "name" in user_input:
        return "I am a chatbot, created to assist you."
    
    elif "your favorite color" in user_input:
        return "I don't have a favorite color, but I think blue is nice!"
    
    elif "what can you do" in user_input:
        return "I can answer questions, chat with you, and help with simple tasks!"
    
    elif "help" in user_input:
        return "Sure! How can I assist you? Just ask me anything!"
    
    # Default response if no rules match
    else:
        return "Sorry, I didn't understand that. Can you please rephrase?"

# Chatbot loop to interact with the user
def start_chat():
    print("Hello! I'm your chatbot. Type 'exit' to end the conversation.")
    
    while True:
        user_input = input("You: ")
        
        if user_input.lower() == "exit":
            print("Bye! Have a nice day!")
            break
        
        response = chatbot_response(user_input)
        print("Bot:", response)

# Run the chatbot
if __name__ == "__main__":
    start_chat()
