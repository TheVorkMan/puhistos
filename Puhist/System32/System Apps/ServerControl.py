import tkinter as tk
import socket

def manage_server():
    server_ip = "192.168.0.1"
    server_port = 22
    
    # Подключение к серверу
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect((server_ip, server_port))
    
    command = command_entry.get()
    
    # Выполнение команд на сервере
    client_socket.sendall(command.encode())
    
    # Получение результатов выполнения команды
    data = client_socket.recv(1024).decode()
    
    result_label.configure(text="Результат выполнения команды: " + data)
    
    # Отключение от сервера
    client_socket.close()

# Создаем графический интерфейс
root = tk.Tk()
root.title("Управление серверами")

command_label = tk.Label(root, text="Введите команду:")
command_label.pack()

command_entry = tk.Entry(root)
command_entry.pack()

execute_button = tk.Button(root, text="Выполнить команду", command=manage_server)
execute_button.pack()

result_label = tk.Label(root, text="")
result_label.pack()

root.mainloop()