import tkinter as tk

root = tk.Tk()
root.title("My PE-like OS")
root.geometry("800x600")

# Создаем элементы интерфейса
label = tk.Label(root, text="Welcome to My PE-like OS!", font=("Arial", 24))
label.pack(pady=50)

button = tk.Button(root, text="Pe info", font=("Arial", 18))
button.pack(pady=20)

button = tk.Button(root, text="Pe txt", font=("Arial", 18))
button.pack(pady=20)

root.configure(bg="lightblue")

label = tk.Label(root, text="Not drives.Drivers a setup,setuping programs and system files", font=("Arial",24))
label.pack(pady=50)









# Добавляем функционал к кнопке
def button_click():
    label.config(text="Pe-like os 2.9")
button.config(command=button_click)

# Запускаем главный цикл приложения
root.mainloop()