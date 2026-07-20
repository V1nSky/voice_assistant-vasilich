from core.voice import listen


def wait_command():
    while True:
        text = listen()

        if text:
            return text