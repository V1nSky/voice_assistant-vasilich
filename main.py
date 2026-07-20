
from core.wake_word import wait_wake_word
from core.executor import execute
from core.speaker import speak



while True:
    print("Василич спит🛏")
    wait_wake_word()
    speak("слушаю!")
    execute()
    print("Пора на боковую..")