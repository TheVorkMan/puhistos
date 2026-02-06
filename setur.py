import tkinter as tk
from tkinter import messagebox
import random

root = tk.Tk()
root.title("Морской бой")

board = []
board_size = 5

for _ in range(board_size):
    board.append(["O"] * board_size)

ship_positions = []

for _ in range(3):
    ship_row = random.randint(0, board_size - 1)
    ship_col = random.randint(0, board_size - 1)
    ship_positions.append((ship_row, ship_col))

def shoot(row, col):
    if (row, col) in ship_positions:
        board[row][col] = "X"
        messagebox.showinfo("Результат выстрела", "Попадание!")
    else:
        board[row][col] = "*"
        messagebox.showinfo("Результат выстрела", "Мимо!")

def on_click(row, col):
    if board[row][col] != "O":
        messagebox.showinfo("Неверный ход", "Вы уже стреляли в эту клетку!")
        return
    shoot(row, col)
    button = buttons[row][col]
    button.config(state=tk.DISABLED)

buttons = []

for row in range(board_size):
    button_row = []
    for col in range(board_size):
        button = tk.Button(root, text=" ", width=2, height=1, command=lambda r=row, c=col: on_click(r, c))
        button.grid(row=row, column=col)
        button_row.append(button)
    buttons.append(button_row)

root.mainloop()