from tkinter import Tk, Canvas

def paint(event):
    x, y = event.x, event.y
    canvas.create_oval(x, y, x+2, y+2, fill="black")

root = Tk()
canvas = Canvas(root, width=400, height=400)
canvas.bind("<B1-Motion>", paint)
canvas.pack()

root.mainloop()