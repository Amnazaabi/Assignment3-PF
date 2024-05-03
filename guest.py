# Importing functions for writing to and reading from binary files
from binary_files_method import write_to_binary_file, read_from_binary_file
# Importing the pickle module for serialization
import pickle

# Create a class called Guest
class Guest:
    # Create the constructor method for the class
    def __init__(self, guest_id, name, address, contact_details):
        # Initialize instance variables with provided data
        self.guest_id = guest_id
        self.name = name
        self.address = address
        self.contact_details = contact_details

    # Create a method to save guest data to a binary file
    def save_guest(self):
        # Create a dictionary to represent the guest data
        guest_data = {
            "Guest ID": self.guest_id,
            "Name": self.name,
            "Address": self.address,
            "Contact Details": self.contact_details
        }
        # Write guest data to a binary file
        write_to_binary_file(guest_data, "guest_data_management.pkl")

    # Create a static method to get guest data by ID from a binary file
    @staticmethod
    def get_guest_by_id(guest_id):
        # Read guest data from the binary file
        guest_data = read_from_binary_file("guest_data_management.pkl")
        # Iterate through guest data
        for guest in guest_data:
            # Check if guest ID matches the provided ID
            if guest["Guest ID"] == guest_id:
                return guest
        return None

    # Create a static method to delete guest data by ID from a binary file
    @staticmethod
    def delete_guest_by_id(guest_id):
        # Read guest data from the binary file
        guest_data = read_from_binary_file("guest_data_management.pkl")
        # Check if guest data exists
        if not guest_data:
            print("No guest data found.")
            return
        # Create an updated list of guest data excluding the specified guest ID
        updated_guest_data = []
        for guest in guest_data:
            if isinstance(guest, dict) and "Guest ID" in guest and guest["Guest ID"] != guest_id:
                updated_guest_data.append(guest)
        # Write the updated guest data to the binary file
        with open("guest_data_management.pkl", "wb") as file:
            for guest in updated_guest_data:
                pickle.dump(guest, file)

    # Create a static method to modify guest data by ID in a binary file
    @staticmethod
    def modify_guest_by_id(guest_id, updated_guest_data):
        # Read guest data from the binary file
        guest_data = read_from_binary_file("guest_data_management.pkl")
        # Check if guest data exists
        if not guest_data:
            print("No guest data found.")
            return
        # Create an updated list of guest data with the specified guest ID modified
        updated_data = []
        for guest in guest_data:
            if isinstance(guest, dict) and "Guest ID" in guest and guest["Guest ID"] == guest_id:
                updated_data.append(updated_guest_data)
            else:
                updated_data.append(guest)
        # Write the updated guest data to the binary file
        with open("guest_data_management.pkl", "wb") as file:
            for data in updated_data:
                pickle.dump(data, file)
