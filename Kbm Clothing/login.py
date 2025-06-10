from tkinter import *
import tkinter as tk
from tkinter import messagebox
from dashboard import Dashboard

# Function to handle login button click
def login():
    username = usertb.get()
    password = passtb.get()
    if validate_login(username, password):
        messagebox.showinfo("Welcome!", "Login Successful")
        root.withdraw()  # Hide the login window
        open_dashboard()  # Open the dashboard
    else:
        messagebox.showerror("Error", "Invalid Username or Password")

# Function to validate login credentials
def validate_login(username, password):
    if username == "admin" and password == "123":
        return True
    else:
        return False

def open_dashboard():
    dashboard = Dashboard(root)

# Main function to open the login window
def open_login_window():
    global root, usertb, passtb

    root = tk.Tk()
    root.configure(bg='#AED6F1')
    root.geometry("700x500")
    root.resizable(False, False)

    usertxt = Label(root, text='Username: ', bg='#AED6F1', font=("Arial", 12))
    usertxt.place(x=150, y=290)

    passtxt = Label(root, text='Password: ', bg='#AED6F1', font=("Arial", 12))
    passtxt.place(x=150, y=330)

    usertb = Entry(root, font=('Arial', 15), width=15)
    usertb.place(x=270, y=290)

    passtb = Entry(root, font=('Arial', 15), show='*', width=15)
    passtb.place(x=270, y=330)

    loginbtn = Button(root, text='Login', bg='white', font='Arial', bd=1, command=login, relief=RAISED, width=15, height=1)
    loginbtn.place(x=270, y=400)

    root.mainloop()

# Run the application
if __name__ == "__main__":
    open_login_window()
