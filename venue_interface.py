# Importing tkinter module as tk
import tkinter as tk
# Importing messagebox module from tkinter for displaying dialog boxes
from tkinter import messagebox
# Importing Venue class from venue.py file
from venue import Venue


# Defining the VenueInterface class
class VenueInterface:
    # Constructor method to initialize VenueInterface object
    def __init__(self, root):
        # Assigning the root window to the instance variable 'root'
        self.root = root
        # Setting the title of the root window
        self.root.title("Venue Management")
        # Configuring the background color of the root window
        self.root.configure(bg="#5B180F")
        # Setting the geometry of the root window
        self.root.geometry("350x250")

        # Define gradient colors
        gradient_color1 = "#F99B99"  # Light blue
        gradient_color2 = "#C4615B"  # Dark blue
        # Define button width
        button_width = 17
        # Define button style
        button_style = {"padx": 20, "pady": 10, "highlightthickness": 0, "bd": 0, "width": button_width, "bg": "#5B180F", "fg": "black"}

        # Create the main menu for venue management
        self.create_main_menu(button_style, gradient_color1, gradient_color2)

    # Method to create the main menu for venue management
    def create_main_menu(self, button_style, color1, color2):
        #create button
        add_venue_button = tk.Button(self.root, text="Add Venue", command=self.add_venue, **button_style)
        add_venue_button.pack(pady=5)

        # Create button for displaying venues
        display_venue_button = tk.Button(self.root, text="Display Venues", command=self.display_venues, **button_style)
        display_venue_button.pack(pady=5)

        delete_venue_button = tk.Button(self.root, text="Delete Venue", command=self.delete_venue, **button_style)
        delete_venue_button.pack(pady=5)

        modify_venue_button = tk.Button(self.root, text="Modify Venue", command=self.modify_venue, **button_style)
        modify_venue_button.pack(pady=5)

        # Apply gradient background color to buttons
        self.apply_gradient(add_venue_button, color1, color2)
        self.apply_gradient(display_venue_button, color1, color2)
        self.apply_gradient(delete_venue_button, color1, color2)
        self.apply_gradient(modify_venue_button, color1, color2)

    # Method to add a new venue
    def add_venue(self):
        # Create a new window for adding a venue
        add_venue_window = tk.Toplevel(self.root)
        add_venue_window.title("Add Venue")
        add_venue_window.geometry("350x400")
        add_venue_window.configure(bg="#5B180F")

        button_width = 17
        button_style = {"padx": 20, "pady": 10, "highlightthickness": 0, "bd": 0, "width": button_width, "bg": "#5B180F", "fg": "black"}

        label_font = ("Arial", 12)

        # Create labels and entry fields for venue details (ID, name, address, contact, min guests, max guests)
        venue_id_label = tk.Label(add_venue_window, text="Venue ID:", bg="#5B180F", fg="white", font=label_font)
        venue_id_label.pack(pady=5)
        venue_id_entry = tk.Entry(add_venue_window)
        venue_id_entry.pack(pady=5)

        name_label = tk.Label(add_venue_window, text="Name:", bg="#5B180F", fg="white", font=label_font)
        name_label.pack(pady=5)
        name_entry = tk.Entry(add_venue_window)
        name_entry.pack(pady=5)

        address_label = tk.Label(add_venue_window, text="Address:", bg="#5B180F", fg="white", font=label_font)
        address_label.pack(pady=5)
        address_entry = tk.Entry(add_venue_window)
        address_entry.pack(pady=5)

        contact_label = tk.Label(add_venue_window, text="Contact:", bg="#5B180F", fg="white", font=label_font)
        contact_label.pack(pady=5)
        contact_entry = tk.Entry(add_venue_window)
        contact_entry.pack(pady=5)

        min_guests_label = tk.Label(add_venue_window, text="Minimum Guests:", bg="#5B180F", fg="white", font=label_font)
        min_guests_label.pack(pady=5)
        min_guests_entry = tk.Entry(add_venue_window)
        min_guests_entry.pack(pady=5)

        max_guests_label = tk.Label(add_venue_window, text="Maximum Guests:", bg="#5B180F", fg="white", font=label_font)
        max_guests_label.pack(pady=5)
        max_guests_entry = tk.Entry(add_venue_window)
        max_guests_entry.pack(pady=5)

        def save_venue():
            venue = Venue(
                venue_id=venue_id_entry.get(),
                name=name_entry.get(),
                address=address_entry.get(),
                contact=contact_entry.get(),
                min_guests=min_guests_entry.get(),
                max_guests=max_guests_entry.get()
            )
            venue.save_venue()
            messagebox.showinfo("Success", f"Venue {name_entry.get()} added successfully.")

        save_button = tk.Button(add_venue_window, text="Save", command=save_venue, **button_style)
        save_button.pack(pady=10)

        self.apply_gradient(save_button, "#F99B99", "#C4615B")

    def display_venues(self):
        display_venue_window = tk.Toplevel(self.root)
        display_venue_window.title("Display Venues")
        display_venue_window.geometry("600x400")
        display_venue_window.configure(bg="#5B180F")

        button_width = 17

        button_style = {"padx": 20, "pady": 10, "highlightthickness": 0, "bd": 0, "width": button_width, "bg": "#5B180F", "fg": "black"}

        label_font = ("Arial", 12)

        venue_id_label = tk.Label(display_venue_window, text="Enter Venue ID:", bg="#5B180F", fg="white", font=label_font)
        venue_id_label.pack(pady=5)
        venue_id_entry = tk.Entry(display_venue_window)
        venue_id_entry.pack(pady=5)

        data_text = tk.Text(display_venue_window, bg="white", fg="black", font=label_font)
        data_text.pack(pady=5)

        def display():
            venue_id = venue_id_entry.get()
            venue = Venue.get_venue_by_id(venue_id)
            if venue:
                data_text.delete(1.0, tk.END)
                for key, value in venue.items():
                    data_text.insert(tk.END, f"{key}: {value}\n")
            else:
                messagebox.showerror("Error", "Venue ID not found.")

        display_button = tk.Button(display_venue_window, text="Display", command=display, **button_style)
        display_button.pack(pady=10)

        self.apply_gradient(display_button, "#F99B99", "#C4615B")

    def delete_venue(self):
        delete_venue_window = tk.Toplevel(self.root)
        delete_venue_window.title("Delete Venue")
        delete_venue_window.geometry("300x200")
        delete_venue_window.configure(bg="#5B180F")

        button_width = 17

        button_style = {"padx": 20, "pady": 10, "highlightthickness": 0, "bd": 0, "width": button_width, "bg": "#5B180F", "fg": "black"}


        label_font = ("Arial", 12)

        venue_id_label = tk.Label(delete_venue_window, text="Enter Venue ID to Delete:", bg="#5B180F", fg="white", font=label_font)
        venue_id_label.pack(pady=5)
        venue_id_entry = tk.Entry(delete_venue_window)
        venue_id_entry.pack(pady=5)

        def delete():
            venue_id = venue_id_entry.get()
            if venue_id:
                if messagebox.askyesno("Confirmation", "Are you sure you want to delete this venue?"):
                    Venue.delete_venue_by_id(venue_id)
                    messagebox.showinfo("Success", f"Venue with ID {venue_id} deleted successfully.")
                    delete_venue_window.destroy()
            else:
                messagebox.showerror("Error", "Please enter Venue ID.")

        delete_button = tk.Button(delete_venue_window, text="Delete", command=delete, **button_style)
        delete_button.pack(pady=10)

        self.apply_gradient(delete_button, "#F99B99", "#C4615B")

    def modify_venue(self):
        modify_venue_window = tk.Toplevel(self.root)
        modify_venue_window.title("Modify Venue")
        modify_venue_window.geometry("350x400")
        modify_venue_window.configure(bg="#5B180F")

        button_width = 17

        button_style = {"padx": 20, "pady": 10, "highlightthickness": 0, "bd": 0, "width": button_width, "bg": "#5B180F", "fg": "black"}

        label_font = ("Arial", 12)

        venue_id_label = tk.Label(modify_venue_window, text="Enter Venue ID to Modify:", bg="#5B180F", fg="white", font=label_font)
        venue_id_label.pack(pady=5)
        venue_id_entry = tk.Entry(modify_venue_window)
        venue_id_entry.pack(pady=5)

        name_label = tk.Label(modify_venue_window, text="Name:", bg="#5B180F", fg="white", font=label_font)
        name_label.pack(pady=5)
        name_entry = tk.Entry(modify_venue_window)
        name_entry.pack(pady=5)

        address_label = tk.Label(modify_venue_window, text="Address:", bg="#5B180F", fg="white", font=label_font)
        address_label.pack(pady=5)
        address_entry = tk.Entry(modify_venue_window)
        address_entry.pack(pady=5)

        contact_label = tk.Label(modify_venue_window, text="Contact:", bg="#5B180F", fg="white", font=label_font)
        contact_label.pack(pady=5)
        contact_entry = tk.Entry(modify_venue_window)
        contact_entry.pack(pady=5)

        min_guests_label = tk.Label(modify_venue_window, text="Minimum Guests:", bg="#5B180F", fg="white", font=label_font)
        min_guests_label.pack(pady=5)
        min_guests_entry = tk.Entry(modify_venue_window)
        min_guests_entry.pack(pady=5)

        max_guests_label = tk.Label(modify_venue_window, text="Maximum Guests:", bg="#5B180F", fg="white", font=label_font)
        max_guests_label.pack(pady=5)
        max_guests_entry = tk.Entry(modify_venue_window)
        max_guests_entry.pack(pady=5)

        def modify():
            venue_id = venue_id_entry.get()
            venue = Venue.get_venue_by_id(venue_id)
            if venue:
                updated_venue = {
                    "Venue ID": venue_id,
                    "Name": name_entry.get(),
                    "Address": address_entry.get(),
                    "Contact": contact_entry.get(),
                    "Min Guests": min_guests_entry.get(),
                    "Max Guests": max_guests_entry.get()
                }
                Venue.modify_venue_by_id(venue_id, updated_venue)
                messagebox.showinfo("Success", f"Venue with ID {venue_id} modified successfully.")
                modify_venue_window.destroy()
            else:
                messagebox.showerror("Error", "Venue ID not found.")

        save_button = tk.Button(modify_venue_window, text="Save", command=modify, **button_style)
        save_button.pack(pady=10)

        self.apply_gradient(save_button, "#F99B99", "#C4615B")

    def apply_gradient(self, widget, color1, color2):
        widget.configure(bg=color1)
        widget.bind("<Enter>", lambda event, widget=widget, color=color2: widget.config(bg=color))
        widget.bind("<Leave>", lambda event, widget=widget, color=color1: widget.config(bg=color))

if __name__ == "__main__":
    # Create the root window
    root = tk.Tk()
    # Create an instance of the VenueInterface class
    app = VenueInterface(root)
    # Run the tkinter event loop
    root.mainloop()
