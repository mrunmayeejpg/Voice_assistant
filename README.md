🎤 Voice Assistant — “Yo Gang” Edition
🧠 Overview

This is a Python-based voice-controlled desktop assistant with a twist — it wakes up when you say “Gang” or “Yo Gang” 😎

It listens to your voice, recognizes commands, and opens desktop apps like Notepad, Chrome, Paint, and Calculator — all while responding with friendly confirmations like “Yes Ma’am” or “App not installed, bruh.”

Built using SpeechRecognition, SoundDevice, and pyttsx3, it blends practicality with personality — your very own talking assistant with attitude.

⚙️ Features

✅ Voice-activated using wake words → "Gang" or "Yo Gang"
✅ Opens desktop apps via speech commands
✅ Real-time speech recognition (Google Speech API)
✅ Fun, personalized text-to-speech responses
✅ Works offline for TTS (pyttsx3)
✅ Simple and customizable

🧩 Supported Commands
Command	Action
“Open Notepad”	Launches Notepad
“Open Chrome”	Launches Google Chrome
“Open Paint”	Opens Microsoft Paint
“Open Calculator”	Opens Calculator
Anything else	“I didn’t catch that, bruh.” 😅
🚀 Setup & Usage
1️⃣ Install Dependencies

Open your terminal and run:

pip install sounddevice numpy SpeechRecognition pyttsx3


(If you face issues, install pyaudio too:)

pip install pipwin
pipwin install pyaudio

2️⃣ Run the Script

If your file is saved as test_voice.py (on Desktop for example):

cd "%userprofile%\Desktop"
python test_voice.py

🎧 How It Works

Continuously records short audio samples.

Checks for wake words (“gang” / “yo gang”).

When heard, responds with “Yes Ma’am”.

Listens for a follow-up command and executes it.

If the command doesn’t match, replies with “I didn’t catch that, bruh.” 😂

🧠 Behind the Scenes

SoundDevice records live microphone input.

SpeechRecognition (Google API) converts speech to text.

pyttsx3 speaks responses aloud.

os.startfile() opens Windows apps directly.

NumPy helps manage raw audio data for smooth recognition.

💡 Future Ideas

Add “close app” or “search on Google” commands.

Add background listening with hotword detection (Snowboy or Porcupine).

Integrate with GPT for smarter responses.

Create a GUI or voice dashboard.

🙌 Author

Developed by Mrunmayee Kulat
A chill, responsive, and slightly sassy voice assistant that listens when you say —

🗣️ “Yo Gang!” 🎧
