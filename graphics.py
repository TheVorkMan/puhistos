import os
import tkinter as tk

def open_file():
    file_name = "example.txt"
    os.startfile(file_name)

def close_file():
    file_name = "example.txt"
    os.system("TASKKILL /F /IM notepad.exe")

root = tk.Tk()
root.title("Мой Графический Интерфейс")

open_button = tk.Button(root, text="Открыть файл", command=open_file)
open_button.pack()

close_button = tk.Button(root, text="Закрыть файл", command=close_file)
close_button.pack()

root.mainloop()