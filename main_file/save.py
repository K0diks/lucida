# save.py
import os
import datetime

folder_path = f"C:\\Users\\{os.getlogin()}\\Documents\\LucidaCode\\config"
save_folder_path = f"C:\\Users\\{os.getlogin()}\\Documents\\LucidaCode\\save"
library_folder_path = f"C:\\Users\\{os.getlogin()}\\Documents\\LucidaCode\\library"
config_path = f"{folder_path}\\default.cfg"
save_file = f"{save_folder_path}\\code.save"
variables = {}

def load_config():
    global file_path, com_deb
    if not os.path.exists(folder_path):
        os.makedirs(folder_path)
    if not os.path.exists(save_folder_path):
        os.makedirs(save_folder_path)
    if not os.path.exists(library_folder_path):
        os.makedirs(library_folder_path)

    if not os.path.exists(config_path):
        with open(config_path, "w") as file:
            file.write('file_path = "C:\\example.pizza"\n')
            file.write('com_deb = false\n')
    with open(config_path, "r") as file:
        for line in file:
            line = line.strip()
            if "=" in line:
                variable, value = line.split("=", 1)
                variable, value = variable.strip(), value.strip().strip('"')
                if variable == "file_path":
                    file_path = value
                elif variable == "com_deb":
                    com_deb = value.lower() == "true"


def save_config():
    with open(config_path, "w") as file:
        file.write(f'file_path = "{file_path}"\n')
        file.write(f'com_deb = {"true" if com_deb else "false"}\n')

def save_data():
    with open(save_file, "w") as file:
        for key, value in variables.items():
            file.write(f"{key}={value}\n")

def load_data():
    global variables
    if os.path.exists(save_file):
        with open(save_file, "r") as file:
            for line in file:
                line = line.strip()
                if "=" in line:
                    key, value = line.split("=", 1)
                    variables[key.strip()] = value.strip()
