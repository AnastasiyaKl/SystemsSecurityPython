import tkinter as tk
import json


def add_new_user(username, passwd):
    with open("users.json", "r") as file:
        data = json.load(file)
    file.close()

    with open("users.json", "w") as file:
        data[username] = dict(password=passwd, blocked=False, type="user")
        json.dump(data, file)
    file.close()


def register_user():
    username_info = username_input.get()
    password_info = password_input.get()

    add_new_user(username_info, password_info)

    username_input.delete(0, tk.END)
    password_input.delete(0, tk.END)
    tk.Label(register_screen, text="Registration Successful", fg="green").pack()


def register():
    global register_screen
    register_screen = tk.Toplevel()
    register_screen.title("Registration")
    register_screen.geometry("400x300")

    global username_input
    global password_input

    username = tk.Text()
    password = tk.Text()

    tk.Label(register_screen, text="Username * ").pack()

    username_input = tk.Entry(register_screen, textvariable=username)
    username_input.pack()

    tk.Label(register_screen, text="Password * ").pack()

    password_input = tk.Entry(register_screen, textvariable=password)
    password_input.pack()

    tk.Button(register_screen, text="Register", width=10, height=1, command=register_user).pack()