# main.py

import os
import sys
import subprocess

# --- Auto install missing packages ---
def install(package):
    subprocess.check_call([sys.executable, "-m", "pip", "install", package])

try:
    import speech_recognition as sr
except ImportError:
    install("SpeechRecognition")
    import speech_recognition as sr

try:
    import openai
except ImportError:
    install("openai")
    import openai

# Optional: install pyaudio (for voice)
try:
    import pyaudio
except ImportError:
    try:
        install("PyAudio")
        import pyaudio
    except:
        print("⚠️  PyAudio installation failed. Voice input might not work.")
        sr = None

from nlp_interface.gemini_client import GeminiClient
from nlp_interface.command_parser import CommandParser
from robot_controller.task_executor import TaskExecutor

def get_voice_input():
    if sr is None:
        return None

    recognizer = sr.Recognizer()
    mic = sr.Microphone()

    with mic as source:
        print("\n🎤 Listening for your command...")
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)

    try:
        command = recognizer.recognize_google(audio)
        print(f"🗣️  You said: {command}")
        return command
    except sr.UnknownValueError:
        print("🤷 Could not understand audio.")
    except sr.RequestError:
        print("🚫 Could not request results from Google Speech Recognition.")

    return None

def get_text_input():
    return input("\n🖋️  Type your command for the robot (or 'exit' to quit):\n> ")

def main():
    print("\n🤖 Robot System Booting Up...")

    gemini = GeminiClient()
    parser = CommandParser()
    executor = TaskExecutor()

    try:
        while True:
            # Step 1: Get input (voice first if possible)
            prompt = None
            if sr is not None:
                print("\n[MODE] Voice input enabled 🎙️")
                prompt = get_voice_input()

            if prompt is None:
                print("\n[MODE] Using text input 🖋️")
                prompt = get_text_input()

            if prompt.lower() == 'exit':
                print("\n👋 Exiting robot control...")
                break

            # Step 2: Send to Gemini
            gemini_response = gemini.ask_gemini(prompt)
            print(f"\n📜 Gemini Response: {gemini_response}")

            # Step 3: Parse response
            command = parser.parse(gemini_response)
            print(f"\n🔍 Parsed Command: {command}")

            # Step 4: Execute command
            executor.execute(command)

    except KeyboardInterrupt:
        print("\n⚡ Interrupted by user. Shutting down...")
        sys.exit(0)

if __name__ == "__main__":
    main()
