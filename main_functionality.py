import tkinter as tk
from tkinter import *
import json
from auth.registration import add_new_user


def compare_passwords(entered, username):
    with open("data/users11.json", "r") as file:
        data = json.load(file)
        file.close()
        password = data[username].get("password", None)
        if entered == password:
            return True
        else:
            return False


# ################################################################################

def back_to_main():
    save_password_success_screen.destroy()
    welcome_user_screen.destroy()


def save_password_success():
    global save_password_success_screen
    save_password_success_screen = tk.Toplevel()
    save_password_success_screen.title("Success!")
    save_password_success_screen.geometry("300x200")

    tk.Label(save_password_success_screen, text="").pack()
    tk.Label(save_password_success_screen, text="You successfully changed you password!", fg="green").pack()
    tk.Label(save_password_success_screen, text="").pack()
    tk.Button(save_password_success_screen, text="OK", command=back_to_main).pack()



def save_new_password():
    passwd = new_password_input.get()
    add_new_user(username, passwd)
    save_password_success()


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

        tk.Label(text="").pack()
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


# ################################################################################

def back_to_main_admin():
    save_admin_passphrase_success_screen.destroy()
    save_admin_password_success_screen.destroy()
    change_admin_password_screen.destroy()


def save_admin_password_success():
    global save_admin_password_success_screen
    save_admin_password_success_screen = tk.Toplevel()
    save_admin_password_success_screen.title("Success!")
    save_admin_password_success_screen.geometry("300x200")

    tk.Label(save_admin_password_success_screen, text="").pack()
    tk.Label(save_admin_password_success_screen, text="You successfully changed you password!", fg="green").pack()
    tk.Label(save_admin_password_success_screen, text="").pack()
    tk.Button(save_admin_password_success_screen, text="OK", command=back_to_main_admin).pack()



def save_new_admin_password():
    passwd = new_admin_password_input.get()
    add_new_user(admin_username, passwd)
    save_admin_password_success()


def delete_admin_password_change_error():
    not_match_admin.destroy()


def admin_password_change_error():
    global not_match_admin
    not_match_admin = tk.Toplevel(change_admin_password_screen)
    not_match_admin.title("Wrong password")
    not_match_admin.geometry("350x100")
    tk.Label(not_match_admin, text="You have another current password. Try again!").pack()
    tk.Button(not_match_admin, text="OK", command=delete_admin_password_change_error).pack()


def admin_change_password():
    global new_admin_password_input
    entered_admin_password = current_admin_password_input.get()

    matches = compare_passwords(entered_admin_password, admin_username)

    if matches:
        tk.Label(change_admin_password_screen, text="").pack()
        tk.Label(change_admin_password_screen, text="Input your new password").pack()
        new_admin_password = tk.Text()
        new_admin_password_input = tk.Entry(change_admin_password_screen, textvariable=new_admin_password)
        new_admin_password_input.pack()

        tk.Label(text="").pack()
        tk.Button(change_admin_password_screen, text="Save new password",
                  command=save_new_admin_password).pack()
    else:
        admin_password_change_error()


def change_admin_password():
    global change_admin_password_screen
    global current_admin_password_input

    change_admin_password_screen = tk.Toplevel()
    change_admin_password_screen.title("Change password")
    change_admin_password_screen.geometry("400x300")

    tk.Label(change_admin_password_screen, text="").pack()
    tk.Label(change_admin_password_screen, text="To change password input you current password first:").pack()

    current_admin_password = tk.Text()
    current_admin_password_input = tk.Entry(change_admin_password_screen, textvariable=current_admin_password)
    current_admin_password_input.pack()
    tk.Label(change_admin_password_screen, text="").pack()
    tk.Button(change_admin_password_screen, text="Change password", command=admin_change_password).pack()

def save_admin_passphrase_success():
    global save_admin_passphrase_success_screen
    save_admin_passphrase_success_screen = tk.Toplevel()
    save_admin_passphrase_success_screen.title("Success!")
    save_admin_passphrase_success_screen.geometry("300x200")

    tk.Label(save_admin_passphrase_success_screen, text="").pack()
    tk.Label(save_admin_passphrase_success_screen, text="You successfully changed you passphrase!", fg="green").pack()
    tk.Label(save_admin_passphrase_success_screen, text="").pack()
    tk.Button(save_admin_passphrase_success_screen, text="OK", command=back_to_main_admin).pack()



