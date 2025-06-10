from tkinter import *
import tkinter as tk
from tkinter import ttk, messagebox
from PIL import ImageTk, Image


# function of login button click
def login():
    username = usertb.get()
    password = passtb.get()
    if validate_login(username, password):
        messagebox.showinfo("Welcome!", "Login Successful")
        root.withdraw()  # hide the login window
        open_dashboard()  # open the dashboard
    else:
        messagebox.showerror("Error", "Invalid Username or Password")


# login credentials
def validate_login(username, password):
    return username == "admin" and password == "123"

# add and edit + int
def is_positive_integer(value):
    try:
        number = int(value)
        return number > 0
    except ValueError:
        return False

# dashboard class
class Dashboard(tk.Toplevel):
    def __init__(self, parent):
        super().__init__(parent)

        self.title("Dashboard")
        self.geometry("800x450")
        self.center_window()
        self.resizable(False, False)

        # stock
        self.stock = {
            "Design 1": {"Small": 10, "Medium": 10, "Large": 10, "XL": 10},
            "Design 2": {"Small": 10, "Medium": 10, "Large": 10, "XL": 10},
            "Design 3": {"Small": 10, "Medium": 10, "Large": 10, "XL": 10}
        }

        # purchase history and total
        self.purchases = []
        self.total = 0

        # sidebar
        self.sidebar = tk.Frame(self, width=200, bg='#AED6F1', height=600, relief='sunken', borderwidth=2)
        self.sidebar.pack(expand=False, fill='y', side='left', anchor='nw')

        # main content frame
        self.main_content = tk.Frame(self, bg='#ecf0f1', width=600, height=600)
        self.main_content.pack(expand=True, fill='both', side='right')
        self.main_content.configure(bg='#ECF6FD')
        self.show_home()

        # buttons in sidebar
        self.home_button = tk.Button(self.sidebar, text="Home", font=("Arial", 12, "bold"), bg='#2874A6',
                                     fg="white",
                                     command=self.show_home, width=20)
        self.home_button.pack(pady=10, padx=15, fill='x')

        self.stock_button = tk.Button(self.sidebar, text="Stock", font=("Arial", 12, "bold"), bg='#2874A6',
                                      fg="white", command=self.show_stock, width=20)
        self.stock_button.pack(pady=10, padx=15, fill='x')

        self.restock_button = tk.Button(self.sidebar, text="Restock", font=("Arial", 12, "bold"), bg='#2874A6',
                                        fg="white",  command=self.show_restock)
        self.restock_button.pack(pady=10, padx=15, fill='x')

        self.order_button = tk.Button(self.sidebar, text="Order", font=("Arial", 12, "bold"), bg='#2874A6',
                                      fg="white", command=self.show_order)
        self.order_button.pack(pady=10, padx=15, fill='x')

        self.history_button = tk.Button(self.sidebar, text="History", font=("Arial", 12, "bold"), bg='#2874A6',
                                        fg="white", command=self.show_history)
        self.history_button.pack(pady=10, padx=15, fill='x')

        self.logout_button = tk.Button(self.sidebar, text="Logout", font=("Arial", 12, "bold"), bg='#2874A6',
                                       fg="white", command=self.logout)
        self.logout_button.pack(pady=10, padx=15, fill='x')

        # logo in sidebar
        try:
            sidebar_image = Image.open("C:\\Users\\aji\\OneDrive\\Pictures\\kbm.jpg")  # image path
            sidebar_image = sidebar_image.resize((150, 150))
            sidebar_photo = ImageTk.PhotoImage(sidebar_image)
            sidebar_picture_label = Label(self.sidebar, image=sidebar_photo, bg='#AED6F1')
            sidebar_picture_label.image = sidebar_photo
            sidebar_picture_label.pack(pady=20)
        except Exception as e:
            print(f"Error loading image: {e}")

            # homepage show after login
            self.show_home()

    def show_home(self):
        # clear main content frame
            for widget in self.main_content.winfo_children():
                widget.destroy()

            # dashboard logo
            try:
                main_image = Image.open("C:\\Users\\aji\\Downloads\\dashlogo.png")  # image path
                main_image = main_image.resize((550, 500))
                main_photo = ImageTk.PhotoImage(main_image)
                main_picture_label = Label(self.main_content, image=main_photo, bg='#2874A6')
                main_picture_label.image = main_photo
                main_picture_label.pack(expand=True)
            except Exception as e:
                print(f"Error loading image: {e}")

    def show_stock(self):
        # Clear main content frame
        for widget in self.main_content.winfo_children():
            widget.destroy()

        # stock info
        tk.Label(self.main_content, text="Stock Information", font=("Arial", 14, "bold"),
                 bg='#AED6F1', fg="black").grid(row=0, column=0, pady=10, padx=10, sticky="w")

        # Add search label and entry
        search_var = tk.StringVar()
        tk.Label(self.main_content, text="Search:", font=("Arial", 10),
                 bg='#AED6F1', fg="black").grid(row=1, column=0, pady=5, padx=10, sticky="w")
        search_entry = tk.Entry(self.main_content, textvariable=search_var, font=("Arial", 10), width=20)
        search_entry.grid(row=1, column=1, pady=5, padx=10, sticky="w")

        # Add treeview table for stock information
        columns = ("design", "small", "medium", "large", "xl")
        self.tree = ttk.Treeview(self.main_content, columns=columns, show='headings')
        self.tree.grid(row=2, column=0, columnspan=3, sticky='nsew')

        self.tree.heading("design", text="Design")
        self.tree.heading("small", text="Small")
        self.tree.heading("medium", text="Medium")
        self.tree.heading("large", text="Large")
        self.tree.heading("xl", text="XL")

        # add stock data to the table
        for design, sizes in self.stock.items():
            self.tree.insert("", "end", values=(design, sizes["Small"], sizes["Medium"], sizes["Large"], sizes["XL"]))


        self.tree.column("design", width=150, anchor='center')
        self.tree.column("small", width=100, anchor='center')
        self.tree.column("medium", width=100, anchor='center')
        self.tree.column("large", width=100, anchor='center')
        self.tree.column("xl", width=100, anchor='center')

        # buttons for adding, deleting, and editing products
        add_button = tk.Button(self.main_content, text="Add Product", font=("Arial", 12, "bold"),
                               bg='#AED6F1', fg="black", command=self.add_product)
        add_button.grid(row=3, column=0, pady=10, padx=10, sticky='w')

        delete_button = tk.Button(self.main_content, text="Delete Product", font=("Arial", 12, "bold"), bg='#AED6F1',
                                  fg="black", command=self.delete_product)
        delete_button.grid(row=3, column=1, pady=10, padx=10, sticky='w')

        edit_button = tk.Button(self.main_content, text="Edit Product", font=("Arial", 12, "bold"), bg='#AED6F1',
                                fg="black", command=self.edit_product)
        edit_button.grid(row=3, column=2, pady=10, padx=10, sticky='w')

        # make treeview expandable
        self.main_content.grid_rowconfigure(2, weight=1)
        self.main_content.grid_columnconfigure(0, weight=1)

        # bind search function to search entry
        search_entry.bind("<KeyRelease>", lambda event: self.search_stock(search_var.get()))

    def search_stock(self, search_term):
        # clear current content in the treeview
        for item in self.tree.get_children():
            self.tree.delete(item)

        # add filtered stock data to the table based on the search term
        for design, sizes in self.stock.items():
            if search_term.lower() in design.lower():
                self.tree.insert("", "end",
                                 values=(design, sizes["Small"], sizes["Medium"], sizes["Large"], sizes["XL"]))

    def add_product(self):
        # window for adding products
        add_window = tk.Toplevel(self)
        add_window.title("Add Product")
        add_window.geometry("400x380")
        add_window.resizable(False, False)
        add_window.configure(bg='#ECF6FD')
        center_window(add_window)

        tk.Label(add_window, text="Design Name:").pack(pady=5)
        design_var = tk.StringVar()
        design_entry = tk.Entry(add_window, textvariable=design_var)
        design_entry.pack(pady=5)

        tk.Label(add_window, text="Small Size Quantity:").pack(pady=5)
        small_var = tk.StringVar()
        small_entry = tk.Entry(add_window, textvariable=small_var)
        small_entry.pack(pady=5)

        tk.Label(add_window, text="Medium Size Quantity:").pack(pady=5)
        medium_var = tk.StringVar()
        medium_entry = tk.Entry(add_window, textvariable=medium_var)
        medium_entry.pack(pady=5)

        tk.Label(add_window, text="Large Size Quantity:").pack(pady=5)
        large_var = tk.StringVar()
        large_entry = tk.Entry(add_window, textvariable=large_var)
        large_entry.pack(pady=5)

        tk.Label(add_window, text="XL Size Quantity:").pack(pady=5)
        xl_var = tk.StringVar()
        xl_entry = tk.Entry(add_window, textvariable=xl_var)
        xl_entry.pack(pady=5)

        def save_product():
            design = design_var.get()
            small = small_var.get()
            medium = medium_var.get()
            large = large_var.get()
            xl = xl_var.get()
            if design and small and medium and large and xl:
                if all(is_positive_integer(quantity) for quantity in [small, medium, large, xl]):
                    small = int(small)
                    medium = int(medium)
                    large = int(large)
                    xl = int(xl)
                    if design not in self.stock:
                        self.stock[design] = {"Small": small, "Medium": medium, "Large": large, "XL": xl}
                        messagebox.showinfo("Add Product", "Product added successfully")
                        add_window.destroy()
                        self.show_stock()  # Refresh stock display after adding product
                    else:
                        messagebox.showwarning("Add Product", "Design already exists")
                else:
                    messagebox.showwarning("Add Product", "Please enter positive integers for quantities")
            else:
                messagebox.showwarning("Add Product", "Please fill in all fields")

        save_button = tk.Button(add_window, text="Save", font=("Arial", 12, "bold"),
                                bg='#AED6F1', fg="black", command=save_product)
        save_button.pack(pady=20)

    def edit_product(self):
        # window for editing products
        edit_window = tk.Toplevel(self)
        edit_window.title("Edit Product")
        edit_window.geometry("400x380")
        edit_window.configure(bg='#ECF6FD')
        center_window(edit_window)

        tk.Label(edit_window, text="Select Design:").pack(pady=5)
        design_var = tk.StringVar()
        design_combobox = ttk.Combobox(edit_window, textvariable=design_var)
        design_combobox['values'] = list(self.stock.keys())
        design_combobox.pack(pady=4)

        tk.Label(edit_window, text="Small Size Quantity:").pack(pady=5)
        small_var = tk.StringVar()
        small_entry = tk.Entry(edit_window, textvariable=small_var)
        small_entry.pack(pady=5)

        tk.Label(edit_window, text="Medium Size Quantity:").pack(pady=5)
        medium_var = tk.StringVar()
        medium_entry = tk.Entry(edit_window, textvariable=medium_var)
        medium_entry.pack(pady=5)

        tk.Label(edit_window, text="Large Size Quantity:").pack(pady=5)
        large_var = tk.StringVar()
        large_entry = tk.Entry(edit_window, textvariable=large_var)
        large_entry.pack(pady=5)

        tk.Label(edit_window, text="XL Size Quantity:").pack(pady=5)
        xl_var = tk.StringVar()
        xl_entry = tk.Entry(edit_window, textvariable=xl_var)
        xl_entry.pack(pady=5)

        def save_changes():
            design = design_var.get()
            small = small_var.get()
            medium = medium_var.get()
            large = large_var.get()
            xl = xl_var.get()
            if design and small and medium and large and xl:
                if all(is_positive_integer(quantity) for quantity in [small, medium, large, xl]):
                    small = int(small)
                    medium = int(medium)
                    large = int(large)
                    xl = int(xl)
                    if design in self.stock:
                        self.stock[design] = {"Small": small, "Medium": medium, "Large": large, "XL": xl}
                        messagebox.showinfo("Edit Product", "Product updated successfully")
                        edit_window.destroy()
                        self.show_stock()  # Refresh stock display after editing product
                    else:
                        messagebox.showwarning("Edit Product", "Design does not exist")
                else:
                    messagebox.showwarning("Edit Product", "Please enter positive integers for quantities")
            else:
                messagebox.showwarning("Edit Product", "Please fill in all fields")

        save_button = tk.Button(edit_window, text="Save", font=("Arial", 12, "bold"),
                                bg='#AED6F1', fg="black", command=save_changes)
        save_button.pack(pady=20)

    def show_order(self):
        # clear main content frame
        for widget in self.main_content.winfo_children():
            widget.destroy()

        tk.Label(self.main_content, text="Place Order", font=("Arial", 20, "bold"),
                 bg='#AED6F1', fg="black").place(x=200, y=35)

        tk.Label(self.main_content, text="Select Design:").place(x=240, y=100)
        design_var = tk.StringVar()
        design_combobox = ttk.Combobox(self.main_content, textvariable=design_var)
        design_combobox['values'] = list(self.stock.keys())
        design_combobox.place(x=210, y=150)

        tk.Label(self.main_content, text="Select Size:").place(x=250, y=200)
        size_var = tk.StringVar()
        size_combobox = ttk.Combobox(self.main_content, textvariable=size_var)
        size_combobox['values'] = ["Small", "Medium", "Large", "XL"]
        size_combobox.place(x=210, y=250)

        tk.Label(self.main_content, text="Enter Quantity:").place(x=240, y=300)
        quantity_var = tk.StringVar()
        quantity_entry = tk.Entry(self.main_content, textvariable=quantity_var)
        quantity_entry.place(x=220, y=350)

        def place_order():
            design = design_var.get()
            size = size_var.get()
            quantity = quantity_var.get()
            if design and size and quantity:
                try:
                    quantity = int(quantity)
                    if quantity > 0:
                        if self.stock[design][size] >= quantity:
                            self.stock[design][size] -= quantity
                            self.purchases.append((design, size, quantity))
                            self.total += quantity  # Assuming each item costs 1 unit for simplicity
                            messagebox.showinfo("Order", f"Order placed for {quantity} units of {design} ({size})")
                            self.show_stock()  # Refresh stock display after ordering
                        else:
                            messagebox.showwarning("Order", f"Not enough stock for {design} ({size})")
                    else:
                        messagebox.showwarning("Order", "Quantity must be a positive integer")
                except ValueError:
                    messagebox.showwarning("Order", "Please enter a valid quantity")
            else:
                messagebox.showwarning("Order", "Please select design, size, and enter a quantity")

        order_button = tk.Button(self.main_content, text="Order", font=("Arial", 12, "bold"), bg='#AED6F1',
                                 fg="black", command=place_order, width=10)
        order_button.place(x=230, y=400)

    def delete_product(self):
        # window for deleting products
        delete_window = tk.Toplevel(self)
        delete_window.title("Delete Product")
        delete_window.geometry("300x150")
        delete_window.resizable(False, False)
        delete_window.configure(bg='#ECF6FD')
        center_window(delete_window)

        tk.Label(delete_window, text="Select Design:").pack(pady=5)
        design_var = tk.StringVar()
        design_combobox = ttk.Combobox(delete_window, textvariable=design_var)
        design_combobox['values'] = list(self.stock.keys())
        design_combobox.pack(pady=5)

        def delete_product_confirm():
            design = design_var.get()
            if design:
                if design in self.stock:
                    confirm = messagebox.askyesno("Confirm Deletion",
                                                  f"Are you sure you want to delete the product '{design}'?")
                    if confirm:
                        del self.stock[design]
                        messagebox.showinfo("Delete Product", "Product deleted successfully")
                        delete_window.destroy()
                        self.show_stock()  # refresh stock display after deleting product
                else:
                    messagebox.showwarning("Delete Product", "Design does not exist")
            else:
                messagebox.showwarning("Delete Product", "Please select a design")

        delete_button = tk.Button(delete_window, text="Delete", font=("Arial", 12, "bold"),
                                  bg='#AED6F1', fg="black", command=delete_product_confirm)
        delete_button.pack(pady=20)

    def show_restock(self):
        # clear main content frame
        for widget in self.main_content.winfo_children():
            widget.destroy()

        tk.Label(self.main_content, text="Restock Products", font=("Arial", 20, "bold"),
                 bg='#AED6F1', fg="black").place(x=170, y=35)

        tk.Label(self.main_content, text="Select Design:").place(x=240, y=100)
        design_var = tk.StringVar()
        design_combobox = ttk.Combobox(self.main_content, textvariable=design_var)
        design_combobox['values'] = list(self.stock.keys())
        design_combobox.place(x=210, y=150)

        tk.Label(self.main_content, text="Select Size:").place(x=250, y=200)
        size_var = tk.StringVar()
        size_combobox = ttk.Combobox(self.main_content, textvariable=size_var)
        size_combobox['values'] = ["Small", "Medium", "Large", "XL"]
        size_combobox.place(x=210, y=250)

        tk.Label(self.main_content, text="Enter Quantity:").place(x=240, y=300)
        quantity_var = tk.StringVar()
        quantity_entry = tk.Entry(self.main_content, textvariable=quantity_var)
        quantity_entry.place(x=220, y=350)

        def restock():
            design = design_var.get()
            size = size_var.get()
            quantity = quantity_var.get()
            if design and size and quantity:
                try:
                    quantity = int(quantity)
                    if quantity > 0:
                        self.stock[design][size] += quantity
                        messagebox.showinfo("Restock", f"Restocked {quantity} units of {design} ({size})")
                        self.show_stock()  # Refresh stock display after restocking
                    else:
                        messagebox.showwarning("Restock", "Quantity must be a positive integer")
                except ValueError:
                    messagebox.showwarning("Restock", "Please enter a valid quantity")
            else:
                messagebox.showwarning("Restock", "Please select design, size, and enter a quantity")

        restock_button = tk.Button(self.main_content, text="Restock", font=("Arial", 12, "bold"),
                                   bg='#AED6F1', fg="black", command=restock, width=10)
        restock_button.place(x=230, y=400)

    def show_history(self):
        # clear main content frame
        for widget in self.main_content.winfo_children():
            widget.destroy()

        (tk.Label(self.main_content, text="Order History", bg='#AED6F1', font=("Arial", 16, "bold")).
         grid(row=0, column=0, pady=10, padx=10, sticky="w"))

        # treeview table
        columns = ("design", "size", "quantity")
        tree = ttk.Treeview(self.main_content, columns=columns, show='headings')
        tree.grid(row=1, column=0, sticky='nsew')

        # headings
        tree.heading("design", text="Design")
        tree.heading("size", text="Size")
        tree.heading("quantity", text="Quantity")

        # purchase history data to the table
        for purchase in self.purchases:
            tree.insert("", "end", values=(purchase[0], purchase[1], purchase[2]))

        # adjust column widths
        tree.column("design", width=200, anchor='center')
        tree.column("size", width=100, anchor='center')
        tree.column("quantity", width=100, anchor='center')

        # treeview expandable
        self.main_content.grid_rowconfigure(1, weight=1)
        self.main_content.grid_columnconfigure(0, weight=1)

    def logout(self):
        confirm = messagebox.askyesno("Confirm Logout", "Are you sure you want to logout?")
        if confirm:
            self.destroy()
            usertb.delete(0, tk.END)  # clear the username field
            passtb.delete(0, tk.END)  # clear the password field
            root.deiconify()  # show login window again


    def center_window(self):
            self.update_idletasks()
            width = self.winfo_width()
            height = self.winfo_height()
            screen_width = self.winfo_screenwidth()
            screen_height = self.winfo_screenheight()

            x = (screen_width // 2) - (width // 2)
            y = (screen_height // 2) - (height // 2)

            self.geometry(f'{width}x{height}+{x}+{y}')
def open_dashboard():
    dashboard = Dashboard(root)
def center_window(window):
    window.update_idletasks()
    width = window.winfo_width()
    height = window.winfo_height()
    screen_width = window.winfo_screenwidth()
    screen_height = window.winfo_screenheight()

    x = (screen_width // 2) - (width // 2)
    y = (screen_height // 2) - (height // 2)

    window.geometry(f'{width}x{height}+{x}+{y}')


# main function to open the login window
def open_login_window():
    global root, usertb, passtb

    root = tk.Tk()
    root.title("Inventory Management System")
    root.configure(bg='#AED6F1')
    root.geometry("700x500")

    center_window(root)
    root.resizable(False, False)

    usertxt = Label(root, text='Username: ', bg='#AED6F1', font=("Arial", 12))
    usertxt.place(x=150, y=290)

    passtxt = Label(root, text='Password: ', bg='#AED6F1', font=("Arial", 12))
    passtxt.place(x=150, y=330)

    usertb = Entry(root, font=('Arial', 13), width=18)
    usertb.place(x=270, y=290)

    passtb = Entry(root, font=('Arial', 13), show='*', width=18)
    passtb.place(x=270, y=330)

    # logo in login page
    try:
        # image path
        image = Image.open("C:\\Users\\aji\\OneDrive\\Pictures\\kbm.jpg")
        image = image.resize((200, 200))
        photo = ImageTk.PhotoImage(image)
        picture_label = Label(root, image=photo, bg='#AED6F1')
        picture_label.image = photo
        picture_label.place(x=250, y=50)
    except Exception as e:
        print(f"Error loading image: {e}")

    loginbtn = Button(root, text='Login', font=("Arial", 12, "bold"), bg='#2874A6', fg="white", bd=1, command=login,
                      relief=RAISED, width=16, height=1)
    loginbtn.place(x=270, y=390)

    root.mainloop()

open_login_window()