import tkinter as tk
from PIL import Image, ImageTk
import os

class FrancePage:
    def __init__(self, root):
        self.root = root
        self.root.title("GlobeHop - France")
        self.root.geometry("900x600")
        self.root.resizable(False, False)

        # Load background image
        bg_path = os.path.join("backgrounds", "france_bg.jpg")  # Make sure this exists
        if os.path.exists(bg_path):
            bg_image = Image.open(bg_path).resize((900, 600), Image.ANTIALIAS)
            self.bg_photo = ImageTk.PhotoImage(bg_image)
        else:
            self.bg_photo = None

        self.build_ui()

    def build_ui(self):
        # Canvas for background image
        canvas = tk.Canvas(self.root, width=900, height=600, highlightthickness=0)
        canvas.pack(fill="both", expand=True)

        if self.bg_photo:
            canvas.create_image(0, 0, image=self.bg_photo, anchor="nw")

        # Content box over canvas (smaller and semi-transparent feel)
        content_box = tk.Frame(self.root, bg="white", bd=2, relief="groove")
        canvas.create_window(450, 300, window=content_box, width=700, height=450)

        # Header
        tk.Label(
            content_box, text="France - Top 5 Hotels",
            font=("Helvetica", 24, "bold"), bg="#3498db", fg="white", width=50
        ).pack(pady=(0, 10))

        # Content layout (flag and hotels)
        layout_frame = tk.Frame(content_box, bg="white")
        layout_frame.pack(padx=10, pady=10, fill="both", expand=True)

        # Flag
        flag_frame = tk.Frame(layout_frame, bg="white")
        flag_frame.pack(side="left", padx=20, anchor="n")

        flag_path = os.path.join("flags", "france_bg.jpg")
        if os.path.exists(flag_path):
            img = Image.open(flag_path).resize((200, 130), Image.ANTIALIAS)
            self.flag_img = ImageTk.PhotoImage(img)
            tk.Label(flag_frame, image=self.flag_img, bg="white").pack()

        # Hotels
        hotel_frame = tk.Frame(layout_frame, bg="white")
        hotel_frame.pack(side="left", fill="both", expand=True)

        tk.Label(
            hotel_frame, text="Top 5 Recommended Hotels", 
            font=("Helvetica", 18, "bold"), bg="white", fg="#2c3e50"
        ).pack(pady=(0, 10))

        hotels = [
            ("Hotel Le Meurice - Paris", 4.9),
            ("Hotel Ritz Paris - Paris", 4.8),
            ("Le Bristol Paris - Paris", 4.7),
            ("Hotel Plaza Athenee - Paris", 4.6),
            ("Four Seasons George V - Paris", 4.9),
        ]

        for name, rating in hotels:
            tk.Label(
                hotel_frame,
                text=f"{name}\nRating: {rating}/5",
                font=("Helvetica", 13), bg="white", fg="#34495e", justify="left", anchor="w"
            ).pack(fill="x", padx=10, pady=6)

        # Back Button
        tk.Button(
            content_box, text="← Back to Country Selector",
            command=self.root.destroy,
            font=("Helvetica", 12, "bold"),
            bg="#2980b9", fg="black", padx=10, pady=5, bd=0
        ).pack(pady=10)

if __name__ == "__main__":
    root = tk.Tk()
    app = FrancePage(root)
    root.mainloop()
