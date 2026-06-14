# Day 48 - Voice Assistant

import pyttsx3
import speech_recognition as sr

class VoiceAssistant:

    def __init__(self):

        self.engine = pyttsx3.init()

    def speak(self, text):

        self.engine.say(text)
        self.engine.runAndWait()

    def listen(self):

        recognizer = sr.Recognizer()

        with sr.Microphone() as source:

            print("Listening...")

            recognizer.adjust_for_ambient_noise(source)

            audio = recognizer.listen(source)

        try:

            command = recognizer.recognize_google(audio)

            print(f"\nYou said: {command}")

            return command.lower()

        except Exception:

            return "Sorry, I could not understand."


def main():

    assistant = VoiceAssistant()

    assistant.speak("Hello! I am your Python voice assistant.")

    while True:

        command = assistant.listen()

        if "hello" in command:

            assistant.speak("Hello Vishwanath!")

        elif "time" in command:

            from datetime import datetime

            current_time = datetime.now().strftime("%H:%M")

            assistant.speak(f"The time is {current_time}")

        elif "bye" in command:

            assistant.speak("Goodbye!")
            break

        else:

            assistant.speak("I did not understand that.")


if __name__ == "__main__":
    main()