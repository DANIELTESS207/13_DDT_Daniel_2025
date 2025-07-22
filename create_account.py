import tkinter as tk
from tkinter import messagebox
import json
import os
import subprocess

# Create the window
root = tk.Tk()
root.title("GlobeHop - Create Account")
root.geometry("1000x700")
root.configure(bg="#f4f4f4")

# Title
title = tk.Label(root, text="Welcome to GlobeHop!", font=("Helvetica", 24, "bold"), bg="#f4f4f4", fg="black")
title.pack(pady=(40, 10))

subtitle = tk.Label(root, text="Create your account below", font=("Helvetica", 14), bg="#f4f4f4", fg="black")
subtitle.pack(pady=(0, 20))

# Form Frame
form_frame = tk.Frame(root, bg="#ffffff", padx=40, pady=40, highlightbackground="#ccc", highlightthickness=1)
form_frame.pack(pady=20)



def create_field(label_text):
    label = tk.Label(form_frame, text=label_text, font=("Helvetica", 12), bg="#ffffff", fg="black", anchor="w")
    label.pack(fill="x", pady=(10, 2))
    entry = tk.Entry(form_frame, font=("Helvetica", 12), width=30, bd=2, relief="groove",
                     bg="#e0e0e0", fg="black", insertbackground="black")
    entry.pack(fill="x", pady=(0, 10))
    return entry

# Fields
name_entry = create_field("Full Name")
email_entry = create_field("Email Address")
password_entry = create_field("Password")
password_entry.config(show="*")
dob_entry = create_field("Date of Birth (DD/MM/YYYY)")

# Save account and redirect to login
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

    # Open login.py (adjust path if needed)
    subprocess.Popen(["python", "login.py"])

# Submit Button
submit_btn = tk.Button(form_frame, text="Create Account", font=("Helvetica", 12, "bold"),
    bg="#004080", fg="black", activebackground="#003366", activeforeground="black",
    padx=10, pady=5, command=save_account)
submit_btn.pack(pady=(20, 10))

# Run app
root.mainloop()
