from tkinter import Tk, Button, Label
import subprocess

def launch_application():
    app_path = "paint.py"
    pass
def launch():
    app_path = "cursor.py"
    pass


def activate_child_mode():
    root = Tk()
    root.title("Детский режим")
    
    label = Label(root, text="Добро пожаловать в детский режим!", font=("Arial", 24))
    label.pack(pady=20)
    
    draw_button = Button(root, text="Рисовать", font=("Arial", 18), width=15, height=2)
    draw_button.pack(pady=10)
    launch_application()
    
    play_button = Button(root, text="Играть", font=("Arial", 18), width=15, height=2)
    play_button.pack(pady=10)
    launch()
    
    root.mainloop()

activate_child_mode()