def save_new_admin_passphrase():
    global passphrase
    passphrase = new_passphrase_input.get()
    save_admin_passphrase_success()

def change_passphrase():
    global change_passphrase_screen
    global change_passphrase_input

    change_passphrase_screen = tk.Toplevel()
    change_passphrase_screen.title("Change passphrase")
    change_passphrase_screen.geometry("400x300")

    tk.Label(change_passphrase_screen, text="").pack()
    tk.Label(change_passphrase_screen, text="Enter new passphrase:").pack()

    new_passphrase = tk.Text()
    global new_passphrase_input
    new_passphrase_input = tk.Entry(change_passphrase_screen, textvariable=new_passphrase)
    new_passphrase_input.pack()
    tk.Label(change_passphrase_screen, text="").pack()
    tk.Button(change_passphrase_screen, text="Change passphrase", command=save_new_admin_passphrase).pack()

# ###############################################################


def successful_changes_ok():
    successful_changes_screen.destroy()
    work_with_users_screen.destroy()


def successful_changes():
    global successful_changes_screen
    successful_changes_screen = tk.Toplevel()
    successful_changes_screen.title("Successful changes!")
    successful_changes_screen.geometry("350x100")

    tk.Label(successful_changes_screen, text="").pack()
    tk.Label(successful_changes_screen, text="Changes was saved successfully").pack()
    tk.Label(successful_changes_screen, text="").pack()
    tk.Button(successful_changes_screen, text="OK", command=successful_changes_ok).pack()


def work_with_users():
    global work_with_users_screen
    work_with_users_screen = tk.Toplevel()
    work_with_users_screen.title("Users")
    work_with_users_screen.geometry("400x300")

    obj_blocked = {}

    with open("data/json", "r") as file:
        data = json.load(file)
        file.close()

        for attr in data:
            blocked_var = BooleanVar(value=True)
            user_info = "type: " + data[attr].get("type", "") + \
                   ", blocked: " + data[attr].get("blocked", False)
            tk.Label(work_with_users_screen, text=attr, font=("Calibri", 13)).pack()
            tk.Label(work_with_users_screen, text=user_info).pack()

            if data[attr].get("blocked", "") == "True":
                blocked_var.set(True)
            else:
                blocked_var.set(False)

            tk.Checkbutton(work_with_users_screen, text="Block", variable=blocked_var, onvalue=1, offvalue=0).pack()
            obj_blocked[attr] = blocked_var

            tk.Label(work_with_users_screen, text="==============================").pack()

        def func():
            with open("data/users11.json", "w") as file:
                new_data = {}
                for attr in data:
                    blocked = str(obj_blocked[attr].get())
                    user_type = data[attr].get("type", "")
                    passwd = data[attr].get("password", "")

                    new_data[attr] = dict(password=passwd, blocked=blocked, type=user_type)
                json.dump(new_data, file)
                file.close()

            successful_changes()


        tk.Button(work_with_users_screen, text="Save changes", command=func).pack()


# ###############################################################


def welcome_admin(username):
    global admin_username
    admin_username = username

    welcome_admin_screen = tk.Toplevel()
    welcome_admin_screen.title("Welcome!")
    welcome_admin_screen.geometry("400x300")

    title_text = "Hi, " + str(username) + ". Here you can work with users."
    tk.Label(welcome_admin_screen, text=title_text).pack()
    tk.Label(welcome_admin_screen, text="").pack()
    tk.Button(welcome_admin_screen, text="Change password", command=change_admin_password).pack()
    tk.Label(welcome_admin_screen, text="").pack()
    tk.Button(welcome_admin_screen, text="Work with users", command=work_with_users).pack()
    tk.Label(welcome_admin_screen, text="").pack()
    tk.Button(welcome_admin_screen, text="Change passphrase", command=change_passphrase).pack()
