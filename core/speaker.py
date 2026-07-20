import subprocess

def speak(text):
    subprocess.run([
        "say",
        "-v",
        "Yuri",
        "-r"
        "250",
        text
    ])