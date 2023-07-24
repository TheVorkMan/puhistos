import os

def display_directory_contents(path):
    for file_name in os.listdir(path):
        print(file_name)

path = input("Введите путь к папке: ")
display_directory_contents(path)

