import webbrowser
import subprocess

def open_youtube():
    url = "https://www.youtube.com"
    webbrowser.open(url)
    print("Открываю YouTube 😎")

def open_downloads():
    path_downloads = r"/Users/vqns/Downloads"
    subprocess.Popen(["open", path_downloads])
    print("Открываю Загрузки 👀")
    

def open_vpn():
    path_happ = r"/Applications/Happ.app"
    subprocess.Popen(["open", path_happ])
    print("Переехал в другую страну 🇳🇱")

def open_telegram():
    path_telegram = r"/Applications/Telegram.app"
    subprocess.Popen(["open", path_telegram])
    print("Открываю Telegram 👨🏼‍💻")

def open_music():
    path_yandex_music = r"/Applications/Яндекс Музыка.app"
    subprocess.Popen(["open", path_yandex_music])
    print("Открываю Yandex Music ☥")


commands = {
    "ютуб": open_youtube,
    "youtube": open_youtube,
    "YouTube": open_youtube,
    "видео": open_youtube,
    "ролики":  open_youtube,
    "vpn": open_vpn,
    "впн": open_vpn,
    "загрузки": open_downloads,
    "telegram": open_telegram,
    "музыка": open_music, 
    "музыку": open_music,
    "музычку": open_music,
    "сообщения": open_telegram,
    "сообщение": open_telegram,
    "написали": open_telegram
}