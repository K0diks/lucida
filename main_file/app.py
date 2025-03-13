import tkinter as tk
import json
import os


# Функция для создания config.json
def create_config():
    config_data = {
        "theme": "dark",  # Устанавливаем тему по умолчанию на dark
        "autoload_last_project": True,
        "library_path": f"C:/Users/{os.getlogin()}/Documents/Lucida/libs"
    }

    # Путь, куда сохранить config.json
    config_folder = f"C:/Users/{os.getlogin()}/Documents/LucidaCode/config"
    if not os.path.exists(config_folder):
        os.makedirs(config_folder)

    config_path = os.path.join(config_folder, "config.json")

    # Запись данных в файл config.json
    with open(config_path, 'w') as config_file:
        json.dump(config_data, config_file, indent=4)

    print(f"Файл конфигурации создан: {config_path}")


# Функция для загрузки конфигурации
def load_config():
    config_folder = f"C:/Users/{os.getlogin()}/Documents/LucidaCode/config"
    config_path = os.path.join(config_folder, "config.json")

    if os.path.exists(config_path):
        with open(config_path, 'r') as config_file:
            config_data = json.load(config_file)
        return config_data
    else:
        print("Конфигурационный файл не найден. Создаем новый.")
        create_config()
        return load_config()  # Рекурсивно пытаемся снова загрузить конфигурацию


# Функция для применения темы
def apply_theme(root, theme):
    if theme == "dark":
        root.config(bg="black")
        root.option_add("*Foreground", "white")
        root.option_add("*Background", "black")
    elif theme == "light":
        root.config(bg="white")
        root.option_add("*Foreground", "black")
        root.option_add("*Background", "white")
    else:
        print("Неизвестная тема. Установлена светлая тема по умолчанию.")
        apply_theme(root, "light")


# Функция для запуска приложения
def open_app():
    print("Запуск приложения...")

    # Загрузка конфигурации
    config_data = load_config()
    theme = config_data.get("theme", "light")  # Если тема не указана, по умолчанию будет light

    # Создаем окно приложения и применяем тему
    root = tk.Tk()
    root.title("Главное окно")
    root.geometry("400x200")  # Размер окна

    apply_theme(root, theme)  # Применяем тему

    # Создаем кнопки
    console_button = tk.Button(root, text="Console", command=open_console)
    console_button.pack(pady=10)

    app_button = tk.Button(root, text="App", command=open_app)
    app_button.pack(pady=10)

    # Запуск окна
    root.mainloop()


# Функция для открытия консоли
def open_console():
    print("Запуск консоли...")


# Функция для создания окна с кнопками
# Функция для запуска окна
if __name__ == "__main__":
    create_window()

