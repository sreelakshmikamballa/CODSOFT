def chatbot():

    print("Hi! I'm a simple chatbot. How can I help you today?")

    

    while True:

        user_input = input("You: ").strip().lower()

        

        if user_input in ["hello", "hi", "hey"]:

            print("Chatbot: Hello! How can I assist you today?")

        

        elif "name" in user_input:

            print("Chatbot: I'm just a simple chatbot without a name. What's yours?")

        

        elif "how are you" in user_input:

            print("Chatbot: I'm just a bunch of code, but I'm here to help you!")

        

        elif "time" in user_input:

            from datetime import datetime

            now = datetime.now()

            current_time = now.strftime("%H:%M:%S")

            print(f"Chatbot: The current time is {current_time}.")

        

        elif user_input in ["exit", "quit", "bye"]:

            print("Chatbot: Goodbye! Have a great day!")

            break

        

        else:

            print("Chatbot: I'm sorry, I didn't understand that. Can you please rephrase?")



# Run the chatbot

chatbot()