from commands.commands import commands
from core.command import wait_command
import sys

def execute():
    text = wait_command()
    print("🔥 MAIN ПОЛУЧИЛ:", text)

    found = False

    if "выход" in text:
        print("Пора на боковую..")
        sys.exit()
    for command in commands:
        print("Проверяю команду:", command)

        if command in text:
            print("✅ НАШЁЛ:", command)

            commands[command]()

            found = True
            break

    if not found:
        print("❌ Не знаю такую команду")

