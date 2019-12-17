import tkinter as tk
import json


# here rule for password
def validate_password(password):
    if len(password) >= 8:
        return True
    else:
        return False


def add_new_user(username, passwd):
    with open("data/users11.json", "r") as file:
        data = json.load(file)
    file.close()

    if username == "admin":
        user_type = "admin"
    else:
        user_type = "user"


    with open("data/users11.json", "w") as file:
        data[username] = dict(password=passwd, blocked="False", type=user_type)
        json.dump(data, file)
    file.close()


def back_to_main():
    registration_success_screen.destroy()
    register_screen.destroy()


def registration_success():
    global registration_success_screen
    registration_success_screen = tk.Toplevel()
    registration_success_screen.title("Success!")
    registration_success_screen.geometry("300x200")

    tk.Label(registration_success_screen, text="").pack()
    tk.Label(registration_success_screen, text="You successfully registered in system!", fg="green").pack()
    tk.Label(registration_success_screen, text="").pack()
    tk.Button(registration_success_screen, text="OK", command=back_to_main).pack()


def register_user():
    username_info = username_input.get()
    password_info = password_input.get()

    if validate_password(password_info):
        add_new_user(username_info, password_info)

        username_input.delete(0, tk.END)
        password_input.delete(0, tk.END)

        registration_success()

    else:
        password_input.delete(0, tk.END)
        tk.Label(register_screen, text='Password should consists at least of 8 characters!', fg="red").pack()


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

    tk.Label(register_screen, text="").pack()
    tk.Button(register_screen, text="Register", width=10, height=1, command=register_user).pack()