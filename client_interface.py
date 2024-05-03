# Import the tkinter module and alias it as tk
import tkinter as tk
# Import the messagebox module from tkinter
from tkinter import messagebox
# Import the Client class from the client module
from client import Client

# Create a class called ClientInterface
class ClientInterface:
    def __init__(self, root):
        # Store the root window passed as an argument
        self.root = root
        # Set the title of the root window
        self.root.title("Client Management")

        # Set the background color of the root window to black
        self.root.configure(bg="#5B180F")
        # Set the dimensions of the root window
        self.root.geometry("350x250")

        # Create two gradient colors
        gradient_color1 = "#F99B99"  # Light blue
        gradient_color2 = "#C4615B"  # Dark blue
        
        # Create the width of buttons
        button_width = 17

        # Create a dictionary for button style
        button_style = {"padx": 20, "pady": 10, "highlightthickness": 0, "bd": 0, "width": button_width, "bg": "#5B180F", "fg": "black"}
        
        # Call a method to create the main menu with buttons
        self.create_main_menu(button_style, gradient_color1, gradient_color2)

    # Create a method to create the main menu with buttons
    def create_main_menu(self, button_style, color1, color2):
        # Create buttons for different functionalities
        add_client_button = tk.Button(self.root, text="Add Client", command=self.add_client, **button_style)
        # Pack the 'Add Client' button onto the root window
        add_client_button.pack(pady=5)

        # Create 'Display Clients' button
        display_client_button = tk.Button(self.root, text="Display Clients", command=self.display_clients, **button_style)
        display_client_button.pack(pady=5)

        # Create 'Delete Client' button
        delete_client_button = tk.Button(self.root, text="Delete Client", command=self.delete_client, **button_style)
        delete_client_button.pack(pady=5)

        # Create 'Modify Client' button
        modify_client_button = tk.Button(self.root, text="Modify Client", command=self.modify_client, **button_style)
        modify_client_button.pack(pady=5)

        # Apply gradient background colors to buttons
        self.apply_gradient(add_client_button, color1, color2)
        self.apply_gradient(display_client_button, color1, color2)
        self.apply_gradient(delete_client_button, color1, color2)
        self.apply_gradient(modify_client_button, color1, color2)

    # Create a method to handle adding a client
    def add_client(self):
        # Open a new window for adding client
        add_client_window = tk.Toplevel(self.root)
        # Set the title of the add client window
        add_client_window.title("Add Client")
        # Set the geometry of the add client window
        add_client_window.geometry("270x400")
        # Set the background color of the add client window
        add_client_window.configure(bg="#5B180F")

        # Create button width
        button_width = 17

        # Create button style for the add client window
        button_style = {"padx": 20, "pady": 10, "highlightthickness": 0, "bd": 0, "width": button_width, "bg": "#5B180F", "fg": "black"}

        # Create input fields for adding client
        id_label = tk.Label(add_client_window, text="Client ID:", bg="#5B180F", fg="white")
        id_label.pack(pady=5)
        id_entry = tk.Entry(add_client_window)
        id_entry.pack(pady=5)

        # Create labels and entry fields for client details
        name_label = tk.Label(add_client_window, text="Name:", bg="#5B180F", fg="white")
        name_label.pack(pady=5)
        name_entry = tk.Entry(add_client_window)
        name_entry.pack(pady=5)

        address_label = tk.Label(add_client_window, text="Address:", bg="#5B180F", fg="white")
        address_label.pack(pady=5)
        address_entry = tk.Entry(add_client_window)
        address_entry.pack(pady=5)

        contact_label = tk.Label(add_client_window, text="Contact Details:", bg="#5B180F", fg="white")
        contact_label.pack(pady=5)
        contact_entry = tk.Entry(add_client_window)
        contact_entry.pack(pady=5)

        budget_label = tk.Label(add_client_window, text="Budget:", bg="#5B180F", fg="white")
        budget_label.pack(pady=5)
        budget_entry = tk.Entry(add_client_window)
        budget_entry.pack(pady=5)

        # Create a function to validate Client ID
        def validate_client_id():
            client_id = id_entry.get()
            # Check if client ID contains only digits
            if not client_id.isdigit():
                # Show error message if client ID is not valid
                messagebox.showerror("Error", "Client ID must contain only digits.")
                return False
            return True

        # Create a function to save client details with validation
        def save_client():
            # Check if all input fields are filled
            if not all(entry.get() for entry in (id_entry, name_entry, address_entry, contact_entry, budget_entry)):
                # Show error message if any field is empty
                messagebox.showerror("Error", "All fields are required.")
                return
            # Validate client ID
            if not validate_client_id():
                return

            # Save client details
            self.save_client(id_entry.get(), name_entry.get(), address_entry.get(), contact_entry.get(), budget_entry.get())

        # Create a 'Save' button to add client
        save_button = tk.Button(add_client_window, text="Save", command=save_client, **button_style)
        save_button.pack(pady=10)

        # Apply gradient background color to save button
        self.apply_gradient(save_button, "#F99B99", "#C4615B")

    # Create a method to save client details
    def save_client(self, client_id, name, address, contact_details, budget):
        # Create a Client object with the provided data
        client = Client(client_id, name, address, contact_details, budget)

        # Call the save_client method from Client class to save the client data
        client.save_client()

        # Show success message
        messagebox.showinfo("Success", f"Client {name} added successfully.")

    # Create a method to display clients
    def display_clients(self):
        # Open a new window to display clients
        display_clients_window = tk.Toplevel(self.root)
        display_clients_window.title("Display Clients")

        # Set background color of the display clients window
        display_clients_window.configure(bg="#5B180F")
        # Set the dimensions of the display clients window
        display_clients_window.geometry("600x400")

        # Create button width
        button_width = 17

        # Create button style for the display clients window
        button_style = {"padx": 20, "pady": 10, "highlightthickness": 0, "bd": 0, "width": button_width, "bg": "#5B180F", "fg": "black"}

        # Create font for labels
        label_font = ("Arial", 12)

        # Create a label and entry for client ID
        id_label = tk.Label(display_clients_window, text="Enter Client ID:", bg="#5B180F", fg="white", font=label_font)
        id_label.pack(pady=5)
        id_entry = tk.Entry(display_clients_window)
        id_entry.pack(pady=5)

        # Create a function to display client details
        def display():
            client_id = id_entry.get()
            client = Client.get_client_by_id(client_id)
            if client:
                # Clear previous data
                data_text.delete(1.0, tk.END)
                # Display client data
                for key, value in client.items():
                    data_text.insert(tk.END, f"{key}: {value}\n")
            else:
                messagebox.showerror("Error", "Client ID not found.")

        # Create a text widget to display client data
        data_text = tk.Text(display_clients_window, bg="white", fg="black", font=label_font)
        data_text.pack(pady=5)

        # Create a button to display client data
        display_button = tk.Button(display_clients_window, text="Display", command=display, **button_style)
        display_button.pack(pady=10)

        # Create a label to show client data
        data_label = tk.Label(display_clients_window, text="", bg="#5B180F", fg="white", font=label_font)
        data_label.pack(pady=5)

        # Apply gradient background color to display button
        self.apply_gradient(display_button, "#F99B99", "#C4615B")

    # Create a method to delete a client
    def delete_client(self):
        # Open a new window to delete client
        delete_client_window = tk.Toplevel(self.root)
        delete_client_window.title("Delete Client")

        # Set background color of the delete client window
        delete_client_window.configure(bg="#5B180F")

        # Set the dimensions of the delete client window
        delete_client_window.geometry("300x250")

        # Create button width
        button_width = 17

        # Create button style for the delete client window
        button_style = {"padx": 20, "pady": 10, "highlightthickness": 0, "bd": 0, "width": button_width, "bg": "#5B180F", "fg": "black"}

        # Create font for labels
        label_font = ("Arial", 12)

        # Create a label and entry for client ID
        id_label = tk.Label(delete_client_window, text="Enter Client ID to Delete:", bg="#5B180F", fg="white", font=label_font)
        id_label.pack(pady=5)
        id_entry = tk.Entry(delete_client_window)
        id_entry.pack(pady=5)

        # Create a function to delete a client
        def delete():
            client_id = id_entry.get()
            if client_id:
                # Ask for confirmation before deleting
                if messagebox.askyesno("Confirmation", "Are you sure you want to delete this client?"):
                    # Delete the client
                    Client.delete_client_by_id(client_id)
                    # Show success message
                    messagebox.showinfo("Success", f"Client with ID {client_id} deleted successfully.")
                    # Close the delete client window
                    delete_client_window.destroy()
            else:
                # Show error message if no client ID is provided
                messagebox.showerror("Error", "Please enter Client ID.")

        # Create a button to delete a client
        delete_button = tk.Button(delete_client_window, text="Delete", command=delete, **button_style)
        delete_button.pack(pady=10)

        # Apply gradient background color to delete button
        self.apply_gradient(delete_button, "#F99B99", "#C4615B")

    # Create a method to modify a client
    def modify_client(self):
        # Open a new window to modify client
        modify_client_window = tk.Toplevel(self.root)
        modify_client_window.title("Modify Client")

        # Set background color of the modify client window
        modify_client_window.configure(bg="#5B180F")
        # Set the dimensions of the modify client window
        modify_client_window.geometry("270x400")

        # Create button width
        button_width = 17

        # Create button style for the modify client window
        button_style = {"padx": 20, "pady": 10, "highlightthickness": 0, "bd": 0, "width": button_width, "bg": "#5B180F", "fg": "black"}

        # Create font for labels
        label_font = ("Arial", 12)

        # Create a label and entry for client ID
        id_label = tk.Label(modify_client_window, text="Enter Client ID to Modify:", bg="#5B180F", fg="white", font=label_font)
        id_label.pack(pady=5)
        id_entry = tk.Entry(modify_client_window)
        id_entry.pack(pady=5)

        # Create input fields for modifying client
        name_label = tk.Label(modify_client_window, text="Name:", bg="#5B180F", fg="white")
        name_label.pack(pady=5)
        name_entry = tk.Entry(modify_client_window)
        name_entry.pack(pady=5)

        address_label = tk.Label(modify_client_window, text="Address:", bg="#5B180F", fg="white")
        address_label.pack(pady=5)
        address_entry = tk.Entry(modify_client_window)
        address_entry.pack(pady=5)

        contact_details_label = tk.Label(modify_client_window, text="Contact Details:", bg="#5B180F", fg="white")
        contact_details_label.pack(pady=5)
        contact_details_entry = tk.Entry(modify_client_window)
        contact_details_entry.pack(pady=5)

        budget_label = tk.Label(modify_client_window, text="Budget:", bg="#5B180F", fg="white")
        budget_label.pack(pady=5)
        budget_entry = tk.Entry(modify_client_window)
        budget_entry.pack(pady=5)

        # Create a function to modify a client
        def modify():
            client_id = id_entry.get()
            client = Client.get_client_by_id(client_id)
            if client:
                # Create a dictionary with updated client details
                updated_client = {
                    "Name": name_entry.get(),
                    "Client ID": client_id,
                    "Address": address_entry.get(),
                    "Contact Details": contact_details_entry.get(),
                    "Budget": budget_entry.get()
                }
                # Modify the client details
                Client.modify_client_by_id(client_id, updated_client)
                # Show success message
                messagebox.showinfo("Success", f"Client with ID {client_id} modified successfully.")
                # Close the modify client window
                modify_client_window.destroy()
            else:
                # Show error message if client ID is not found
                messagebox.showerror("Error", "Client ID not found.")

        # Create a 'Save' button to modify client
        save_button = tk.Button(modify_client_window, text="Save", command=modify, **button_style)
        save_button.pack(pady=10)

        # Apply gradient background color to save button
        self.apply_gradient(save_button, "#F99B99", "#C4615B")

    # Create a method to apply gradient background to widgets
    def apply_gradient(self, widget, color1, color2):
        # Apply gradient background color to widget
        widget.configure(bg=color1)
        # Bind mouse hover events to change background color
        widget.bind("<Enter>", lambda event, widget=widget, color=color2: widget.config(bg=color))
        widget.bind("<Leave>", lambda event, widget=widget, color=color1: widget.config(bg=color))

# Check if the script is being run directly
if __name__ == "__main__":
    # Create the root window
    root = tk.Tk()
    # Create an instance of the ClientInterface class with the root window
    app = ClientInterface(root)
    # Start the main event loop
    root.mainloop()
