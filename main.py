
from core.wake_word import wait_wake_word
from core.executor import execute



while True:
    print("Василич спит🛏")
    wait_wake_word()
    print("👂 Жду команду...")
    execute()
    print("Пора на боковую..")