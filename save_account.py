import os
import json
import subprocess
from tkinter import messagebox, Tk, Entry

# Assuming these Entry widgets are defined somewhere in your code
root = Tk()
name_entry = Entry(root)
email_entry = Entry(root)
password_entry = Entry(root)
dob_entry = Entry(root)

def save_account():
    name = name_entry.get()
    email = email_entry.get()
    password = password_entry.get()
    dob = dob_entry.get()

    if not name or not email or not password or not dob:
        messagebox.showerror("Error", "All fields must be filled.")
        return

    account = {
        "username": name,
        "email": email,
        "password": password,
        "dob": dob
    }

    accounts = []
    if os.path.exists("accounts.json"):
        with open("accounts.json", "r") as f:
            try:
                accounts = json.load(f)
            except json.JSONDecodeError:
                accounts = []

    accounts.append(account)

    with open("accounts.json", "w") as f:
        json.dump(accounts, f, indent=4)

    messagebox.showinfo("Success", "Account created successfully!")

    root.destroy()  # Close current window

    # Open main.py
    subprocess.Popen(["python", "main.py"])
