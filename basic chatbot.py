"""
CodeAlpha Python Programming Internship
Task 4: Basic Rule-Based Chatbot
Description: A simple text-based console chatbot that responds to user inputs 
             based on predefined rules and keyword matching.
"""

def get_chatbot_response(user_input: str) -> str:
    """
    Evaluates the sanitized user input against predefined rules 
    and returns the corresponding chatbot response.
    """
    # 1. Check for Exit/Goodbye commands
    if "bye" in user_input or "exit" in user_input or "quit" in user_input:
        return "Goodbye! Have a wonderful day!"
        
    # 2. Check for Greetings
    elif "hello" in user_input or "hi" in user_input or "hey" in user_input:
        return "Hello there! How can I help you today?"
        
    # 3. Check for Status/Well-being questions
    elif "how are you" in user_input or "how's it going" in user_input:
        return "I'm just a computer program, but I'm functioning perfectly! Thank you for asking. How are you doing?"
        
    # 4. Check for Identity/Name questions
    elif "your name" in user_input or "who are you" in user_input:
        return "I am a basic rule-based chatbot created for the CodeAlpha internship task."
        
    # 5. Check for Help/Capabilities
    elif "help" in user_input or "what can you do" in user_input:
        return "I can chat with you! Try saying hello, asking how I am, or asking for my name. Type 'bye' to exit."
        
    # 6. Fallback response if no rules/keywords match
    else:
        return "I'm sorry, I don't quite understand that. Could you try phrasing it differently or type 'help'?"


def start_chatbot():
    """
    Main driver function to run the chatbot loop, handle console I/O, 
    and clean user input strings.
    """
    print("=" * 50)
    print("   Welcome to the CodeAlpha Rule-Based Chatbot!   ")
    print("      (Type 'bye', 'exit', or 'quit' to stop)     ")
    print("=" * 50)
    
    # Infinite conversation loop
    while True:
        # Prompt user for input and handle potential keyboard interrupts gracefully
        try:
            user_raw_input = input("\nYou: ")
        except (KeyboardInterrupt, EOFError):
            print("\nChatbot: Program interrupted. Goodbye!")
            break
            
        # Sanitize input: convert to lowercase and strip leading/trailing whitespace
        clean_input = user_raw_input.lower().strip()
        
        # Avoid processing empty inputs (if user just presses Enter)
        if not clean_input:
            print("Chatbot: Please type something so we can chat!")
            continue
            
        # Fetch the response based on our rules
        response = get_chatbot_response(clean_input)
        
        # Display the response to the user
        print(f"Chatbot: {response}")
        
        # Break the infinite loop if the chatbot issued the goodbye sequence
        if "goodbye" in response.lower():
            break

    print("\n[Chatbot Session Ended Successfully]")
    print("=" * 50)


# Entry point of the script
if __name__ == "__main__":
    start_chatbot()