import speech_recognition as sr
import pyaudio

def listen():
    recognizer = sr.Recognizer()

    with sr.Microphone() as source:
        audio = recognizer.listen(source)

    try:
        text = recognizer.recognize_google(audio, language="ru-RU")
        print(f"Ты сказал: {text}")
        return text.lower()

    except:
        print("Не расслышал 😅")
        return ""
    