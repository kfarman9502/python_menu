import speech_recognition as sr
import subprocess
import os
import pyttsx3
import pywhatkit
import random
import datetime
from PIL import Image

def speak(text):
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()

def recognize_speech():
    # Initialize the recognizer
    recognizer = sr.Recognizer()

    # Using the default system microphone as the audio source
    with sr.Microphone() as source:
        print("Listening...")
        audio = recognizer.listen(source)
        

    try:
        # Recognize the speech using Google Web Speech API
        recognized_text = recognizer.recognize_google(audio)
        print("You said: " , recognized_text)
        

        # Execute corresponding actions based on recognized_text
        if "don't" in recognized_text or "do not" in recognized_text or "not" in recognized_text:
            print("Try something else")
        else:
            if "editor" in recognized_text:
                subprocess.run(["notepad.exe"])
            elif "calculator" in recognized_text:
                subprocess.run(["calc.exe"])
            elif "ms paint" in recognized_text: 
                os.system("mspaint")
            elif "open browser" in recognized_text:
                subprocess.run(["start", "https://www.google.com"])
            elif "play music" in recognized_text:
                pywhatkit.playonyt("Best of Arijit Singh 2020 superhit romantic and sad song Arijit Singh")
            elif "tell a joke" in recognized_text:
                jokes = [
                    "Why don't scientists trust atoms? Because they make up everything!",
                    "Did you hear about the mathematician who’s afraid of negative numbers? He’ll stop at nothing to avoid them!",
                    "Why don’t some couples go to the gym? Because some relationships don’t work out!",
                    "Why did the scarecrow win an award? Because he was outstanding in his field!",
                    "Parallel lines have so much in common. It’s a shame they’ll never meet!",
                ]
                joke = random.choice(jokes)
                print("Assistant:", joke)
                speak(joke)
            elif "tell the time" in recognized_text:
                now = datetime.datetime.now().strftime("%I:%M %p")
                print("Assistant:", now)
                speak(f"The current time is {now}.")
            elif "open code editor" in recognized_text:
                subprocess.run(["code"])  # Assuming 'code' is the command to open your code editor (e.g., Visual Studio Code)
            
            elif "exit" in recognized_text or "quit" in recognized_text:
                print("Exiting the assistant. Goodbye!")
                speak("Exiting the assistant. Goodbye!")
                exit()
            else:
                print("Command not recognized. Try saying one of the supported commands.")
                speak("Command not recognized. Try saying one of the supported commands.")

        return recognized_text  # Return the recognized text

    except sr.UnknownValueError:
        print("Sorry, could not understand audio.")
        return ""  # Return an empty string if the recognition failed
    except sr.RequestError as e:
        print("Error accessing Google Speech Recognition service; {0}".format(e))
        return ""  # Return an empty string if there was an error

if __name__ == "__main__":
    speak("Hello! I am your creative assistant. How can I help you?")
    while True:
        recognized_text = recognize_speech()  # Get the recognized text from the function
        if "goodbye" in recognized_text.lower():
            print("Goodbye! Stopping the assistant.")
            speak("Goodbye! Stopping the assistant.")
            break
