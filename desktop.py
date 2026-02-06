import os
import tkinter as tk
from tkinter import messagebox

def open_app():
    print("Открыть приложение")

def exit_app():
    print("Выход из приложения")
    root.quit()
    
    # Создаем функцию, которая будет вызывать уведомление
def show_notification():
    messagebox.showinfo("Уведомление", "Привет, это уведомление!")

# Вызываем функцию для отображения уведомления
show_notification()
    
def os_app():
    print("OS a set")

root = tk.Tk()
root.title("Desktop")
root.geometry("800x600")

# Добавьте свои виджеты и настройки рабочего стола здесь\
root.configure(bg="lightblue")
root.geometry("600x400+200+100")

frame = tk.Frame(root)
frame.pack(side=tk.TOP, fill=tk.X)

open_button = tk.Button(frame, text="Open App", command=open_app)
open_button.pack(side=tk.LEFT)

exit_button = tk.Button(frame, text="Exit", command=exit_app)
exit_button.pack(side=tk.LEFT)

open_button = tk.Button(frame, text="OS", command=os_app())
open_button.pack(side=tk.LEFT)

open_button = tk.Button(frame, text="Pravka", command=os_app())
open_button.pack(side=tk.LEFT)


def process_input():
    input_text = entry.get()
    print("Ты написал:", input_text)

root = tk.Tk()
root.title("Ряд ввода")

entry = tk.Entry(root)
entry.pack()

button = tk.Button(root, text="Ввод", command=process_input)
button.pack()

def show_menu(event):
    menu.post(event.x_root, event.y_root)
root = tk.Tk()

# Создаем главное меню
menu = tk.Menu(root, tearoff=0)
menu.add_command(label="Screen", command=lambda: print("Выбран пункт меню 1"))
menu.add_command(label="Theme", command=lambda: print("Выбран пункт меню 2"))
menu.add_separator()
menu.add_command(label="Выход", command=root.quit)

# Привязываем событие нажатия левой кнопки мыши к функции отображения меню
root.bind("<Button-1>", show_menu)

root.mainloop()
        
        




root.mainloop()