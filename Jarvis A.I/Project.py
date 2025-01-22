import webbrowser
import speech_recognition as sr
import os
import pygame
# import win32com.client
import pyttsx3
# import openai

def say(text):
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()

def play_music():
    musicPath = "Path/music/folder/present/music.mp3"  # Update with the correct path
    if os.path.exists(musicPath):  # Check if the file exists
        pygame.mixer.init()  # Initialize the mixer for audio playback
        pygame.mixer.music.load(musicPath)
        pygame.mixer.music.play()
        print("Playing music...")
    else:
        print("Music file not found.")

def takeCommand():
    r = sr.Recognizer()
    r.pause_threshold=0.8
    with sr.Microphone() as source:
        r.adjust_for_ambient_noise(source)
        try:
            audio = r.listen(source)
            query = r.recognize_google(audio, language="en-in")
            print(f"User said: {query}")
            return query
        except sr.UnknownValueError:
            print("Sorry, I couldn't understand that.")
            return "Sorry, I couldn't understand that."
        except sr.RequestError as e:
            print(f"Could not request results from Google Speech Recognition service; {e}")
            return f"Error: {e}"

if __name__ == '__main__':
    print('Pycharm')
    say("Hello I am Jarvis AI")
    while True:
        print("Listening...")
        _query = takeCommand().lower()
        site = [
            ["youtube", "https://www.youtube.com"],
            ["wikipedia", "https://www.wikipedia.com"],
            ["google", "https://www.google.com"],
            ["amazon", "https://www.amazon.com/?language=en_US&currency=INR"]
        ]
        for s in site:
            if f"open {s[0]}" in _query:
                say(f"Opening {s[0]} dude...")
                webbrowser.open(s[1])
                break

        if "play music" in _query:
            play_music()

        # say(_query)