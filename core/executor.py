from commands.commands import commands
from core.command import wait_command
from core.speaker import speak
import sys

def execute():
    text = wait_command()
    print("🔥 MAIN ПОЛУЧИЛ:", text)

    found = False

    if "выход" in text:
        speak("Выключаюсь..")
        sys.exit()
    for command in commands:
        print("Проверяю команду:", command)

        if command in text:
            print("✅ НАШЁЛ:", command)

            commands[command]()

            found = True
            break

    if not found:
        speak("Не знаю такую команду")

