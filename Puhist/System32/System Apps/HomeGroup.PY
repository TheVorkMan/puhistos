import tkinter as tk

class Group:
    def __init__(self, name):
        self.name = name
        self.members = []

    def add_member(self):
        member = member_entry.get()
        if member:
            self.members.append(member)
            member_list.insert(tk.END, member)
            member_entry.delete(0, tk.END)

    def remove_member(self):
        selected_index = member_list.curselection()
        if selected_index:
            member_list.delete(selected_index)
            del self.members[selected_index[0]]

# Создание главного окна
window = tk.Tk()
window.title("Group Management")

# Создание группы
group = Group("Group 1")

# Создание компонентов GUI
label = tk.Label(window, text="Group Name: " + group.name)
label.pack()

member_label = tk.Label(window, text="Members:")
member_label.pack()

member_list = tk.Listbox(window)
member_list.pack()

member_entry = tk.Entry(window)
member_entry.pack()

add_button = tk.Button(window, text="Add Member", command=group.add_member)
add_button.pack()

remove_button = tk.Button(window, text="Remove Member", command=group.remove_member)
remove_button.pack()

# Запуск главного цикла приложения
window.mainloop()