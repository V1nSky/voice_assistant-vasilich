from core.speaker import speak
import speech_recognition as sr


def listen():
    recognizer = sr.Recognizer()

    with sr.Microphone() as source:
        audio = recognizer.listen(source)

    try:
        text = recognizer.recognize_google(audio, language="ru-RU")
        return text.lower()

    except:
        return ""
    