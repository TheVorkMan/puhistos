from tkinter import *

def show_selected():
    selected_options = []
    if var_option1.get():
        selected_options.append("OS Temp")
    if var_option2.get():
        selected_options.append("Control Panel")
    if var_option3.get():
        selected_options.append("Drivers")
    if var_option4.get():
        selected_options.append("Other")
    if selected_options:
        print("Selected options:", ", ".join(selected_options))
    else:
        print("No options selected.")

window = Tk()
window.title("Component Selection")

var_option1 = BooleanVar()
var_option2 = BooleanVar()
var_option3 = BooleanVar()
var_option4 = BooleanVar()

check_option1 = Checkbutton(window, text="OS Temp", variable=var_option1)
check_option1.pack()

check_option2 = Checkbutton(window, text="Control Panel", variable=var_option2)
check_option2.pack()

check_option3 = Checkbutton(window, text="Drivers", variable=var_option3)
check_option3.pack()

check_option4 = Checkbutton(window, text="Other", variable=var_option4)
check_option4.pack()

button = Button(window, text="Show selected", command=show_selected)
button.pack()

window.mainloop()