import platform
import os
import subprocess
import socket
from colorama import init, Fore

# Инициализация colorama
init(autoreset=True)

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

    # Форматируем вывод
    info = f"""
    {Fore.RED}NeofetchARCH
    {Fore.RED}{os_name} {os_release} {os_version}
    {Fore.RED}Architecture: {architecture}
    {Fore.RED}Machine: {machine}
    {Fore.RED}Processor: {processor}
    {Fore.RED}:User  {username}
    {Fore.RED}Graphics: {graphics_info}
    {Fore.RED}Total Memory: {total_memory_gb if isinstance(total_memory_gb, str) else f"{total_memory_gb:.2f} GB"}
    {Fore.RED}Hostname: {hostname}
    {Fore.RED}IP Address: {ip_address}
    """
    
    return info

if __name__ == "__main__":
    print(get_system_info())
    input(Fore.RED + "Нажмите Enter для выхода...")