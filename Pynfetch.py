import platform
import os
import subprocess
import socket
from colorama import init, Fore
import pyfiglet
import time
import psutil  # Импортируем psutil для проверки процессов

# Инициализация colorama
init(autoreset=True)

def is_music_playing():
    # Проверяем, запущены ли процессы, связанные с воспроизведением музыки
    music_processes = ["wmplayer.exe", "spotify.exe", "iTunes.exe", "vlc.exe", "audacious.exe"]
    for proc in psutil.process_iter(['name']):
        if proc.info['name'].lower() in music_processes:
            return True
    return False

def get_system_info():
    # Получаем информацию о системе
    os_name = platform.system()
    os_version = platform.version()
    os_release = platform.release()
    architecture = platform.architecture()[0]
    machine = platform.machine()
    processor = platform.processor()
    
    # Получаем информацию о пользователе
    username = os.getlogin()
    
    # Получаем информацию о графическом интерфейсе
    try:
        graphics_info = subprocess.check_output("wmic path win32_videocontroller get name", shell=True).decode().strip().split('\n')[1]
    except Exception as e:
        graphics_info = "Не удалось получить информацию о графическом адаптере"

    # Получаем информацию о памяти
    try:
        memory_info = subprocess.check_output("wmic memorychip get capacity", shell=True).decode().strip().split('\n')[1:]
        total_memory = sum(int(mem) for mem in memory_info if mem.isdigit())
        total_memory_gb = total_memory / (1024 ** 3)  # Переводим в ГБ
    except Exception as e:
        total_memory_gb = "Не удалось получить информацию о памяти"

    # Получаем информацию о сети
    hostname = socket.gethostname()
    ip_address = socket.gethostbyname(hostname)

    # Генерируем большой текст "archpacman"
    big_text = pyfiglet.figlet_format("archpacman", font="slant")

    # Проверяем, играет ли музыка
    music_status = "Музыка играет" if is_music_playing() else "Музыка не играет"

    # Форматируем вывод
    info = f"""
    {Fore.RED}{big_text}
    {Fore.RED}OS: {os_name} {os_release} {os_version}
    {Fore.RED}Architecture: {architecture}
    {Fore.RED}Machine: {machine}
    {Fore.RED}Processor: {processor}
    {Fore.RED}:User  {username}
    {Fore.RED}Graphics: {graphics_info}
    {Fore.RED}Total Memory: {total_memory_gb if isinstance(total_memory_gb, str) else f"{total_memory_gb:.2f} GB"}
    {Fore.RED}Hostname: {hostname}
    {Fore.RED}IP Address: {ip_address}
    {Fore.RED}Music Status: {music_status}
    """
    
    return info

if __name__ == "__main__":
    # Очистка экрана
    os.system('cls' if os.name == 'nt' else 'clear')
    
    # Вывод информации о системе
    print(get_system_info())
    input(Fore.RED + "Нажмите Enter для выхода...")

    # Генерируем большой текст "Спасибо, что использовали by archpacman"
    exit_message = pyfiglet.figlet_format("Спасибо, что использовали by archpacman", font="slant")
    os.system('cls' if os.name == 'nt' else 'clear')  # Очистка экрана перед завершением
    print(Fore.RED + exit_message)
    time.sleep(3)  # Ждем 3 секунды перед очисткой экрана
