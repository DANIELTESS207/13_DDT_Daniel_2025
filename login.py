import tkinter as tk
from tkinter import messagebox
import json
import subprocess
import os

# Load user data
def load_users():
    if os.path.exists("users.json"):
        with open("users.json", "r") as f:
            return json.load(f)
    return {}

# Validate login
def login():
    username = entry_username.get().strip()
    password = entry_password.get().strip()
    
    users = load_users()

    if username in users and users[username] == password:
        messagebox.showinfo("Login Success", f"Welcome, {username}!")
        root.destroy()  # Close the login window
        subprocess.Popen(["python3", "main.py", username])  # Launch main app with username
    else:
        messagebox.showerror("Login Failed", "Incorrect username or password.")

# UI Setup
root = tk.Tk()
root.title("Login")
root.geometry("300x250")
root.configure(bg="white")

tk.Label(root, text="Login to GlobeHop", font=("Helvetica", 16, "bold"), bg="white").pack(pady=20)

tk.Label(root, text="Username:", bg="white").pack()
entry_username = tk.Entry(root)
entry_username.pack(pady=5)

tk.Label(root, text="Password:", bg="white").pack()
entry_password = tk.Entry(root, show="*")
entry_password.pack(pady=5)

tk.Button(root, text="Login", command=login, bg="#3498db", fg="white").pack(pady=15)

root.mainloop()

print "welcome" 