from Crypto.PublicKey import RSA
from hashlib import sha512
import os.path
import os
import tkinter as tk
from tkinter import *
import psutil
import json
from ctypes import *
user32 = windll.user32


def about():
    global about_screen
    about_screen = tk.Toplevel()
    about_screen.title("About")
    about_screen.geometry("400x350")

    tk.Label(about_screen, text="").pack()
    tk.Label(about_screen, text="Done by").pack()
    tk.Label(about_screen, text="Mudraya Anastasiya, group IS-61").pack()
    tk.Label(about_screen, text="Khodarchenko Andrey, group IS-61").pack()
    tk.Label(about_screen, text="Variant #11").pack()

def main_screen():
    global root
    root = tk.Tk()
    root.geometry("400x300")
    root.resizable(False, False)
    root.title("Lab 1")

    tk.Label(text="Lab 1", bg="grey", height="2", width="300", font=("Calibri", 13)).pack()
    tk.Label(text="").pack()
    tk.Button(root, text="Register", height="2", width="30", command=register).pack()
    tk.Label(text="").pack()
    tk.Button(root, text="Login", height="2", width="30", command=login).pack()
    tk.Label(text="").pack()
    tk.Button(root, text="About", height="2", width="30", command=about).pack()

    root.mainloop()

def compare_passwords(entered, username):
    with open("data/users.json", "r") as file:
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

    with open("data/users.json", "r") as file:
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
            with open("data/users.json", "w") as file:
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

# here rule for password
def validate_password(password):
    digits = 0
    letters = 0
    signs = 0
    for char in password:
        if char.isdigit():
            digits += 1
        if char.isalpha():
            letters += 1
        if char == '+' or char == '-' or char == '*' or char == '/':
            signs += 1
    if digits > 0 and letters > 0 and signs > 0:
        return True
    else:
        return False


def add_new_user(username, passwd):
    with open("data/users.json", "r") as file:
        data = json.load(file)
    file.close()

    if username == "admin":
        user_type = "admin"
    else:
        user_type = "user"


    with open("data/users.json", "w") as file:
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
        tk.Label(register_screen, text='Password should consists at least one letter, one digit and one sign of arithmetic operation!', fg="red").pack()


def register():
    global register_screen
    register_screen = tk.Toplevel()
    register_screen.title("Registration")
    register_screen.geometry("600x300")

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

def check_user(username, passwd):
    with open("data/users.json", "r") as file:
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

def start_permission():
    if (os.path.exists("rsa") == False and os.path.exists("rsa_pub") == False and os.path.exists("signature") == False):
        keyPair = RSA.generate(bits=1024)

        f = open("rsa_pub","w+")
        f.write(str(keyPair.n) + " " + str(keyPair.e))
        f.close()

        f = open("rsa","w+")
        f.write(str(keyPair.n) + " " + str(keyPair.d))
        f.close()

        f = open("signature","w+")
        msg = str(sys_inf()).encode('utf-8')
        hash = int.from_bytes(sha512(msg).digest(), byteorder='big')
        signature = pow(hash, keyPair.d, keyPair.n)
        f.write(str(signature))
        f.close()
        return True
    elif(os.path.exists("rsa") == False or os.path.exists("rsa_pub") == False or os.path.exists("signature") == False):
        return False
    else:
        f = open("rsa_pub","r")
        contentsPub = f.read()
        arContentsPub = contentsPub.split(" ")
        try:
            arContentsPub_1 = int(arContentsPub[1])
            arContentsPub_0 = int(arContentsPub[0])
        except:
            return False
        f.close()

        f = open("signature","r")
        contentsSign = f.read()
        try:
            contentsSign = int(contentsSign)
        except:
            return False
        f.close()

        msg = str(sys_inf()).encode('utf-8')
        hash = int.from_bytes(sha512(msg).digest(), byteorder='big')
        hashFromSignature = pow(contentsSign, arContentsPub_1, arContentsPub_0)
        if (hash == hashFromSignature):
            return True
        else:
            return False

def sys_inf():
    inf = ''

    # Определяем язык ввода
    hwnd = user32.GetForegroundWindow()
    threadID = user32.GetWindowThreadProcessId(hwnd, None)
    StartLang = user32.GetKeyboardLayout(threadID)
    if ( StartLang == 67699721):
        lang = " ENG "
    elif ( StartLang == 67568647):
        lang = " DEU "
    elif (StartLang == -257424350):
        lang = " UKR "
    elif (StartLang == 68748313):
        lang = " RUS "
    else :
        lang = " " + StartLang + " "
    # RAM
    memory = psutil.virtual_memory().total / (1024.0 ** 3)
    inf += " " + str(memory) + " "
    # Screen size
    root_main = tk.Tk()
    inf += " " + str(root_main.winfo_screenheight()) + "px "
    inf += " " + str(root_main.winfo_screenheight()) + "px "
    root_main.destroy()
    # Username
    inf += " " + os.environ.get( "USERNAME" ) + " "
    # Path to Windows
    inf += " " + os.environ.get('SYSTEMROOT') + " "
    # Computername
    inf += " " + os.environ['COMPUTERNAME'] + " "
    # Current disk
    inf += " " + str(os.getcwd())[:2] + " "
    # Memory on current disk
    inf += " " + str(psutil.disk_usage('/').total / (1024.0 ** 3)) + " "

    return inf


if (start_permission()):
    main_screen()
else:
    global denied_permission_screen
    denied_permission_screen = tk.Tk()
    denied_permission_screen.title("Denied access")
    denied_permission_screen.geometry("400x350")
    denied_permission_screen.resizable(False, False)

    tk.Label(denied_permission_screen, text="").pack()
    tk.Label(denied_permission_screen, text="Sorry, but your keys are damaged(").pack()

    denied_permission_screen.mainloop()
