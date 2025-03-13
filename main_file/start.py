# start.py
import os
import datetime

variables = {}

def start(file_path):
    global variables
    if not os.path.exists(file_path):
        print("Файл не найден.")
        return

    with open(file_path, "r") as file:
        lines = [line.strip() for line in file.readlines()]

    i = 0
    while i < len(lines):
        line = lines[i]

        if not line:
            i += 1
            continue

        # Объявление переменной
        if line.startswith("var "):
            parts = line.split("=")
            if len(parts) == 2:
                variable_name = parts[0].replace("var", "").strip()
                value = parts[1].strip()
                if value.isdigit():
                    value = int(value)
                elif value.replace(".", "", 1).isdigit():
                    value = float(value)
                elif value.lower() == "true":
                    value = True
                elif value.lower() == "false":
                    value = False
                else:
                    value = value.strip('"')
                variables[variable_name] = value

        # Обработка print()
        elif line.startswith("print(") and line.endswith(")"):
            content = line[6:-1].strip()
            if content.startswith('"') and content.endswith('"'):
                print(content.strip('"'))  # Вывод текста
            elif content in variables:
                print(variables[content])  # Вывод значения переменной
            else:
                print("Ошибка: переменная не найдена")

        # Обработка if-условий
        elif line.startswith("if "):
            condition = line[3:].strip()
            block_lines = []

            # Проверяем, есть ли сразу `{` или на новой строке
            if i + 1 < len(lines) and lines[i + 1] == "{":
                i += 2  # Пропускаем строку с `{`
            else:
                print("Ошибка: после if должна быть {")
                return

            # Собираем строки внутри {}
            while i < len(lines) and lines[i] != "}":
                block_lines.append(lines[i])
                i += 1

            # Подставляем переменные в условие
            condition_eval = condition
            for var in variables:
                condition_eval = condition_eval.replace(var, str(variables[var]))

            try:
                if eval(condition_eval):  # Проверяем условие
                    for block_line in block_lines:
                        if block_line.startswith("print(") and block_line.endswith(")"):
                            content = block_line[6:-1].strip()
                            if content.startswith('"') and content.endswith('"'):
                                print(content.strip('"'))
                            elif content in variables:
                                print(variables[content])
                            else:
                                print("Ошибка: переменная не найдена")
                    continue  # Пропускаем elif/else, если if выполнился
            except Exception as e:
                print(f"Ошибка в if-условии: {e}")

        i += 1  # Следующая строка

