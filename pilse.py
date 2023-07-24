import os
from tkinter import Tk, Button, Label

def create_file():
    file_name = "example.txt"
    file = open(file_name, "w")
    file.write("This is an example file.")
    file.close()
    label.config(text="File created!")

def delete_file():
    file_name = "example.txt"
    if os.path.exists(file_name):
        os.remove(file_name)
        label.config(text="File deleted!")
    else:
        label.config(text="File does not exist!")

root = Tk()
root.title("Плюс_Пакет")

button1 = Button(root, text="Create File", command=create_file)
button1.pack()

button2 = Button(root, text="Delete File", command=delete_file)
button2.pack()

label = Label(root, text="")
label.pack()

root.mainloop()