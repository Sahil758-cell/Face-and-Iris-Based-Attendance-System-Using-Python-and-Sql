import tkinter as tk
from tkinter import messagebox
from tkinter import ttk
from PIL import Image, ImageTk
import smtplib
import random

# Replace these with your email credentials
EMAIL_SENDER = "sahidesh02@gmail.com"
EMAIL_PASSWORD = "absrgmcukmcpcknp"

# Store OTP globally
generated_otp = None

# Function to send OTP
def send_otp(email_entry):
    global generated_otp
    recipient = email_entry.get()
    if not recipient:
        messagebox.showerror("Error", "Please enter email ID before sending OTP.")
        return

    generated_otp = str(random.randint(100000, 999999))

    try:
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        server.login(EMAIL_SENDER, EMAIL_PASSWORD)
        subject = "Your OTP for Signup Verification"
        body = f"Your OTP is: {generated_otp}"
        msg = f"Subject: {subject}\n\n{body}"
        server.sendmail(EMAIL_SENDER, recipient, msg)
        server.quit()
        messagebox.showinfo("OTP Sent", f"OTP sent to {recipient}")
    except Exception as e:
        messagebox.showerror("Error", f"Failed to send OTP:\n{e}")

# Function to validate and register user
def register_user():
    name = name_entry.get()
    lname = lname_entry.get()
    email = email_entry.get()
    phone = phone_entry.get()
    password = pass_entry.get()
    confirm_password = confirm_pass_entry.get()
    otp_entered = otp_entry.get()

    if not all([name, lname, email, phone, password, confirm_password, otp_entered]):
        messagebox.showerror("Error", "All fields are required.")
        return

    if password != confirm_password:
        messagebox.showerror("Error", "Passwords do not match.")
        return

    if otp_entered != generated_otp:
        messagebox.showerror("Error", "Incorrect OTP.")
        return

    # Save to file
    with open("user.txt", "a") as f:
        f.write(f"{email},{password}\n")

    messagebox.showinfo("Success", "Registered successfully!")
    root.destroy()

# Main window
root = tk.Tk()
root.title("Signup Page with OTP")
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
root.geometry(f"{screen_width}x{screen_height}")
root.configure(bg="white")

# Background image
bg_image = Image.open(r"C:\Users\SAHIL DESHMUKH.SAHIL\Desktop\FaceRecognition System\Collage_image\b11.jpg")  # Replace with your background image path
bg_image = bg_image.resize((screen_width, screen_height), Image.LANCZOS)
bg_photo = ImageTk.PhotoImage(bg_image)
bg_label = tk.Label(root, image=bg_photo)
bg_label.place(x=0, y=0, relwidth=1, relheight=1)

# Signup frame
frame = tk.Frame(root, bg="#ffffff", bd=2, relief=tk.RIDGE)
frame.place(relx=0.5, rely=0.5, anchor=tk.CENTER, width=600, height=600)

# Heading
title = tk.Label(frame, text="Create Account", font=("Helvetica", 22, "bold"), bg="white", fg="#333")
title.pack(pady=10)

# Form fields
fields = [
    ("First Name", "name_entry"),
    ("Last Name", "lname_entry"),
    ("Email ID", "email_entry"),
    ("Mobile Number", "phone_entry"),
    ("Password", "pass_entry", '*'),
    ("Confirm Password", "confirm_pass_entry", '*')
]

entries = {}

for i, field in enumerate(fields):
    label = tk.Label(frame, text=field[0], font=("Arial", 12), bg="white")
    label.pack()
    entry = tk.Entry(frame, font=("Arial", 12), width=30)
    if len(field) == 3:
        entry.config(show=field[2])
    entry.pack(pady=5)
    entries[field[1]] = entry

name_entry = entries['name_entry']
lname_entry = entries['lname_entry']
email_entry = entries['email_entry']
phone_entry = entries['phone_entry']
pass_entry = entries['pass_entry']
confirm_pass_entry = entries['confirm_pass_entry']

# OTP Section
otp_label = tk.Label(frame, text="Enter OTP", font=("Arial", 12), bg="white")
otp_label.pack()
otp_entry = tk.Entry(frame, font=("Arial", 12), width=30)
otp_entry.pack(pady=5)

otp_btn = tk.Button(frame, text="Send OTP", font=("Arial", 11), command=lambda: send_otp(email_entry), bg="#4CAF50", fg="white")
otp_btn.pack(pady=5)

# Submit Button
submit_btn = tk.Button(frame, text="Register", font=("Arial", 13), command=register_user, bg="#2196F3", fg="white")
submit_btn.pack(pady=15)

root.mainloop()
