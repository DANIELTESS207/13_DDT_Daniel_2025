import tkinter as tk
from tkinter import messagebox
import json
import os
import subprocess
import sys

def open_create_account():
    create_path = os.path.join(os.path.dirname(__file__), "create_account.py")
    subprocess.Popen([sys.executable, create_path])
    root.destroy()

root = tk.Tk()
root.title("GlobeHop - Login")
root.geometry("1000x700")
root.configure(bg="#f4f4f4")

tk.Label(root, text="Welcome Back to GlobeHop!", font=("Helvetica", 24, "bold"), bg="#f4f4f4", fg="black").pack(pady=(40, 10))
tk.Label(root, text="Login to your account", font=("Helvetica", 14), bg="#f4f4f4", fg="black").pack(pady=(0, 20))

form_frame = tk.Frame(root, bg="#ffffff", padx=40, pady=40, highlightbackground="#ccc", highlightthickness=1)
form_frame.pack(pady=20)

def create_login_field(label_text):
    label = tk.Label(form_frame, text=label_text, font=("Helvetica", 12), bg="#ffffff", fg="black", anchor="w")
    label.pack(fill="x", pady=(10, 2))
    entry = tk.Entry(form_frame, font=("Helvetica", 12), width=30, bd=2, relief="groove",
                     bg="#e0e0e0", fg="black", insertbackground="grey")
    entry.pack(fill="x", pady=(0, 10))
    return entry

email_entry = create_login_field("Email Address")
password_entry = create_login_field("Password")
password_entry.config(show="*")

def login():
    email = email_entry.get()
    password = password_entry.get()

    if not email or not password:
        messagebox.showerror("Error", "Please enter both email and password.")
        return

    if not os.path.exists("accounts.json"):
        messagebox.showerror("Error", "No accounts found. Please create an account first.")
        return

    with open("accounts.json", "r") as f:
        try:
            accounts = json.load(f)
        except json.JSONDecodeError:
            accounts = []

    for account in accounts:
        if account["email"] == email and account["password"] == password:
            messagebox.showinfo("Login Successful", f"Welcome back, {account['username']}!")

            #Open main.py and pass the username
            main_path = os.path.join(os.path.dirname(__file__), "main.py")
            subprocess.Popen([sys.executable, main_path, account['username']])
            root.destroy()
            return

    messagebox.showerror("Login Failed", "Incorrect email or password.")

login_btn = tk.Button(form_frame, text="Login", font=("Helvetica", 12, "bold"),
                      bg="#004080", fg="black", activebackground="#003366", activeforeground="white",
                      padx=10, pady=5, command=login)
login_btn.pack(pady=(20, 10))

root.mainloop()
