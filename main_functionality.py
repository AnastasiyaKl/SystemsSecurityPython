import tkinter as tk
import json
from auth.registration import add_new_user


def compare_passwords(entered, username):
    with open("users.json", "r") as file:
        data = json.load(file)
        file.close()
        password = data[username].get("password", None)
        if entered == password:
            return True
        else:
            return False


def save_new_password():
    passwd = new_password_input.get()
    add_new_user(username, passwd)
    tk.Label(welcome_user_screen, text="New password was saved", fg="green").pack()


def delete_password_change_error():
    not_match.destroy()


def password_change_error():
    global not_match
    not_match = tk.Toplevel(welcome_user_screen)
    not_match.title("Wrong password")
    not_match.geometry("350x100")
    tk.Label(not_match, text="You have another current password. Try again!").pack()
    tk.Button(not_match, text="OK", command=delete_password_change_error).pack()


def change_password():
    global new_password_input
    entered_password = current_password_input.get()

    matches = compare_passwords(entered_password, username)

    if matches:
        tk.Label(welcome_user_screen, text="").pack()
        tk.Label(welcome_user_screen, text="Input your new password").pack()
        new_password = tk.Text()
        new_password_input = tk.Entry(welcome_user_screen, textvariable=new_password)
        new_password_input.pack()
        tk.Button(welcome_user_screen, text="Save new password",
                  command=save_new_password).pack()
    else:
        password_change_error()


def welcome_user(user):
    global username
    username = user
    global welcome_user_screen
    global current_password_input

    welcome_user_screen = tk.Toplevel()
    welcome_user_screen.title("Welcome!")
    welcome_user_screen.geometry("400x300")

    title_text = "Hi, " + str(username) + ". Here you can change you password."
    tk.Label(welcome_user_screen, text=title_text).pack()
    tk.Label(welcome_user_screen, text="").pack()
    tk.Label(welcome_user_screen, text="To change password input you current password first:").pack()

    current_password = tk.Text()
    current_password_input = tk.Entry(welcome_user_screen, textvariable=current_password)
    current_password_input.pack()
    tk.Label(welcome_user_screen, text="").pack()
    tk.Button(welcome_user_screen, text="Change password", command=change_password).pack()


def welcome_admin(username):
    welcome_admin_screen = tk.Toplevel()
    welcome_admin_screen.title("Welcome!")
    welcome_admin_screen.geometry("400x300")

    title_text = "Hi, " + str(username) + ". Here you can work with users."
    tk.Label(welcome_admin_screen, text=title_text).pack()