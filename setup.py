from tkinter import *
import tkinter.messagebox as mbox
import sys
import os

if os.path.exists('installed.txt'):
    print('Файл "installed.txt" уже существует. Установщик не будет запущен.')

def install():
    # Логика установки
    mbox.showinfo('Установка', 'Установка завершена')

def cancel():
    if mbox.askyesno('Отмена', 'Вы действительно хотите отменить установку?'):
        sys.exit()

root = Tk()
root.title('Установщик')

label = Label(root, text='Добро пожаловать в установщик.')
label.pack()

install_button = Button(root, text='Установить', command=install)
install_button.pack(side=LEFT)

cancel_button = Button(root, text='Отмена', command=cancel)
cancel_button.pack(side=LEFT)

file_name = "installed.txt"

with open(file_name, "w") as file:
    file.write("System a setup setup file don't start")

root.mainloop()