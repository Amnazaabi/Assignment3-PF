# Importing necessary functions from the binary_files_method module
from binary_files_method import write_to_binary_file, read_from_binary_file
# Importing the pickle module for serialization
import pickle

# Defining the Supplier class
class Supplier:
    # Constructor method to initialize Supplier object
    def __init__(self, supplier_id, name, address, contact_details, menu=None, min_guests=None, max_guests=None):
        # Assigning values to instance variables
        self.supplier_id = supplier_id
        self.name = name
        self.address = address
        self.contact_details = contact_details
        self.menu = menu
        self.min_guests = min_guests
        self.max_guests = max_guests

    # Method to save supplier data to a binary file
    def save_supplier(self):
        # Creating a dictionary containing supplier data
        supplier_data = {
            "Supplier ID": self.supplier_id,
            "Name": self.name,
            "Address": self.address,
            "Contact Details": self.contact_details,
            "Menu": self.menu,
            "Min Guests": self.min_guests,
            "Max Guests": self.max_guests
        }
        # Writing supplier data to a binary file using the write_to_binary_file function
        write_to_binary_file(supplier_data, "supplier_data_management.pkl")

    # Static method to get supplier data by ID from the binary file
    @staticmethod
    def get_supplier_by_id(supplier_id):
        # Reading supplier data from the binary file
        supplier_data = read_from_binary_file("supplier_data_management.pkl")
        # Iterating through supplier data to find the supplier with the specified ID
        for supplier in supplier_data:
            if supplier["Supplier ID"] == supplier_id:
                return supplier
        return None

    # Static method to delete supplier data by ID from the binary file
    @staticmethod
    def delete_supplier_by_id(supplier_id):
        # Reading supplier data from the binary file
        supplier_data = read_from_binary_file("supplier_data_management.pkl")
        # Checking if there is no supplier data
        if not supplier_data:
            print("No supplier data found.")
            return
        
        # Creating a list to store updated supplier data
        updated_supplier_data = []
        # Iterating through supplier data to filter out the supplier with the specified ID
        for supplier in supplier_data:
            if isinstance(supplier, dict) and "Supplier ID" in supplier and supplier["Supplier ID"] != supplier_id:
                updated_supplier_data.append(supplier)

        # Writing updated supplier data to the binary file
        with open("supplier_data_management.pkl", "wb") as file:
            for supplier in updated_supplier_data:
                pickle.dump(supplier, file)

    # Static method to modify supplier data by ID in the binary file
    @staticmethod
    def modify_supplier_by_id(supplier_id, updated_supplier_data):
        # Reading supplier data from the binary file
        supplier_data = read_from_binary_file("supplier_data_management.pkl")
        # Checking if there is no supplier data
        if not supplier_data:
            print("No supplier data found.")
            return
        
        # Creating a list to store updated supplier data
        updated_data = []
        # Iterating through supplier data to find the supplier with the specified ID and update its data
        for supplier in supplier_data:
            if isinstance(supplier, dict) and "Supplier ID" in supplier and supplier["Supplier ID"] == supplier_id:
                updated_data.append(updated_supplier_data)
            else:
                updated_data.append(supplier)

        # Writing updated supplier data to the binary file
        with open("supplier_data_management.pkl", "wb") as file:
            for data in updated_data:
                pickle.dump(data, file)
