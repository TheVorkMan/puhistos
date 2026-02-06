import tkinter as tk

def create_card(title, content):
    card_window = tk.Toplevel()
    card_window.title(title)

    label = tk.Label(card_window, text=content)
    label.pack()
    
    card_window.mainloop()

# Создание главного окна
window = tk.Tk()
window.title("Windows Card Space")

# Создание карточек
create_card("Карточка 1", "User John Defender code=*************")
window.mainloop()