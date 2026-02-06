import tkinter as tk

def login():
    username = entry_username.get()
    password = entry_password.get()
    # Добавь здесь код для проверки введенных данных
    print("Username:", username)
    print("Password:", password)

root = tk.Tk()

# Создание меток и полей ввода для имени пользователя и пароля
label_username = tk.Label(root, text="Username:")
label_username.pack()
entry_username = tk.Entry(root)
entry_username.pack()

label_password = tk.Label(root, text="Password:")
label_password.pack()
entry_password = tk.Entry(root, show="*") # чтобы скрыть вводимый пароль
entry_password.pack()

# Кнопка для входа
button_login = tk.Button(root, text="Login", command=login)
button_login.pack()

root.mainloop()