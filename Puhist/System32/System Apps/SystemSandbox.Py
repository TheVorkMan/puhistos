import tkinter as tk

def create_sandbox():
    root = tk.Tk()
    root.configure(bg="lightblue")
    
    label = tk.Label(root, text="Welcome to My Sandbox-SandBox Shell 5.0!", font=("Arial", 24))
    label.pack(pady=50)
    
    def button_click():
        label.config(text="Sandbox-Sandbox Shell 5.0")
    
    button = tk.Button(root, text="Sandbox info", font=("Arial", 18), command=button_click)
    button.pack(pady=20)
    
    root.mainloop()

create_sandbox()