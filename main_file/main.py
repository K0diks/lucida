import os
import datetime
from save import load_config, save_config, save_data, load_data
from start import start

username = os.getlogin()
folder_path = f"C:\\Users\\{username}\\Documents\\LucidaCode\\config"
save_folder_path = f"C:\\Users\\{username}\\Documents\\LucidaCode\\save"
library_folder_path = f"C:\\Users\\{username}\\Documents\\LucidaCode\\library"
config_path = f"{folder_path}\\default.cfg"
save_file = f"{save_folder_path}\\code.save"
com_deb = False
file_path = ""
variables = {}

def debug_message(message):
    if com_deb:
        print(message)

def clear_console():
    os.system("cls" if os.name == "nt" else "clear")

def reset_data():
    global variables
    variables = {}
    if os.path.exists(save_file):
        os.remove(save_file)
    print("Все сохраненные данные удалены.")

def print_vars():
    print("Переменные:", variables)

def show_help():
    print("""Список команд:
    (список команд)
    """)

def main():
    global com_deb, file_path
    load_config()
    load_data()

    while True:
        com = input("Enter command: ").strip().lower()
        if com == "code start()":
            if not os.path.exists(file_path):
                file_path = input("Введите путь к файлу: ").strip()
                save_config()
            start(file_path)
        elif com == "code debug() true":
            com_deb = True
            save_config()
            print("Debug mode enabled")
        elif com == "code debug() false":
            com_deb = False
            save_config()
            print("Debug mode disabled")
        elif com == "code save()":
            save_data()
            print("Данные сохранены.")
        elif com == "code load()":
            load_data()
            print("Данные загружены:", variables)
        elif com == "code clear()":
            clear_console()
        elif com == "code reset()":
            reset_data()
        elif com == "code print_vars()":
            print_vars()
        elif com == "code help()":
            show_help()
        elif com == "code exit()":
            print("Leaving.")
            break
        else:
            print("Неизвестная команда. Введите code help() для списка команд.")

main()
