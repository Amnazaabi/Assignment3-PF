import tkinter as tk
from tkinter import messagebox
from guest import Guest

class GuestInterface:
    def __init__(self, root):
        self.root = root
        self.root.title("Guest Management")

        # Set background color of the root window to black
        self.root.configure(bg="#5B180F")
        self.root.geometry("350x250")

        # Define gradient colors
        gradient_color1 = "#F99B99"  # Light blue
        gradient_color2 = "#C4615B"  # Dark blue
        
        button_width=17

        # Define button style
        button_style = {"padx": 20, "pady": 10, "highlightthickness": 0, "bd": 0, "width": button_width, "bg": "#5B180F", "fg": "black"}
        
        # Create main menu
        self.create_main_menu(button_style, gradient_color1, gradient_color2)

    def create_main_menu(self, button_style, color1, color2):
        # Main menu buttons
        add_guest_button = tk.Button(self.root, text="Add Guest", command=self.add_guest, **button_style)
        add_guest_button.pack(pady=5)

        display_guest_button = tk.Button(self.root, text="Display Guests", command=self.display_guests, **button_style)
        display_guest_button.pack(pady=5)

        delete_guest_button = tk.Button(self.root, text="Delete Guest", command=self.delete_guest, **button_style)
        delete_guest_button.pack(pady=5)

        modify_guest_button = tk.Button(self.root, text="Modify Guest", command=self.modify_guest, **button_style)
        modify_guest_button.pack(pady=5)

        # Apply gradient background color
        self.apply_gradient(add_guest_button, color1, color2)
        self.apply_gradient(display_guest_button, color1, color2)
        self.apply_gradient(delete_guest_button, color1, color2)
        self.apply_gradient(modify_guest_button, color1, color2)

    def add_guest(self):
        add_guest_window = tk.Toplevel(self.root)
        add_guest_window.title("Add Guest")
        add_guest_window.geometry("270x350")
        add_guest_window.configure(bg="#5B180F")

        button_width = 17
        button_style = {"padx": 20, "pady": 10, "highlightthickness": 0, "bd": 0, "width": button_width, "bg": "#5B180F", "fg": "black"}

        label_font = ("Arial", 12)

        guest_id_label = tk.Label(add_guest_window, text="Guest ID:", bg="#5B180F", fg="white", font=label_font)
        guest_id_label.pack(pady=5)
        guest_id_entry = tk.Entry(add_guest_window)
        guest_id_entry.pack(pady=5)

        name_label = tk.Label(add_guest_window, text="Name:", bg="#5B180F", fg="white", font=label_font)
        name_label.pack(pady=5)
        name_entry = tk.Entry(add_guest_window)
        name_entry.pack(pady=5)

        address_label = tk.Label(add_guest_window, text="Address:", bg="#5B180F", fg="white", font=label_font)
        address_label.pack(pady=5)
        address_entry = tk.Entry(add_guest_window)
        address_entry.pack(pady=5)

        contact_details_label = tk.Label(add_guest_window, text="Contact Details:", bg="#5B180F", fg="white", font=label_font)
        contact_details_label.pack(pady=5)
        contact_details_entry = tk.Entry(add_guest_window)
        contact_details_entry.pack(pady=5)

        # Function to validate Guest ID
        def validate_guest_id():
            guest_id = guest_id_entry.get()
            if not guest_id.isdigit():
                messagebox.showerror("Error", "Guest ID must contain only digits.")
                return False
            return True

        # Function to save guest details with validation
        def save_guest():
            if not all(entry.get() for entry in (guest_id_entry, name_entry, address_entry, contact_details_entry)):
                messagebox.showerror("Error", "All fields are required.")
                return
            if not validate_guest_id():
                return

            # Save guest details
            self.save_guest(guest_id_entry.get(), name_entry.get(), address_entry.get(), contact_details_entry.get())

        save_button = tk.Button(add_guest_window, text="Save", command=save_guest, **button_style)
        save_button.pack(pady=10)

        self.apply_gradient(save_button, "#F99B99", "#C4615B")

    def save_guest(self, guest_id, name, address, contact_details):
        guest = Guest(guest_id, name, address, contact_details)
        Guest.save_guest(guest)
        messagebox.showinfo("Success", f"Guest {name} added successfully.")
    def display_guests(self):
        # Open a new window to display guests
        display_guest_window = tk.Toplevel(self.root)
        display_guest_window.title("Display Guests")

        # Set background color of the display guest window
        display_guest_window.configure(bg="#5B180F")
        display_guest_window.geometry("600x600")

        button_width = 17

        # Define button style for the display guest window
        button_style = {"padx": 20, "pady": 10, "highlightthickness": 0, "bd": 0, "width": button_width, "bg": "#5B180F", "fg": "black"}

        label_font = ("Arial", 12)

        # Create a label and entry for guest ID
        id_label = tk.Label(display_guest_window, text="Enter Guest ID:", bg="#5B180F", fg="white", font=label_font)
        id_label.pack(pady=5)
        id_entry = tk.Entry(display_guest_window)
        id_entry.pack(pady=5)

        def display():
            guest_id = id_entry.get()
            guest = Guest.get_guest_by_id(guest_id)
            if guest:
                # Clear previous data
                data_text.delete(1.0, tk.END)
                # Display guest data
                for key, value in guest.items():
                    data_text.insert(tk.END, f"{key}: {value}\n")
            else:
                messagebox.showerror("Error", "Guest ID not found.")

        # Text widget to display guest data
        data_text = tk.Text(display_guest_window, bg="white", fg="black", font=label_font)
        data_text.pack(pady=5)

        # Button to display guest data
        display_button = tk.Button(display_guest_window, text="Display", command=display, **button_style)
        display_button.pack(pady=10)

        # Label to show guest data
        data_label = tk.Label(display_guest_window, text="", bg="#5B180F", fg="white", font=label_font)
        data_label.pack(pady=5)

        # Apply gradient background color to display button
        self.apply_gradient(display_button, "#F99B99", "#C4615B")


    def delete_guest(self):
        # Open a new window to delete guest
        delete_guest_window = tk.Toplevel(self.root)
        delete_guest_window.title("Delete Guest")

        # Set background color of the delete guest window
        delete_guest_window.configure(bg="#5B180F")
        delete_guest_window.geometry("300x200")

        button_width = 17

        # Define button style for the delete guest window
        button_style = {"padx": 20, "pady": 10, "highlightthickness": 0, "bd": 0, "width": button_width, "bg": "#5B180F", "fg": "black"}

        label_font = ("Arial", 12)

        # Create a label and entry for guest ID to delete
        id_label = tk.Label(delete_guest_window, text="Enter Guest ID to Delete:", bg="#5B180F", fg="white", font=label_font)
        id_label.pack(pady=5)
        id_entry = tk.Entry(delete_guest_window)
        id_entry.pack(pady=5)

        # Function to delete guest
        def delete():
            guest_id = id_entry.get()
            if guest_id:
                if messagebox.askyesno("Confirmation", "Are you sure you want to delete this guest?"):
                    # Here you would implement the functionality to delete the guest
                    messagebox.showinfo("Success", f"Guest with ID {guest_id} deleted successfully.")
                    delete_guest_window.destroy()
            else:
                messagebox.showerror("Error", "Please enter Guest ID.")

        # Button to delete guest
        delete_button = tk.Button(delete_guest_window, text="Delete", command=delete, **button_style)
        delete_button.pack(pady=10)

        # Apply gradient background color to delete button
        self.apply_gradient(delete_button, "#F99B99", "#C4615B")

    def modify_guest(self):
        # Open a new window to modify guest
        modify_guest_window = tk.Toplevel(self.root)
        modify_guest_window.title("Modify Guest")

        # Set background color of the modify guest window
        modify_guest_window.configure(bg="#5B180F")
        modify_guest_window.geometry("300x300")

        button_width = 17

        # Define button style for the modify guest window
        button_style = {"padx": 20, "pady": 10, "highlightthickness": 0, "bd": 0, "width": button_width, "bg": "#5B180F", "fg": "black"}

        label_font = ("Arial", 12)

        # Create a label and entry for guest ID to modify
        id_label = tk.Label(modify_guest_window, text="Enter Guest ID to Modify:", bg="#5B180F", fg="white", font=label_font)
        id_label.pack(pady=5)
        id_entry = tk.Entry(modify_guest_window)
        id_entry.pack(pady=5)

        # Input fields for modifying guest
        name_label = tk.Label(modify_guest_window, text="Name:", bg="#5B180F", fg="white", font=label_font)
        name_label.pack(pady=5)
        name_entry = tk.Entry(modify_guest_window)
        name_entry.pack(pady=5)

        address_label = tk.Label(modify_guest_window, text="Address:", bg="#5B180F", fg="white", font=label_font)
        address_label.pack(pady=5)
        address_entry = tk.Entry(modify_guest_window)
        address_entry.pack(pady=5)

        contact_details_label = tk.Label(modify_guest_window, text="Contact Details:", bg="#5B180F", fg="white", font=label_font)
        contact_details_label.pack(pady=5)
        contact_details_entry = tk.Entry(modify_guest_window)
        contact_details_entry.pack(pady=5)

        # Function to modify guest
        def modify():
            guest_id = id_entry.get()
            guest = Guest.get_guest_by_id(guest_id)
            if guest:
                updated_guest = {
                    "Guest ID": guest_id,
                    "Name": name_entry.get(),
                    "Address": address_entry.get(),
                    "Contact Details": contact_details_entry.get()
                }
                Guest.modify_guest_by_id(guest_id, updated_guest)
                messagebox.showinfo("Success", f"Guest with ID {guest_id} modified successfully.")
                modify_guest_window.destroy()
            else:
                messagebox.showerror("Error", "Guest ID not found.")

        # Button to modify guest
        modify_button = tk.Button(modify_guest_window, text="Modify", command=modify, **button_style)
        modify_button.pack(pady=10)

        # Apply gradient background color to modify button
        self.apply_gradient(modify_button, "#F99B99", "#C4615B")

    def apply_gradient(self, widget, color1, color2):
        # Apply gradient background color to widget
        widget.configure(bg=color1)
        widget.bind("<Enter>", lambda event, widget=widget, color=color2: widget.config(bg=color))
        widget.bind("<Leave>", lambda event, widget=widget, color=color1: widget.config(bg=color))
