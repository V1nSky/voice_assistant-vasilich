from core.voice import listen

wake_words = [
    "василич",
    "василь",
    "василье",
    "васик",
    "васильевич"
] 

def wait_wake_word():
    while True:

        text = listen()

        if text in wake_words:
            print("🟢 Василич тута!")
            break
