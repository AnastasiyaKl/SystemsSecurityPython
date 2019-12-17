import tkinter as tk
import json
from main_functionality import welcome_user, welcome_admin


def check_user(username, passwd):
    with open("data/users11.json", "r") as file:
        data = json.load(file)
        file.close()
        if data.get(username, None):
            password = data[username].get("password", None)
            if data[username].get("blocked", None) == "True" and data[username].get("type", "") == "user":
                return 3    # user is blocked
            elif passwd == password:
                return data[username].get("type", "user")    # success
            else:
                return 1    # wrong password
        else:
            return 2    # no user with this username


def delete_wrong_password_screen():
    wrong_password_screen.destroy()


def delete_wrong_username_screen():
    wrong_username_screen.destroy()


def delete_blocked_user_screen():
    blocked_user_screen.destroy()


def wrong_password():
    global wrong_password_screen
    wrong_password_screen = tk.Toplevel()
    wrong_password_screen.title("Wrong password")
    wrong_password_screen.geometry("150x100")
    tk.Label(wrong_password_screen, text="Wrong password").pack()
    tk.Button(wrong_password_screen, text="OK", command=delete_wrong_password_screen).pack()


def wrong_username():
    global wrong_username_screen
    wrong_username_screen = tk.Toplevel()
    wrong_username_screen.title("User not found")
    wrong_username_screen.geometry("150x100")
    tk.Label(wrong_username_screen, text="User not found").pack()
    tk.Button(wrong_username_screen, text="OK", command=delete_wrong_username_screen).pack()


def blocked_user(name):
    global blocked_user_screen
    blocked_user_screen = tk.Toplevel()
    blocked_user_screen.title("Blocked user")
    blocked_user_screen.geometry("350x150")
    text = "User with name " + name + " is blocked."
    tk.Label(blocked_user_screen, text=text).pack()
    tk.Label(blocked_user_screen, text="Please, contact your administrator.").pack()
    tk.Button(blocked_user_screen, text="OK", command=delete_blocked_user_screen).pack()


def verify_user():
    username_info_verify = username_input_verify.get()
    password_info_verify = password_input_verify.get()

    verifying_result = check_user(username_info_verify, password_info_verify)

    if verifying_result == 3:
        blocked_user(username_info_verify)
    elif verifying_result == "user":
        welcome_user(username_info_verify)
    elif verifying_result == "admin":
        welcome_admin(username_info_verify)
    elif verifying_result == 1:
        wrong_password()
    else:
        wrong_username()

    username_input_verify.delete(0, tk.END)
    password_input_verify.delete(0, tk.END)


def login():
    global login_screen
    login_screen = tk.Toplevel()
    login_screen.title("Verifying")
    login_screen.geometry("400x300")

    global username_input_verify
    global password_input_verify

    username = tk.Text()
    password = tk.Text()

    tk.Label(login_screen, text="Username").pack()

    username_input_verify = tk.Entry(login_screen, textvariable=username)
    username_input_verify.pack()

    tk.Label(login_screen, text="").pack()
    tk.Label(login_screen, text="Password").pack()

    password_input_verify = tk.Entry(login_screen, textvariable=password)
    password_input_verify.pack()

    tk.Label(login_screen, text="").pack()
    tk.Button(login_screen, text="Log in", width=10, height=1, command=verify_user).pack()