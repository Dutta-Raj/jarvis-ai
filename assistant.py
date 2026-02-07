from wake import listen_for_wake_word
from automation import type_text, shutdown_pc, restart_pc, open_notepad, open_chrome, open_vscode
import requests
import pyttsx3
import speech_recognition as sr
import datetime
import webbrowser
import os
import subprocess

engine = pyttsx3.init()

def speak(text):
    print("Jarvis:", text)
    engine.say(text)
    engine.runAndWait()
def ask_ollama(prompt):
    url = "http://localhost:11434/api/generate"

    data = {
        "model": "llama3",
        "prompt": prompt,
        "stream": False
    }

    response = requests.post(url, json=data)
    result = response.json()

    return result["response"]


def wish():
    hour = int(datetime.datetime.now().hour)
    if hour < 12:
        speak("Good Morning")
    elif hour < 18:
        speak("Good Afternoon")
    else:
        speak("Good Evening")

def take_command():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        query = r.recognize_google(audio, language="en-in")
        print("You:", query)
        return query.lower()
    except:
        speak("Say that again please")
        return "none"

def open_telegram():
    path = r"C:\Users\KIIT\AppData\Roaming\Telegram Desktop\Telegram.exe"
    os.startfile(path)

def run_jarvis():
    speak("System ready")
    while True:
        query = take_command()

        if "exit" in query or "stop" in query or "shutdown" in query:
            speak("Goodbye sir")
            break

        elif "open youtube" in query:
            webbrowser.open("https://youtube.com")

        elif "open google" in query:
            webbrowser.open("https://google.com")

        elif "time" in query:
            time = datetime.datetime.now().strftime("%H:%M")
            speak("Time is " + time)

        elif "open telegram" in query:
            open_telegram()

        else:
            speak("Thinking...")
            reply = ask_ollama(query)
            print("AI:", reply)
            speak(reply)


if __name__ == "__main__":
    run_jarvis()
