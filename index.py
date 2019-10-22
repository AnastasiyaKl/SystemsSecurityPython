import tkinter as tk
from auth.registration import register
from auth.authentication import login


def main_screen():
    global root
    root = tk.Tk()
    root.geometry("400x300")
    root.resizable(False, False)
    root.title("Lab 1")

    tk.Label(text="Lab 1", bg="grey", height="2", width="300", font=("Calibri", 13)).pack()
    tk.Label(text="").pack()
    tk.Button(root, text="Register", height="2", width="30", command=register).pack()
    tk.Button(root, text="Login", height="2", width="30", command=login).pack()

    root.mainloop()


main_screen()
