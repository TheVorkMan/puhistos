from tkinter import *

def show_selection():
    selected_value = var.get()
    label_status.config(text="Выбрано: " + selected_value)

root = Tk()

var = StringVar()

check_button = Checkbutton(root, text="Специальная возможность", variable=var, command=show_selection)
check_button.pack()

label_status = Label(root, text="")
label_status.pack()

root.mainloop()