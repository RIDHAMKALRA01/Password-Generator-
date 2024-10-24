# Importing necessary modules
from tkinter import *
import random
from tkinter import messagebox  # For generating random passwords

# Initialize the Tkinter root window
root = Tk()
root.title("Password Generator")  # Set the title of the window
root.geometry("400x300")  # Define the window size
root.resizable(False, False)  # Prevent resizing of the window

# Variables to hold the generated password and the length of the password
password_str = StringVar()  # StringVar to hold the generated password
password_length = IntVar()  # IntVar to hold the password length input by the user

# Default length for the password
password_length.set(8)

# Function to generate a random password
def generate_password():
    try:
        length = password_length.get()  # Get the length entered by the user

        # List of characters to generate the password from
        char_list = (
            'abcdefghijklmnopqrstuvwxyz'
            'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
            '0123456789'
            '!@#$%^&*()'
        )

        # Generate a random password
        generated_password = ''.join(random.choice(char_list) for _ in range(length))
        
        # Set the generated password to the StringVar
        password_str.set(generated_password)
    except Exception as e:
        password_str.set("Error")

# Function to copy the password to the clipboard
def copy_to_clipboard():
    generated_password = password_str.get()  # Get the generated password
    if generated_password:
        root.clipboard_clear()  # Clear the clipboard
        root.clipboard_append(generated_password)  # Append the password to the clipboard
        messagebox.showinfo("Success", "Password copied to clipboard!")  # Show success message
    else:
        messagebox.showwarning("Warning", "No password to copy!")  # Show warning if no password is generated

# Set attractive background colors for the window
bg_color = "#C1CFA1"
frame_bg_color = "#001F3F"  # Slate blue for the frame and inner components
button_color = "#B8001F"  # Tomato color for buttons
label_color = "#F0E68C"  # Light Khaki color for labels

# Configure the main window's background color
root.configure(bg=bg_color)

# Creating and organizing the UI components

# Title Label
Label(root, text="Password Generator", font="Calibri 18 bold", bg=bg_color).pack(pady=10)

# Frame for organizing inner components and setting background color
frame = Frame(root, bg=frame_bg_color)
frame.pack(pady=10, padx=10, fill="both", expand=True)

# Password length label and entry
Label(frame, text="Enter password length:", font="Calibri 12", bg=frame_bg_color, fg=label_color).pack(pady=5)
Entry(frame, textvariable=password_length, width=10, font="Calibri 12").pack(pady=5)

# Button to generate the password
Button(frame, text="Generate Password", command=generate_password, font="Calibri 12", bg=button_color, fg="white", width=20).pack(pady=10)

# Entry to display the generated password
Entry(frame, textvariable=password_str, width=30, font="Calibri 12").pack(pady=5)

# Button to copy the generated password to the clipboard
Button(frame, text="Copy to Clipboard", command=copy_to_clipboard, font="Calibri 12", bg=button_color, fg="white", width=20).pack(pady=10)

# Start the main event loop
root.mainloop()
