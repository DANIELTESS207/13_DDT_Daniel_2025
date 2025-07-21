import tkinter as tk
from tkinter import ttk, filedialog, messagebox
from PIL import Image, ImageTk
import sqlite3
import os
import shutil
import subprocess  # For Back to Home


# SQLite Setup
class CountryDatabase:
    def __init__(self, db_name="countries.db"):
        self.connection = sqlite3.connect(db_name)
        self.create_table()

    def create_table(self):
        cursor = self.connection.cursor()
        cursor.execute('''CREATE TABLE IF NOT EXISTS countries (
                            id INTEGER PRIMARY KEY AUTOINCREMENT,
                            name TEXT NOT NULL UNIQUE)''')
        self.connection.commit()

    def add_countries(self, country_list):
        cursor = self.connection.cursor()
        for country in country_list:
            cursor.execute("INSERT OR IGNORE INTO countries (name) VALUES (?)", (country,))
        self.connection.commit()

    def fetch_countries(self):
        cursor = self.connection.cursor()
        cursor.execute("SELECT name FROM countries ORDER BY name ASC")
        return [row[0] for row in cursor.fetchall()]

    def close(self):
        self.connection.close()


# GUI Class
class GlobeHopApp:
    def __init__(self, root):
        self.root = root
        self.root.title("GlobeHop - Select Country")
        self.root.geometry("800x550")
        self.root.resizable(False, False)

        self.db = CountryDatabase()
        self.setup_database()

        if not os.path.exists("flags"):
            os.makedirs("flags")

        # Background
        self.bg_image = Image.open("selectcountrybg_jpg.jpg").resize((800, 550))
        self.bg_photo = ImageTk.PhotoImage(self.bg_image)
        self.bg_label = tk.Label(self.root, image=self.bg_photo)
        self.bg_label.place(x=0, y=0, relwidth=1, relheight=1)

        self.create_widgets()

    def setup_database(self):
        countries = [
            "France", "Italy", "Spain", "Japan", "New Zealand", "Australia",
            "United States", "Canada", "Thailand", "Greece", "Switzerland",
            "Germany", "United Kingdom", "Portugal", "Turkey", "Vietnam",
            "Mexico", "South Korea", "Indonesia", "Brazil"
        ]
        self.db.add_countries(countries)

    def create_widgets(self):
        # Top Title Bar
        title_bar = tk.Label(
            self.root, text="GlobeHop",
            font=("Helvetica", 26, "bold"),
            fg="white", bg="#4682B4"
        )
        title_bar.place(relx=0, rely=0, relwidth=1, height=60)

        # Back to Home Button
        home_btn = tk.Button(
            self.root, text="← Back to Home", command=self.go_home,
            font=("Helvetica", 10, "bold"),
            bg="#eeeeee", fg="black",
            padx=10, pady=5, relief="flat", bd=1
        )
        home_btn.place(x=10, y=10)

        # Content Frame
        content_frame = tk.Frame(self.root, bg="#ffffff", bd=1)
        content_frame.place(relx=0.5, rely=0.55, anchor="center")
        content_frame.configure(highlightbackground="#cccccc", highlightthickness=1)

        # Left: Dropdown
        dropdown_frame = tk.Frame(content_frame, bg="#ffffff", padx=25, pady=25)
        dropdown_frame.grid(row=0, column=0, sticky="n")

        tk.Label(
            dropdown_frame, text="Select a Country",
            font=("Helvetica", 14, "bold"), bg="#ffffff"
        ).pack(anchor="w", pady=(0, 10))

        self.country_var = tk.StringVar()
        self.country_dropdown = ttk.Combobox(
            dropdown_frame, textvariable=self.country_var,
            state="readonly", width=25, font=("Helvetica", 11)
        )
        self.country_dropdown['values'] = self.db.fetch_countries()
        self.country_dropdown.pack(pady=(0, 15))
        self.country_dropdown.bind("<<ComboboxSelected>>", self.show_country_info)

        self.change_flag_button = tk.Button(
            dropdown_frame, text="Upload New Flag",
            command=self.change_flag, font=("Helvetica", 10, "bold"),
            bg="#3498db", fg="white", padx=10, pady=5,
            relief="flat", bd=0, highlightthickness=0
        )
        self.change_flag_button.pack()

        # Right: Flag & Info
        self.display_frame = tk.Frame(
            content_frame, bg="#f8f9fa", width=400, height=250,
            relief="ridge", bd=1
        )
        self.display_frame.grid(row=0, column=1, padx=(40, 20), pady=10)
        self.display_frame.grid_propagate(False)

        self.flag_label = tk.Label(self.display_frame, bg="#f8f9fa")
        self.flag_label.pack(pady=10)

        self.info_label = tk.Label(
            self.display_frame,
            text="Country information will appear here.",
            font=("Helvetica", 12),
            bg="#f8f9fa", fg="#333333", wraplength=360, justify="center"
        )
        self.info_label.pack(pady=(10, 0))

    def get_flag_path(self, country):
        filename = country.lower().replace(" ", "_") + ".png"
        return os.path.join("flags", filename)

    def show_country_info(self, event=None):
        country = self.country_var.get()
        if not country:
            return

        flag_path = self.get_flag_path(country)

        if os.path.exists(flag_path):
            img = Image.open(flag_path).resize((100, 60))
            self.flag_photo = ImageTk.PhotoImage(img)
            self.flag_label.config(image=self.flag_photo, text="")
            self.flag_label.image = self.flag_photo
        else:
            self.flag_label.config(image="", text="No flag available")

        self.info_label.config(text=f"You selected: {country}\n\n[Add interesting info, travel tips or highlights here.]")

    def change_flag(self):
        country = self.country_var.get()
        if not country:
            messagebox.showwarning("No Country Selected", "Please select a country first.")
            return

        file_path = filedialog.askopenfilename(
            title="Select Flag Image",
            filetypes=[("PNG Images", "*.png"), ("JPG Images", "*.jpg;*.jpeg")]
    
        )

        if not file_path:
            return

        ext = os.path.splitext(file_path)[1]
        if ext.lower() not in [".png", ".jpg", ".jpeg"]:
            messagebox.showerror("Invalid File", "Please select a PNG or JPG image.")
            return

        new_name = self.get_flag_path(country)
        shutil.copy(file_path, new_name)

        messagebox.showinfo("Success", f"Flag for {country} has been updated!")
        self.show_country_info()

    def go_home(self):
        self.on_close()
        subprocess.Popen(["python3", "main.py"])  # Make sure "main.py" is the correct filename

    def on_close(self):
        self.db.close()
        self.root.destroy()


# Launch App 
if __name__ == "__main__":
    root = tk.Tk()
    app = GlobeHopApp(root)
    root.protocol("WM_DELETE_WINDOW", app.on_close)
    root.mainloop()
