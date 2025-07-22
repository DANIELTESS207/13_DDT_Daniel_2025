import tkinter as tk
from tkinter import font as tkfont, messagebox
from PIL import Image, ImageTk
import os
import subprocess
import sys

# Get username from login (fallback = "Guest")
username = sys.argv[1] if len(sys.argv) > 1 else "Guest"


# Main App UI 
root = tk.Tk()
root.title("GlobeHop")
root.geometry("800x600")
root.resizable(False, False)

def nextPage():
    root.destroy()  # Close the current window
    subprocess.Popen(["python3", "select_country.py"])  # Open the select country window

def nextPage1():
    root.destroy()  # Close the current window
    subprocess.Popen(["python3", "login.py"])  # Open the select country window

def nextPage2():
    root.destroy()  # Close the current window
    subprocess.Popen(["python3", "create_account.py"])  # Open the select country window

# Theme colors
BG_COLOR = "#ecf0f1"
SIDEBAR_COLOR = "#2c3e50"
BUTTON_COLOR = "#3498db"
BUTTON_HOVER = "#2980b9"
TEXT_COLOR = "black"

root.configure(bg=BG_COLOR)

# Sidebar
sidebar = tk.Frame(root, bg=SIDEBAR_COLOR, width=200)
sidebar.pack(side="left", fill="y")

tk.Label(sidebar, text="Menu", font=("Helvetica", 14, "bold"), bg=SIDEBAR_COLOR, fg="white", pady=20).pack(fill="x")

button_font = ("Helvetica", 12)
button_config = {
    "font": button_font,
    "bg": BUTTON_COLOR,
    "fg": "black",
    "activebackground": BUTTON_HOVER,
    "activeforeground": "white",
    "bd": 0,
    "highlightthickness": 0,
    "width": 15,
    "height": 1,
    "padx": 10,
    "pady": 10
}

def on_enter(e): e.widget['bg'] = BUTTON_HOVER
def on_leave(e): e.widget['bg'] = BUTTON_COLOR

# Sidebar Buttons
create_btn = tk.Button(sidebar, text="Create Account", **button_config, command=nextPage2)
create_btn.pack(pady=(10, 5), padx=20, fill="x")
create_btn.bind("<Enter>", on_enter)
create_btn.bind("<Leave>", on_leave)

login_btn = tk.Button(sidebar, text="Login", **button_config, command=nextPage1)
login_btn.pack(pady=5, padx=20, fill="x")
login_btn.bind("<Enter>", on_enter)
login_btn.bind("<Leave>", on_leave)

select_btn = tk.Button(sidebar, text="Select Country", **button_config, command=nextPage)
select_btn.pack(pady=5, padx=20, fill="x")
select_btn.bind("<Enter>", on_enter)
select_btn.bind("<Leave>", on_leave)

support_btn = tk.Button(sidebar, text="Support/QA", **button_config)
support_btn.pack(pady=5, padx=20, fill="x")
support_btn.bind("<Enter>", on_enter)
support_btn.bind("<Leave>", on_leave)

# Main Content
content = tk.Frame(root, bg=BG_COLOR)
content.pack(side="right", expand=True, fill="both", padx=20, pady=20)

tk.Label(content, text=f"Welcome to GlobeHop, {username}", font=("Helvetica", 24, "bold"), bg=BG_COLOR, fg=TEXT_COLOR).pack(pady=20)
tk.Label(content, text="Your global travel companion", font=("Helvetica", 14), bg=BG_COLOR, fg=TEXT_COLOR).pack(pady=10)

# Background image
try:
    bg_image = Image.open("Globehop13DDT.jpg")
    bg_image = bg_image.resize((550, 400))
    bg_photo = ImageTk.PhotoImage(bg_image)
    tk.Label(content, image=bg_photo, bg=BG_COLOR).pack(pady=20)
    root.bg_photo = bg_photo  # prevent garbage collection
except:
    tk.Label(content, text="Travel destinations will appear here", font=("Helvetica", 12), bg=BG_COLOR, fg=TEXT_COLOR).pack(pady=50)

root.mainloop()