import tkinter as tk

def show_device_properties():
    selected_device = listbox.curselection()
    if selected_device:
        device_name = listbox.get(selected_device)
        if device_name == "Системний драйвер":
            description_label.config(text="Os Device 1.7")
        elif device_name == "Устройство 2":
            description_label.config(text="Other Driver 1.9")
        elif device_name == "DVD":
            description_label.config(text="DVD 1.10")
        elif device_name == "Monitor":
            description_label.config(text="Monitor 1.10")
        elif device_name == "USB":
            description_label.config(text="USB 1.10")

root = tk.Tk()
root.title("Диспетчер устройств")

listbox = tk.Listbox(root)
listbox.insert(1, "Системний драйвер")
listbox.insert(2, "Устройство 2")
listbox.insert(3, "DVD")
listbox.insert(4, "Monitor")
listbox.insert(5, "USB")
listbox.pack()

description_label = tk.Label(root, text="")
description_label.pack()

button = tk.Button(root, text="Показать свойства", command=show_device_properties)
button.pack()

root.mainloop()