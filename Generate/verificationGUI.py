import csv
import tkinter as tk
from tkinter import ttk

# Initialize a set to store verified codes
verified_codes = set()

# Function to verify a student by code
def verify_student(student_code):
    if student_code in verified_codes:
        label_verification_status.config(text="Code {} has already been used for verification.".format(student_code))
    else:
        with open('Output.csv', mode='r') as csv_file:
            csv_reader = csv.reader(csv_file)
            for row in csv_reader:
                if row[4] == student_code:
                    if student_code in verified_codes:
                        label_verification_status.config(text="{} with Reg No. {} has already been verified.".format(row[1], row[2]))
                        break
                    else:
                        verified_codes.add(student_code)
                        label_verification_status.config(text="{} with Reg No. {} is verified.".format(row[1], row[2]))

# Create the GUI window
window = tk.Tk()

# Set the window title
window.title("Student Verification")

# Set the window size
window.geometry("500x400")

# Set the background color to black
window.config(bg="#1e1e1e")

# Create a frame to contain the widgets
frame = tk.Frame(window, bg="#1e1e1e")

# Create a label to display the verification status
label_verification_status = tk.Label(frame, text="Enter a code to verify:", font=("Roboto", 16, "bold"), fg="white", bg="#1e1e1e")

# Create an entry box for the user to enter the code
entry_code = tk.Entry(frame, font=("Roboto", 16), fg="black", bg="white", insertbackground="white")

# Create a button to verify the code
button_verify = ttk.Button(frame, text="Verify", command=lambda: verify_student(entry_code.get()), style='TButton')

# Style the button
style = ttk.Style()
style.configure('TButton', font=('Roboto', 16), foreground='black', background='#0078d7')

# Pack the widgets into the frame
label_verification_status.pack(pady=10)
entry_code.pack(pady=10)
button_verify.pack(pady=10)

# Center the frame in the window
frame.place(relx=0.5, rely=0.5, anchor=tk.CENTER)

# Start the mainloop
window.mainloop()
