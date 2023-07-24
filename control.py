from tkinter import *

def button1_click():
    print("Button 1 clicked")

def button2_click():
    print("Button 2 clicked")
def button3_click():
    print("System_page=Puhist")
def button4_click():
    print("Code=435646")
    
window = Tk()
window.title("Панель управления")

button1 = Button(window, text="TCP.IP", command=button1_click)
button1.pack()

button2 = Button(window, text="Other", command=button2_click)
button2.pack()

button3 = Button(window, text="System_page", command=button3_click)
button3.pack()

button4 = Button(window, text="Defender_code", command=button4_click) 
button4.pack()


window.mainloop()