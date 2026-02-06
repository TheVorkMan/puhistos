import tkinter as tk

def show_reason():
    reason = "Безопасность! Просим не отключать ОС без разрешения."

    root = tk.Tk()
    root.title("Причина отключения ОС")
    label = tk.Label(root, text=reason, padx=20, pady=20)
    label.pack()

    label = tk.Label(root, text="Введите значение:")
    label.pack()

    entry = tk.Entry(root)
    entry.pack()

    def add_value():
        value = entry.get()
        values.append(value)
        entry.delete(0, tk.END)

    button = tk.Button(root, text="Добавить", command=add_value)
    button.pack()

    root.mainloop()

values = []
show_reason()