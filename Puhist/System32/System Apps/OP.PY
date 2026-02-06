import tkinter as tk
from tkinter import messagebox

def show_warning():
    messagebox.showwarning("Предупреждение", "Не удаляйте системные файлы!")

root = tk.Tk()
root.withdraw()

show_warning()
root.mainloop()
