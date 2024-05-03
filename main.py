# Import the tkinter library with the alias tk
import tkinter as tk
# Import the messagebox module from tkinter
from tkinter import messagebox
# Import classes from other interfaces
from employee_interface import EmployeeInterface
from event_interface import EventInterface
from client_interface import ClientInterface
from guest_interface import GuestInterface
from supplier_interface import SupplierInterface
from venue_interface import VenueInterface
 
# Create the MainApplication class
class MainApplication:
    # Constructor method to initialize the MainApplication object
    def __init__(self, root):
        # Store the root window
        self.root = root
        # Set the title of the root window
        self.root.title("Best Events Management System")
        # Set the background color of the root window
        self.root.configure(bg="#5B180F")
        # Configure the size of the root window
        self.root.geometry("400x300")

        # Create gradient colors
        gradient_color1 = "#F99B99"  # Light blue
        gradient_color2 = "#C4615B"  # Dark blue

        # Create button width
        button_width = 17

        # Create button style
        button_style = {"padx": 20, "pady": 10, "highlightthickness": 0, "bd": 0, "width": button_width, "bg": "#5B180F", "fg": "black"}

        # Create buttons for different management interfaces
        # Employee Management Button
        employee_button = tk.Button(root, text="Employee Management", command=self.open_employee_interface, **button_style)
        employee_button.pack(pady=5)

        # Event Management Button
        event_button = tk.Button(root, text="Event Management", command=self.open_event_interface, **button_style)
        event_button.pack(pady=5)

        # Client Management Button
        client_button = tk.Button(root, text="Client Management", command=self.open_client_interface, **button_style)
        client_button.pack(pady=5)

        # Guest Management Button
        guest_button = tk.Button(root, text="Guest Management", command=self.open_guest_interface, **button_style)
        guest_button.pack(pady=5)

        # Supplier Management Button
        supplier_button = tk.Button(root, text="Supplier Management", command=self.open_supplier_interface, **button_style)
        supplier_button.pack(pady=5)

        # Venue Management Button
        venue_button = tk.Button(root, text="Venue Management", command=self.open_venue_interface, **button_style)
        venue_button.pack(pady=5)

        # Apply gradient background color to buttons
        self.apply_gradient(employee_button, gradient_color1, gradient_color2)
        self.apply_gradient(event_button, gradient_color1, gradient_color2)
        self.apply_gradient(client_button, gradient_color1, gradient_color2)
        self.apply_gradient(guest_button, gradient_color1, gradient_color2)
        self.apply_gradient(supplier_button, gradient_color1, gradient_color2)
        self.apply_gradient(venue_button, gradient_color1, gradient_color2)

    # Method to apply gradient background color to buttons
    def apply_gradient(self, widget, color1, color2):
        # Apply initial gradient color
        widget.configure(bg=color1)
        # Change button color on mouse hover
        widget.bind("<Enter>", lambda event, widget=widget, color=color2: widget.config(bg=color))
        # Restore original color when mouse leaves the button
        widget.bind("<Leave>", lambda event, widget=widget, color=color1: widget.config(bg=color))

    # Method to open the Employee Management interface
    def open_employee_interface(self):
        # Create a new window for the Employee Management interface
        employee_window = tk.Toplevel(self.root)
        # Initialize the EmployeeInterface class
        employee_interface = EmployeeInterface(employee_window)

    # Method to open the Event Management interface
    def open_event_interface(self):
        # Create a new window for the Event Management interface
        event_window = tk.Toplevel(self.root)
        # Initialize the EventInterface class
        event_interface = EventInterface(event_window)

    # Method to open the Client Management interface
    def open_client_interface(self):
        # Create a new window for the Client Management interface
        client_window = tk.Toplevel(self.root)
        # Initialize the ClientInterface class
        client_interface = ClientInterface(client_window)

    # Method to open the Guest Management interface
    def open_guest_interface(self):
        # Create a new window for the Guest Management interface
        guest_window = tk.Toplevel(self.root)
        # Initialize the GuestInterface class
        guest_interface = GuestInterface(guest_window)

    # Method to open the Supplier Management interface
    def open_supplier_interface(self):
        # Create a new window for the Supplier Management interface
        supplier_window = tk.Toplevel(self.root)
        # Initialize the SupplierInterface class
        supplier_interface = SupplierInterface(supplier_window)

    # Method to open the Venue Management interface
    def open_venue_interface(self):
        # Create a new window for the Venue Management interface
        venue_window = tk.Toplevel(self.root)
        # Initialize the VenueInterface class
        venue_interface = VenueInterface(venue_window)

# Entry point of the application
if __name__ == "__main__":
    # Create the root window
    root = tk.Tk()
    # Initialize the MainApplication class
    app = MainApplication(root)
    # Start the tkinter event loop
    root.mainloop()
