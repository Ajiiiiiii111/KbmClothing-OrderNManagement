import tkinter as tk
from tkinter import ttk, messagebox

class Dashboard(tk.Toplevel):
    def __init__(self, parent):
        super().__init__(parent)
        self.parent = parent

        self.title("Dashboard")
        self.geometry("800x500")
        self.resizable(False, False)

        # Stock
        self.stock = {
            "Design 1": {"Small": 10, "Medium": 10, "Large": 10, "XL": 10},
            "Design 2": {"Small": 10, "Medium": 10, "Large": 10, "XL": 10},
            "Design 3": {"Small": 10, "Medium": 10, "Large": 10, "XL": 10}
        }

        # Initialize purchase history and total
        self.purchases = []
        self.total = 0

        # Sidebar
        self.sidebar = tk.Frame(self, width=200, bg='#AED6F1', height=600, relief='sunken', borderwidth=2)
        self.sidebar.pack(expand=False, fill='y', side='left', anchor='nw')

        # Main content frame
        self.main_content = tk.Frame(self, bg='#ecf0f1', width=600, height=600)
        self.main_content.pack(expand=True, fill='both', side='right')

        # Buttons in sidebar
        self.stock_button = tk.Button(self.sidebar, text="Stock", command=self.show_stock, width=20)
        self.stock_button.pack(pady=10, padx=15, fill='x')

        self.order_button = tk.Button(self.sidebar, text="Order", command=self.show_order)
        self.order_button.pack(pady=10, padx=15, fill='x')

        self.restock_button = tk.Button(self.sidebar, text="Restock", command=self.show_restock)
        self.restock_button.pack(pady=10, padx=15, fill='x')

        self.logout_button = tk.Button(self.sidebar, text="Logout", command=self.logout)
        self.logout_button.pack(pady=10, padx=15, fill='x')

    def show_stock(self):
        for widget in self.main_content.winfo_children():
            widget.destroy()

        tk.Label(self.main_content, text="Stock Information", font=("Arial", 16)).grid(row=0, column=0, pady=10, padx=10, sticky="w")

        # Treeview table
        columns = ("design", "small", "medium", "large", "xl")
        tree = ttk.Treeview(self.main_content, columns=columns, show='headings')
        tree.grid(row=1, column=0, sticky='nsew')

        # Define headings
        tree.heading("design", text="Design")
        tree.heading("small", text="Small")
        tree.heading("medium", text="Medium")
        tree.heading("large", text="Large")
        tree.heading("xl", text="XL")

        # Add stock data to the table
        for design, sizes in self.stock.items():
            tree.insert("", "end", values=(design, sizes["Small"], sizes["Medium"], sizes["Large"], sizes["XL"]))

        # Adjust column widths
        tree.column("design", width=150, anchor='center')
        tree.column("small", width=100, anchor='center')
        tree.column("medium", width=100, anchor='center')
        tree.column("large", width=100, anchor='center')
        tree.column("xl", width=100, anchor='center')

        # Make the treeview expandable
        self.main_content.grid_rowconfigure(1, weight=1)
        self.main_content.grid_columnconfigure(0, weight=1)

    def show_order(self):
        for widget in self.main_content.winfo_children():
            widget.destroy()

        tk.Label(self.main_content, text="Place Order", font=("Arial", 16)).pack(pady=10)

        tk.Label(self.main_content, text="Select Design:").pack(pady=5)
        design_var = tk.StringVar()
        design_combobox = ttk.Combobox(self.main_content, textvariable=design_var)
        design_combobox['values'] = list(self.stock.keys())
        design_combobox.pack(pady=5)

        tk.Label(self.main_content, text="Select Size:").pack(pady=5)
        size_var = tk.StringVar()
        size_combobox = ttk.Combobox(self.main_content, textvariable=size_var)
        size_combobox['values'] = ["Small", "Medium", "Large", "XL"]
        size_combobox.pack(pady=5)

        tk.Label(self.main_content, text="Enter Quantity:").pack(pady=5)
        quantity_var = tk.IntVar()
        quantity_entry = tk.Entry(self.main_content, textvariable=quantity_var)
        quantity_entry.pack(pady=5)

        def place_order():
            design = design_var.get()
            size = size_var.get()
            quantity = quantity_var.get()
            if design and size and quantity > 0:
                if self.stock[design][size] >= quantity:
                    self.stock[design][size] -= quantity
                    self.purchases.append((design, size, quantity))
                    self.total += quantity  # Assuming each item costs 1 unit for simplicity
                    messagebox.showinfo("Order", f"Order placed for {quantity} units of {design} ({size})")
                    self.update_purchase_history()
                else:
                    messagebox.showwarning("Order", f"Not enough stock for {design} ({size})")
            else:
                messagebox.showwarning("Order", "Please select design, size, and enter a valid quantity")

        order_button = tk.Button(self.main_content, text="Place Order", command=place_order)
        order_button.pack(pady=20)

        self.purchase_history_label = tk.Label(self.main_content, text="Purchase History:", font=("Arial", 14))
        self.purchase_history_label.pack(pady=10)

        self.purchase_history_text = tk.Text(self.main_content, height=10, width=50)
        self.purchase_history_text.pack(pady=5)

        self.total_label = tk.Label(self.main_content, text=f"Total: {self.total}", font=("Arial", 14))
        self.total_label.pack(pady=10)

    def show_restock(self):
        for widget in self.main_content.winfo_children():
            widget.destroy()

        tk.Label(self.main_content, text="Restock Products", font=("Arial", 16)).pack(pady=10)

        tk.Label(self.main_content, text="Select Design:").pack(pady=5)
        design_var = tk.StringVar()
        design_combobox = ttk.Combobox(self.main_content, textvariable=design_var)
        design_combobox['values'] = list(self.stock.keys())
        design_combobox.pack(pady=5)

        tk.Label(self.main_content, text="Select Size:").pack(pady=5)
        size_var = tk.StringVar()
        size_combobox = ttk.Combobox(self.main_content, textvariable=size_var)
        size_combobox['values'] = ["Small", "Medium", "Large", "XL"]
        size_combobox.pack(pady=5)

        tk.Label(self.main_content, text="Enter Quantity:").pack(pady=5)
        quantity_var = tk.IntVar()
        quantity_entry = tk.Entry(self.main_content, textvariable=quantity_var)
        quantity_entry.pack(pady=5)

        def restock():
            design = design_var.get()
            size = size_var.get()
            quantity = quantity_var.get()
            if design and size and quantity > 0:
                self.stock[design][size] += quantity
                messagebox.showinfo("Restock", f"Restocked {quantity} units of {design} ({size})")
                self.show_stock()
            else:
                messagebox.showwarning("Restock", "Please select design, size, and enter a valid quantity")

        restock_button = tk.Button(self.main_content, text="Restock", command=restock)
        restock_button.pack(pady=20)

    def update_purchase_history(self):
        self.purchase_history_text.delete(1.0, tk.END)
        for purchase in self.purchases:
            self.purchase_history_text.insert(tk.END, f"{purchase[2]} units of {purchase[0]} ({purchase[1]})\n")
        self.total_label.config(text=f"Total: {self.total}")

    def logout(self):
        self.destroy()
        self.parent.deiconify()
        self.usertb.delete(0, tk.END)  # Clear the username field
        self.passtb.delete(0, tk.END)  # Clear the password field
