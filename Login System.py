# Simple Login System

import tkinter as tk
from tkinter import messagebox

root = tk.Tk()
root.title("1O1 Portal")
root.geometry("320x165")

# Configure a custom color scheme
btn_bg_color = "grey"  
btn_fg_color = "white"  
bg_color = "yellow"  
label_font = ("Helvetica", 15)
button_font = ("Helvetica", 11)

root.configure(bg=bg_color)

# Function to display the initial welcome screen
def new():
    # Clear the GUI
    for widget in root.winfo_children():
        widget.destroy()

    # Display the welcome message
    welcome_label = tk.Label(text="Welcome to 101", font=label_font, bg=bg_color)
    welcome_label.pack(pady=5)

    # Add buttons for login, registration, and exit
    Login_Button = tk.Button(root, text="Login", command=login, font=button_font, bg=btn_bg_color, fg=btn_fg_color)
    Login_Button.pack(pady=5)

    Register_Button = tk.Button(root, text="Register", command=register, font=button_font, bg=btn_bg_color, fg=btn_fg_color)
    Register_Button.pack(pady=5)

    close_Button = tk.Button(root, text="Exit", command=close, font=button_font, bg=btn_bg_color, fg=btn_fg_color)
    close_Button.pack(pady=5)

# Function to handle the login process
def login():
    # Clear the GUI
    for widget in root.winfo_children():
        widget.destroy()
    c = 0

    def login1():
        # Check the entered username and password
        nonlocal c
        a = str(name.get())
        b = str(password.get())
        c += 1
        if a in x and x[a] == b:
            messagebox.showinfo("Congratulations", "Login Successful !!!")
            new()
        elif c < 5:
            messagebox.showinfo("Invalid", "Enter Correct Account Name and Password")
        elif c > 5:
            messagebox.showinfo("Invalid", "Too many Trials")
            new()

    # Create labels and entry fields for username and password
    name_label = tk.Label(text="User Name", font=("Helvetica", 12), bg=bg_color)
    name_label.place(x=10, y=20)

    name = tk.Entry(root, font=("Helvetica", 13))
    name.place(x=100, y=20)

    password_label = tk.Label(text="Password", font=("Helvetica", 12), bg=bg_color)
    password_label.place(x=10, y=60)

    password = tk.Entry(root, font=("Helvetica", 13))
    password.place(x=100, y=60)

    # Add a button to trigger the login process
    Login_Button = tk.Button(root, text="Login", command=login1, font=("Helvetica", 13), bg=btn_bg_color, fg=btn_fg_color)
    Login_Button.place(x=140, y=100)

# Function to handle the registration process
def register():
    # Clear the GUI
    for widget in root.winfo_children():
        widget.destroy()

    def register1():
        # Check the entered username and password during registration
        a = str(name.get())
        b = str(password.get())
        c = str(confirm.get())
        if a in x:
            messagebox.showinfo("Invalid User Name", "User Name already exists. Please enter a new User Name.")
        elif c != b:
            messagebox.showinfo("Invalid Password", "Enter the same password as above to confirm!")
        elif a == "" or b == "":
            messagebox.showinfo("Invalid", "Enter valid User Name and Password")
        else:
            # Add the new account to the dictionary
            x[a] = b
            messagebox.showinfo("Congratulations", "Account Successfully Created!!!")
            new()

    # Create labels and entry fields for username, password, and password confirmation
    name_label = tk.Label(text="User Name", font=("Helvetica", 12), bg=bg_color)
    name_label.place(x=10, y=10)

    name = tk.Entry(root, font=("Helvetica", 12))
    name.place(x=100, y=10)

    password_label = tk.Label(text="Password", font=("Helvetica", 12), bg=bg_color)
    password_label.place(x=10, y=50)

    password = tk.Entry(root, font=("Helvetica", 12))
    password.place(x=100, y=50)

    confirm_label = tk.Label(text="Confirm", font=("Helvetica", 12), bg=bg_color)
    confirm_label.place(x=10, y=90)

    confirm = tk.Entry(root, font=("Helvetica", 12))
    confirm.place(x=100, y=90)

    # Add a button to trigger the registration process
    Register_Button = tk.Button(root, text="Register", command=register1, font=("Helvetica", 12),
                                bg=btn_bg_color, fg=btn_fg_color)
    Register_Button.place(x=140, y=120)

# Function to close the tkinter window
def close():
    root.destroy()

# Create the initial welcome screen
welcome_label = tk.Label(text="Welcome to 101", font=label_font, bg=bg_color)
welcome_label.pack(pady=5)

Login_Button = tk.Button(root, text="Login", command=login, font=button_font, bg=btn_bg_color, fg=btn_fg_color)
Login_Button.pack(pady=5)

Register_Button = tk.Button(root, text="Register", command=register, font=button_font, bg=btn_bg_color,
                            fg=btn_fg_color)
Register_Button.pack(pady=5)

close_Button = tk.Button(root, text="Exit", command=close, font=button_font, bg=btn_bg_color, fg=btn_fg_color)
close_Button.pack(pady=5)

# Dictionary to store the registered accounts
x = {}

root.mainloop()
