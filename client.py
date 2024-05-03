# Importing the write_to_binary_file and read_from_binary_file functions from the binary_files_method module
from binary_files_method import write_to_binary_file, read_from_binary_file
# Importing the pickle module
import pickle

# Create a class called Client
class Client:
    # Create the constructor method for the class
    def __init__(self, client_id, name, address, contact_details, budget):
        # Initialize attributes for client data
        self.client_id = client_id
        self.name = name
        self.address = address
        self.contact_details = contact_details
        self.budget = budget

    # Create a method to save client data to a binary file
    def save_client(self):
        # Create a dictionary containing client data
        client_data = {
            "Client ID": self.client_id,
            "Name": self.name,
            "Address": self.address,
            "Contact Details": self.contact_details,
            "Budget": self.budget
        }
        # Call the write_to_binary_file function to write client data to a binary file
        write_to_binary_file(client_data, "client_data_management.pkl")

    # Create a static method to get client data by ID from the binary file
    @staticmethod
    def get_client_by_id(client_id):
        # Read client data from the binary file
        client_data = read_from_binary_file("client_data_management.pkl")
        # Iterate through client data
        for client in client_data:
            # Check if the client ID matches the specified ID
            if client["Client ID"] == client_id:
                return client
        return None

    # Create a static method to delete client data by ID from the binary file
    @staticmethod
    def delete_client_by_id(client_id):
        # Read client data from the binary file
        client_data = read_from_binary_file("client_data_management.pkl")
        # Check if there is no client data
        if not client_data:
            print("No client data found.")
            return
        
        # Create an empty list to store updated client data
        updated_client_data = []
        # Iterate through client data
        for client in client_data:
            # Check if the client is a dictionary and contains "Client ID", and if the ID does not match the specified ID
            if isinstance(client, dict) and "Client ID" in client and client["Client ID"] != client_id:
                # Append the client data to the updated list
                updated_client_data.append(client)

        # Open the binary file in write mode
        with open("client_data_management.pkl", "wb") as file:
            # Iterate through updated client data and write it to the file
            for client in updated_client_data:
                pickle.dump(client, file)

    # Create a static method to modify client data by ID in the binary file
    @staticmethod
    def modify_client_by_id(client_id, updated_client_data):
        # Read client data from the binary file
        client_data = read_from_binary_file("client_data_management.pkl")
        # Check if there is no client data
        if not client_data:
            print("No client data found.")
            return
        
        # Create an empty list to store updated data
        updated_data = []
        # Iterate through client data
        for client in client_data:
            # Check if the client is a dictionary, contains "Client ID", and if the ID matches the specified ID
            if isinstance(client, dict) and "Client ID" in client and client["Client ID"] == client_id:
                # Append the updated client data to the updated list
                updated_data.append(updated_client_data)
            else:
                # Append the original client data to the updated list
                updated_data.append(client)

        # Open the binary file in write mode
        with open("client_data_management.pkl", "wb") as file:
            # Iterate through updated data and write it to the file
            for data in updated_data:
                pickle.dump(data, file)
