import tkinter as tk
from tkinter import messagebox
import json
import os

# Save new user
def save_account():
    username = entry_username.get().strip()
    password = entry_password.get().strip()

    if not username or not password:
        messagebox.showerror("Error", "Username and password cannot be empty.")
        return

    users = {}
    if os.path.exists("users.json"):
        with open("users.json", "r") as f:
            users = json.load(f)

    if username in users:
        messagebox.showerror("Error", "Username already exists.")
        return

    users[username] = password

    with open("users.json", "w") as f:
        json.dump(users, f)

    messagebox.showinfo("Success", "Account created! You can now log in.")
    root.destroy()

# UI
root = tk.Tk()
root.title("Create Account")
root.geometry("300x250")
root.configure(bg="white")

tk.Label(root, text="Create Account", font=("Helvetica", 16, "bold"), bg="white").pack(pady=20)

tk.Label(root, text="Username:", bg="white").pack()
entry_username = tk.Entry(root)
entry_username.pack(pady=5)

tk.Label(root, text="Password:", bg="white").pack()
entry_password = tk.Entry(root, show="*")
entry_password.pack(pady=5)

tk.Button(root, text="Create", command=save_account, bg="#2ecc71", fg="white").pack(pady=15)

root.mainloop()
