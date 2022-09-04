import speech_recognition as sr
import re
import os
import pyaudio
import random
import time
import jarvisfront


user_voice = sr.Recognizer()


def take_command():
    try:
        with sr.Microphone() as source:
            user_voice.adjust_for_ambient_noise(source, duration=0.2)
            audio = user_voice.listen(source)
            text = user_voice.recognize_google(audio)
            text = text.lower()
            return text
    except sr.RequestError as e:
        print("Could not request results; {0}".format(e))
        return -1
    except sr.UnknownValueError:
        print("unknown error occurred")
        return -1



def dec_func(text):
    timedatematch = re.search(r"(?:time)|(?:date)", text)
    applicationmatch = re.match(r"(?:open )(.+)", text)
    websitematch = re.match(r"(?:search )(.+) in (.+)", text)
    jokematch = re.search(r"joke", text)
    if timedatematch:
        jarvisfront.TimeAndDate.dec_func(timedatematch.group(0))
        print(timedatematch.group(0))
    elif applicationmatch:
        app = jarvisfront.Applications(applicationmatch.group(1))
        app.open_app()
        if app.status == False:
            new = jarvisfront.Website(applicationmatch.group(1), False)
            new.open_web_and_search()
    elif websitematch:
        new = jarvisfront.Website(websitematch.group(2), websitematch.group(1))
        new.open_web_and_search()
        print(websitematch.group(1), websitematch.group(2))
    elif jokematch:
        jarvisfront.say_a_joke()
    else:
        jarvisfront.speak("The given command is not valid.")
        print("-The given command is not valid")


jarvisfront.speak("Welcome to JarvisFront AI.")
print("-Welcome to JarvisFront AI")
user_command = "open instagram"
while user_command != 0:
    if user_command != -1:
        dec_func(user_command)
    user_command = take_command()
    print("You:", user_command)
