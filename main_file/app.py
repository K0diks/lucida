import tkinter as tk

def open_console():
    print("Консоль открыта!")

def open_app():
    print("Приложение открыто!")

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
