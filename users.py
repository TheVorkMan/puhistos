import tkinter as tk

def add_user():
    username = entry.get()
    listbox.insert(tk.END, username)
    entry.delete(0, tk.END)

root = tk.Tk()
root.title("Список пользователей")

entry = tk.Entry(root)
entry.pack()

button = tk.Button(root, text="Добавить", command=add_user)
button.pack()

listbox = tk.Listbox(root)
listbox.pack()

root.mainloop()