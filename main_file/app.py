import tkinter as tk
import threading
import os
import datetime
from save import load_config, save_config, save_data, load_data
from start import start

# Эта функция будет вызываться при нажатии кнопки "Console"
def open_console():
    print("Запуск консоли...")
    
    # Импортируем main.py и вызываем main() в новом потоке, чтобы не блокировать GUI
    import main
    threading.Thread(target=main.main).start()

def open_app():
    print("Запуск приложения...")

def create_window():
    # Создаем главное окно
    root = tk.Tk()
    root.title("Главное окно")

    # Создаем кнопки
    console_button = tk.Button(root, text="Console", command=open_console)
    console_button.pack(pady=10)

    app_button = tk.Button(root, text="App", command=open_app)
    app_button.pack(pady=10)

    # Запуск окна
    root.mainloop()

# Функция для запуска окна
if __name__ == "__main__":
    create_window()

