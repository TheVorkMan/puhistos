import tkinter as tk

def button_click():
    label.config(text="Кнопку нажали!")

root = tk.Tk()
root.title("Моя ОС")

label = tk.Label(root, text="Привет, Мир!")
label.pack()

button = tk.Button(root, text="Нажми меня!", command=button_click)
button_click()
button.pack()

root.mainloop()