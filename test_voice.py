
#cd "%userprofile%\Desktop"
#python test_voice.py

import sounddevice as sd
import numpy as np
import speech_recognition as sr
import pyttsx3
import os
import time  # for small delay to ensure speech is heard

# Initialize text-to-speech
engine = pyttsx3.init()

# Initialize speech recognizer
r = sr.Recognizer()

def speak(text):
    engine.say(text)
    engine.runAndWait()  # ensure speaking finishes before continuing

def record_audio(duration=5, fs=44100):
    print("Recording...")
    audio = sd.rec(int(duration * fs), samplerate=fs, channels=1, dtype='int16')
    sd.wait()
    return audio.flatten(), fs

def recognize_speech(audio_data, fs):
    audio_np = sr.AudioData(audio_data.tobytes(), fs, 2)  # 2 bytes per sample
    try:
        text = r.recognize_google(audio_np)
        return text.lower()
    except Exception:
        return ""

def open_app(command):
    if "notepad" in command:
        if os.path.exists("C:\\Windows\\System32\\notepad.exe"):
            speak("Yes Maam, opening Notepad!")  # speak first
            time.sleep(0.2)
            os.startfile("C:\\Windows\\System32\\notepad.exe")
        else:
            speak("App is not installed, bruh.")
    elif "chrome" in command:
        chrome_path = "C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe"
        if os.path.exists(chrome_path):
            speak("Yes Maam, opening Chrome!")
            time.sleep(0.2)
            os.startfile(chrome_path)
        else:
            speak("App is not installed, bruh.")
    elif "paint" in command:
        paint_path = "C:\\Windows\\System32\\mspaint.exe"
        if os.path.exists(paint_path):
            speak("Yes Maam, opening Paint!")
            time.sleep(0.2)
            os.startfile(paint_path)
        else:
            speak("App is not installed, bruh.")
    elif "calculator" in command:
        calc_path = "C:\\Windows\\System32\\calc.exe"
        if os.path.exists(calc_path):
            speak("Yes Maam, opening Calculator!")
            time.sleep(0.2)
            os.startfile(calc_path)
        else:
            speak("App is not installed, bruh.")
    else:
        speak("I didn't catch that, bruh.")

# Main loop
while True:
    # Listen for wake word
    audio_data, fs = record_audio(duration=3)  # 3 sec listening
    text = recognize_speech(audio_data, fs)
    print("You said:", text)

    # Fuzzy wake word detection
    wake_words = ["gang","yo gang"]
    if any(wake_word in text for wake_word in wake_words):
        speak("Yes Maam")  # Wake word response

        # Listen for actual command
        audio_data, fs = record_audio(duration=5)
        command = recognize_speech(audio_data, fs)
        print("Command:", command)
        if command:
            open_app(command)
        else:
            speak("I didn't catch that, bruh.")
