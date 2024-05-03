# Importing necessary functions from the binary_files_method module
from binary_files_method import write_to_binary_file, read_from_binary_file
# Importing the pickle module for serialization
import pickle

# Defining the Venue class
class Venue:
    # Constructor method to initialize Venue object
    def __init__(self, venue_id, name, address, contact, min_guests, max_guests):
        # Assigning values to instance variables
        self.venue_id = venue_id
        self.name = name
        self.address = address
        self.contact = contact
        self.min_guests = min_guests
        self.max_guests = max_guests

    # Method to save venue data to a binary file
    def save_venue(self):
        # Creating a dictionary containing venue data
        venue_data = {
            "Venue ID": self.venue_id,
            "Name": self.name,
            "Address": self.address,
            "Contact": self.contact,
            "Min Guests": self.min_guests,
            "Max Guests": self.max_guests
        }
        # Writing venue data to a binary file using the write_to_binary_file function
        write_to_binary_file(venue_data, "venue_data_management.pkl")

    # Static method to get venue data by ID from the binary file
    @staticmethod
    def get_venue_by_id(venue_id):
        # Reading venue data from the binary file
        venue_data = read_from_binary_file("venue_data_management.pkl")
        # Iterating through venue data to find the venue with the specified ID
        for venue in venue_data:
            if venue["Venue ID"] == venue_id:
                return venue
        return None

    # Static method to delete venue data by ID from the binary file
    @staticmethod
    def delete_venue_by_id(venue_id):
        # Reading venue data from the binary file
        venue_data = read_from_binary_file("venue_data_management.pkl")
        # Checking if there is no venue data
        if not venue_data:
            print("No venue data found.")
            return
        
        # Creating a list to store updated venue data
        updated_venue_data = []
        # Iterating through venue data to filter out the venue with the specified ID
        for venue in venue_data:
            if isinstance(venue, dict) and "Venue ID" in venue and venue["Venue ID"] != venue_id:
                updated_venue_data.append(venue)

        # Writing updated venue data to the binary file
        with open("venue_data_management.pkl", "wb") as file:
            for venue in updated_venue_data:
                pickle.dump(venue, file)

    # Static method to modify venue data by ID in the binary file
    @staticmethod
    def modify_venue_by_id(venue_id, updated_venue_data):
        # Reading venue data from the binary file
        venue_data = read_from_binary_file("venue_data_management.pkl")
        # Checking if there is no venue data
        if not venue_data:
            print("No venue data found.")
            return
        
        # Creating a list to store updated venue data
        updated_data = []
        # Iterating through venue data to find the venue with the specified ID and update its data
        for venue in venue_data:
            if isinstance(venue, dict) and "Venue ID" in venue and venue["Venue ID"] == venue_id:
                updated_data.append(updated_venue_data)
            else:
                updated_data.append(venue)

        # Writing updated venue data to the binary file
        with open("venue_data_management.pkl", "wb") as file:
            for data in updated_data:
                pickle.dump(data, file)
