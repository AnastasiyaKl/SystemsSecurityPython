import tkinter as tk
from auth.registration import register
from auth.authentication import login
from start_permission import start_permission


def about():
    global about_screen
    about_screen = tk.Toplevel()
    about_screen.title("About")
    about_screen.geometry("400x350")

    tk.Label(about_screen, text="").pack()
    tk.Label(about_screen, text="Done by").pack()
    tk.Label(about_screen, text="Anastasiya Kovalenko, group IS-63").pack()
    tk.Label(about_screen, text="Katerina Avramenko, group IS-63").pack()
    tk.Label(about_screen, text="Variant #8").pack()

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


if(start_permission()):
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

