from core.voice import listen
from core.speaker import speak

wake_words = [
    "василич",
    "василь",
    "василье",
    "васик",
    "васильевич",
    "vasile",
    "Васи"

] 

def wait_wake_word():
    while True:

        text = listen()

        if text in wake_words:
            break
