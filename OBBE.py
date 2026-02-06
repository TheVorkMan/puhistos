from tkinter import *

def save_settings():
    username = entry_username.get()
    password = entry_password.get()
    os = entry_os.get()

    # здесь можно добавить логику для сохранения настроек

    label_status.config(text="Настройки сохранены")

# создание главного окна
root = Tk()

# создание элементов интерфейса
label_username = Label(root, text="Имя пользователя:")
entry_username = Entry(root)

label_password = Label(root, text="Пароль:")
entry_password = Entry(root, show="*")

label_os = Label(root, text="OS:")
entry_os = Entry(root, text="Options:")         

button_save = Button(root, text="Сохранить", command=save_settings)
label_status = Label(root, text="")

# размещение элементов на форме
label_username.pack()
entry_username.pack()

label_password.pack()
entry_password.pack()

label_os.pack()
entry_os.pack()

button_save.pack()
label_status.pack()

# запуск главного цикла окна
root.mainloop()