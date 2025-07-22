import tkinter as tk
from tkinter import messagebox

class CreateAccountApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Create Account - GlobeHop")
        self.root.geometry("600x400")
        self.root.configure(bg="#f2f2f2")

        self.title_label = tk.Label(root, text="Create Your GlobeHop Account!", font=("Arial", 18, "bold"), bg="#f2f2f2")
        self.title_label.pack(pady=10)

        self.subtitle_label = tk.Label(root, text="Sign up below", font=("Arial", 12), bg="#f2f2f2")
        self.subtitle_label.pack()

        self.form_frame = tk.Frame(root, bg="white", bd=1, relief="solid")
        self.form_frame.place(relx=0.5, rely=0.5, anchor="center", width=350, height=300)

        # Name Entry
        self.name_label = tk.Label(self.form_frame, text="Full Name", bg="white", anchor="w")
        self.name_label.pack(pady=(20, 0), padx=20, anchor="w")
        self.name_entry = tk.Entry(self.form_frame, width=30, bd=2, relief="groove")
        self.name_entry.pack(padx=20)

        # Email Entry
        self.email_label = tk.Label(self.form_frame, text="Email Address", bg="white", anchor="w")
        self.email_label.pack(pady=(10, 0), padx=20, anchor="w")
        self.email_entry = tk.Entry(self.form_frame, width=30, bd=2, relief="groove")
        self.email_entry.pack(padx=20)

        # Password Entry
        self.password_label = tk.Label(self.form_frame, text="Password", bg="white", anchor="w")
        self.password_label.pack(pady=(10, 0), padx=20, anchor="w")
        self.password_entry = tk.Entry(self.form_frame, show="*", width=30, bd=2, relief="groove")
        self.password_entry.pack(padx=20)

        # Confirm Password Entry
        self.confirm_password_label = tk.Label(self.form_frame, text="Confirm Password", bg="white", anchor="w")
        self.confirm_password_label.pack(pady=(10, 0), padx=20, anchor="w")
        self.confirm_password_entry = tk.Entry(self.form_frame, show="*", width=30, bd=2, relief="groove")
        self.confirm_password_entry.pack(padx=20)

        # Register Button
        self.register_button = tk.Button(self.form_frame, text="Create Account", command=self.create_account, bd=2, relief="solid", padx=10, pady=5)
        self.register_button.pack(pady=15)

    def create_account(self):
        name = self.name_entry.get()
        email = self.email_entry.get()
        password = self.password_entry.get()
        confirm_password = self.confirm_password_entry.get()

        if not name or not email or not password:
            messagebox.showerror("Error", "Please fill in all fields.")
        elif password != confirm_password:
            messagebox.showerror("Error", "Passwords do not match.")
        else:
            messagebox.showinfo("Success", "Account created successfully!")

if __name__ == "__main__":
    root = tk.Tk()
    app = CreateAccountApp(root)
    root.mainloop()
