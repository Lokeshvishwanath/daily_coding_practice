# Day 30 - AI Chatbot using Python

import random

class SimpleChatBot:

    def __init__(self):
        self.responses = {
            "hello": [
                "Hi there!",
                "Hello!",
                "Hey!"
            ],

            "how are you": [
                "I'm doing great!",
                "All good!",
                "I'm fine, thanks!"
            ],

            "bye": [
                "Goodbye!",
                "See you later!",
                "Take care!"
            ]
        }

    def get_response(self, message):

        message = message.lower()

        for key in self.responses:
            if key in message:
                return random.choice(self.responses[key])

        return "Sorry, I don't understand that."

    def start_chat(self):

        print("===== AI CHATBOT =====")
        print("Type 'bye' to exit.\n")

        while True:

            user_message = input("You: ")

            bot_reply = self.get_response(user_message)

            print("Bot:", bot_reply)

            if "bye" in user_message.lower():
                break


def main():

    chatbot = SimpleChatBot()

    chatbot.start_chat()


if __name__ == "__main__":
    main()