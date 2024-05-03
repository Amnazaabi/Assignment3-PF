# Importing tkinter module as tk
import tkinter as tk
# Importing messagebox from tkinter module
from tkinter import messagebox
# Importing Supplier class from supplier module
from supplier import Supplier

# Defining the SupplierInterface class
class SupplierInterface:
    # Constructor method to initialize SupplierInterface object
    def __init__(self, root):
        # Setting the root window
        self.root = root
        # Setting the title of the root window
        self.root.title("Supplier Management")
        # Setting the background color of the root window
        self.root.configure(bg="#5B180F")
        # Setting the geometry of the root window
        self.root.geometry("350x250")

        # Defining gradient colors
        gradient_color1 = "#F99B99"  # Light blue
        gradient_color2 = "#C4615B"  # Dark blue
        # Defining button width
        button_width = 17
        # Defining button style
        button_style = {"padx": 20, "pady": 10, "highlightthickness": 0, "bd": 0, "width": button_width, "bg": "#5B180F", "fg": "black"}
        
        # Creating the main menu for supplier management
        self.create_main_menu(button_style, gradient_color1, gradient_color2)


    # Method to create the main menu for supplier management
    def create_main_menu(self, button_style, color1, color2):
        # Creating "Add Supplier" button
        add_supplier_button = tk.Button(self.root, text="Add Supplier", command=self.add_supplier, **button_style)
        add_supplier_button.pack(pady=5)

        # Creating "Display Suppliers" button
        display_supplier_button = tk.Button(self.root, text="Display Suppliers", command=self.display_suppliers, **button_style)
        display_supplier_button.pack(pady=5)

        # Creating "Delete Supplier" button
        delete_supplier_button = tk.Button(self.root, text="Delete Supplier", command=self.delete_supplier, **button_style)
        delete_supplier_button.pack(pady=5)

        # Creating "Modify Supplier" button
        modify_supplier_button = tk.Button(self.root, text="Modify Supplier", command=self.modify_supplier, **button_style)
        modify_supplier_button.pack(pady=5)

        # Applying gradient background color to buttons
        self.apply_gradient(add_supplier_button, color1, color2)
        self.apply_gradient(display_supplier_button, color1, color2)
        self.apply_gradient(delete_supplier_button, color1, color2)
        self.apply_gradient(modify_supplier_button, color1, color2)

    # Method to add a new supplier
    def add_supplier(self):
        # Creating a new window for adding a supplier
        add_supplier_window = tk.Toplevel(self.root)
        add_supplier_window.title("Add Supplier")
        add_supplier_window.geometry("270x500")
        add_supplier_window.configure(bg="#5B180F")

        # Defining button width
        button_width = 17
        # Defining button style
        button_style = {"padx": 20, "pady": 10, "highlightthickness": 0, "bd": 0, "width": button_width, "bg": "#5B180F", "fg": "black"}

        # Creating labels and entry fields for supplier details
        id_label = tk.Label(add_supplier_window, text="Supplier ID:", bg="#5B180F", fg="white")
        id_label.pack(pady=5)
        id_entry = tk.Entry(add_supplier_window)
        id_entry.pack(pady=5)

        name_label = tk.Label(add_supplier_window, text="Name:", bg="#5B180F", fg="white")
        name_label.pack(pady=5)
        name_entry = tk.Entry(add_supplier_window)
        name_entry.pack(pady=5)

        address_label = tk.Label(add_supplier_window, text="Address:", bg="#5B180F", fg="white")
        address_label.pack(pady=5)
        address_entry = tk.Entry(add_supplier_window)
        address_entry.pack(pady=5)

        contact_label = tk.Label(add_supplier_window, text="Contact Details:", bg="#5B180F", fg="white")
        contact_label.pack(pady=5)
        contact_entry = tk.Entry(add_supplier_window)
        contact_entry.pack(pady=5)

        menu_label = tk.Label(add_supplier_window, text="Menu:", bg="#5B180F", fg="white")
        menu_label.pack(pady=5)
        menu_entry = tk.Entry(add_supplier_window)
        menu_entry.pack(pady=5)

        min_guests_label = tk.Label(add_supplier_window, text="Min Guests:", bg="#5B180F", fg="white")
        min_guests_label.pack(pady=5)
        min_guests_entry = tk.Entry(add_supplier_window)
        min_guests_entry.pack(pady=5)

        max_guests_label = tk.Label(add_supplier_window, text="Max Guests:", bg="#5B180F", fg="white")
        max_guests_label.pack(pady=5)
        max_guests_entry = tk.Entry(add_supplier_window)
        max_guests_entry.pack(pady=5)

        # Defining a function to save supplier details
        def save_supplier():
            # Getting values from entry fields
            supplier_id = id_entry.get()
            name = name_entry.get()
            address = address_entry.get()
            contact_details = contact_entry.get()
            menu = menu_entry.get()
            min_guests = min_guests_entry.get()
            max_guests = max_guests_entry.get()

            supplier = Supplier(supplier_id, name, address, contact_details, menu, min_guests, max_guests)
            supplier.save_supplier()

            # Showing success message
            messagebox.showinfo("Success", f"Supplier {name} added successfully.")
            add_supplier_window.destroy()

        # Creating a "Save" button
        save_button = tk.Button(add_supplier_window, text="Save", command=save_supplier, **button_style)
        save_button.pack(pady=10)
        # Applying gradient background color to the save button
        self.apply_gradient(save_button, "#F99B99", "#C4615B")

    def display_suppliers(self):
        display_suppliers_window = tk.Toplevel(self.root)
        display_suppliers_window.title("Display Suppliers")
        display_suppliers_window.geometry("600x600")
        display_suppliers_window.configure(bg="#5B180F")

        button_width = 17
        button_style = {"padx": 20, "pady": 10, "highlightthickness": 0, "bd": 0, "width": button_width, "bg": "#5B180F", "fg": "black"}

        label_font = ("Arial", 12)

        id_label = tk.Label(display_suppliers_window, text="Enter Supplier ID:", bg="#5B180F", fg="white", font=label_font)
        id_label.pack(pady=5)
        id_entry = tk.Entry(display_suppliers_window)
        id_entry.pack(pady=5)

        def display():
            supplier_id = id_entry.get()
            supplier = Supplier.get_supplier_by_id(supplier_id)
            if supplier:
                data_text.delete(1.0, tk.END)
                for key, value in supplier.items():
                    data_text.insert(tk.END, f"{key}: {value}\n")
            else:
                messagebox.showerror("Error", "Supplier ID not found.")

        data_text = tk.Text(display_suppliers_window, bg="white", fg="black", font=label_font)
        data_text.pack(pady=5)

        display_button = tk.Button(display_suppliers_window, text="Display", command=display, **button_style)
        display_button.pack(pady=10)

        data_label = tk.Label(display_suppliers_window, text="", bg="#5B180F", fg="white", font=label_font)
        data_label.pack(pady=5)

        self.apply_gradient(display_button, "#F99B99", "#C4615B")

    def delete_supplier(self):
        delete_supplier_window = tk.Toplevel(self.root)
        delete_supplier_window.title("Delete Supplier")
        delete_supplier_window.geometry("300x300")
        delete_supplier_window.configure(bg="#5B180F")

        button_width = 17
        button_style = {"padx": 20, "pady": 10, "highlightthickness": 0, "bd": 0, "width": button_width, "bg": "#5B180F", "fg": "black"}

        label_font = ("Arial", 12)

        id_label = tk.Label(delete_supplier_window, text="Enter Supplier ID to Delete:", bg="#5B180F", fg="white", font=label_font)
        id_label.pack(pady=5)
        id_entry = tk.Entry(delete_supplier_window)
        id_entry.pack(pady=5)

        def delete():
            supplier_id = id_entry.get()
            if supplier_id:
                if messagebox.askyesno("Confirmation", "Are you sure you want to delete this supplier?"):
                    Supplier.delete_supplier_by_id(supplier_id)
                    messagebox.showinfo("Success", f"Supplier with ID {supplier_id} deleted successfully.")
                    delete_supplier_window.destroy()
            else:
                messagebox.showerror("Error", "Please enter Supplier ID.")

        delete_button = tk.Button(delete_supplier_window, text="Delete", command=delete, **button_style)
        delete_button.pack(pady=10)

        self.apply_gradient(delete_button, "#F99B99", "#C4615B")

    def modify_supplier(self):
        modify_supplier_window = tk.Toplevel(self.root)
        modify_supplier_window.title("Modify Supplier")
        modify_supplier_window.geometry("270x550")
        modify_supplier_window.configure(bg="#5B180F")

        button_width = 17
        button_style = {"padx": 20, "pady": 10, "highlightthickness": 0, "bd": 0, "width": button_width, "bg": "#5B180F", "fg": "black"}

        label_font = ("Arial", 12)

        id_label = tk.Label(modify_supplier_window, text="Enter Supplier ID to Modify:", bg="#5B180F", fg="white", font=label_font)
        id_label.pack(pady=5)
        id_entry = tk.Entry(modify_supplier_window)
        id_entry.pack(pady=5)

        name_label = tk.Label(modify_supplier_window, text="Name:", bg="#5B180F", fg="white")
        name_label.pack(pady=5)
        name_entry = tk.Entry(modify_supplier_window)
        name_entry.pack(pady=5)

        address_label = tk.Label(modify_supplier_window, text="Address:", bg="#5B180F", fg="white")
        address_label.pack(pady=5)
        address_entry = tk.Entry(modify_supplier_window)
        address_entry.pack(pady=5)

        contact_label = tk.Label(modify_supplier_window, text="Contact Details:", bg="#5B180F", fg="white")
        contact_label.pack(pady=5)
        contact_entry = tk.Entry(modify_supplier_window)
        contact_entry.pack(pady=5)

        menu_label = tk.Label(modify_supplier_window, text="Menu:", bg="#5B180F", fg="white")
        menu_label.pack(pady=5)
        menu_entry = tk.Entry(modify_supplier_window)
        menu_entry.pack(pady=5)

        min_guests_label = tk.Label(modify_supplier_window, text="Min Guests:", bg="#5B180F", fg="white")
        min_guests_label.pack(pady=5)
        min_guests_entry = tk.Entry(modify_supplier_window)
        min_guests_entry.pack(pady=5)

        max_guests_label = tk.Label(modify_supplier_window, text="Max Guests:", bg="#5B180F", fg="white")
        max_guests_label.pack(pady=5)
        max_guests_entry = tk.Entry(modify_supplier_window)
        max_guests_entry.pack(pady=5)

        def modify():
            supplier_id = id_entry.get()
            supplier = Supplier.get_supplier_by_id(supplier_id)
            if supplier:
                updated_supplier = {
                    "Name": name_entry.get(),
                    "Supplier ID": supplier_id,
                    "Address": address_entry.get(),
                    "Contact Details": contact_entry.get(),
                    "Menu": menu_entry.get(),
                    "Min Guests": min_guests_entry.get(),
                    "Max Guests": max_guests_entry.get()
                }
                Supplier.modify_supplier_by_id(supplier_id, updated_supplier)
                messagebox.showinfo("Success", f"Supplier with ID {supplier_id} modified successfully.")
                modify_supplier_window.destroy()
            else:
                messagebox.showerror("Error", "Supplier ID not found.")

        save_button = tk.Button(modify_supplier_window, text="Save", command=modify, **button_style)
        save_button.pack(pady=10)

        self.apply_gradient(save_button, "#F99B99", "#C4615B")
    
    # Method to apply gradient background to a widget
    def apply_gradient(self, widget, color1, color2):
        # Apply gradient background color to widget
        widget.configure(bg=color1)
        widget.bind("<Enter>", lambda event, widget=widget, color=color2: widget.config(bg=color))
        widget.bind("<Leave>", lambda event, widget=widget, color=color1: widget.config(bg=color))

# Creating the root window and SupplierInterface object
if __name__ == "__main__":
    root = tk.Tk()
    app = SupplierInterface(root)
    root.mainloop()
