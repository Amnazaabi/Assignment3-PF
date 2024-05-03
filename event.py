# Importing functions for writing to and reading from binary files
from binary_files_method import write_to_binary_file, read_from_binary_file
# Importing the pickle module for serialization
import pickle

# Create a class called Event
class Event:
    # Create the constructor method for the class
    def __init__(self, event_id, event_type, theme, date, time, duration, venue_address, client_id, guest_list, catering_company, cleaning_company, decorations_company, entertainment_company, furniture_company, invoice):
        # Initialize instance variables with provided data
        self.event_id = event_id
        self.event_type = event_type
        self.theme = theme
        self.date = date
        self.time = time
        self.duration = duration
        self.venue_address = venue_address
        self.client_id = client_id
        self.guest_list = guest_list
        self.catering_company = catering_company
        self.cleaning_company = cleaning_company
        self.decorations_company = decorations_company
        self.entertainment_company = entertainment_company
        self.furniture_company = furniture_company
        self.invoice = invoice

    # Create a method to save event data to a binary file
    def save_event(self):
        # Create a dictionary to represent the event data
        event_data = {
            "Event ID": self.event_id,
            "Event Type": self.event_type,
            "Theme": self.theme,
            "Date": self.date,
            "Time": self.time,
            "Duration": self.duration,
            "Venue Address": self.venue_address,
            "Client ID": self.client_id,
            "Guest List": self.guest_list,
            "Catering Company": self.catering_company,
            "Cleaning Company": self.cleaning_company,
            "Decorations Company": self.decorations_company,
            "Entertainment Company": self.entertainment_company,
            "Furniture Company": self.furniture_company,
            "Invoice": self.invoice
        }
        # Write event data to a binary file
        write_to_binary_file(event_data, "event_data_management.pkl")

    # Create a static method to get event data by ID from a binary file
    @staticmethod
    def get_event_by_id(event_id):
        # Read event data from the binary file
        event_data = read_from_binary_file("event_data_management.pkl")
        # Iterate through event data
        for event in event_data:
            # Check if event ID matches the provided ID
            if event["Event ID"] == event_id:
                return event
        return None

    # Create a static method to delete event data by ID from a binary file
    @staticmethod
    def delete_event_by_id(event_id):
        # Read event data from the binary file
        event_data = read_from_binary_file("event_data_management.pkl")
        # Check if event data exists
        if not event_data:
            print("No event data found.")
            return
        # Create an updated list of event data excluding the specified event ID
        updated_event_data = []
        for event in event_data:
            if isinstance(event, dict) and "Event ID" in event and event["Event ID"] != event_id:
                updated_event_data.append(event)
        # Write the updated event data to the binary file
        with open("event_data_management.pkl", "wb") as file:
            for event in updated_event_data:
                pickle.dump(event, file)

    # Create a static method to modify event data by ID in a binary file
    @staticmethod
    def modify_event_by_id(event_id, updated_event_data):
        # Read event data from the binary file
        event_data = read_from_binary_file("event_data_management.pkl")
        # Check if event data exists
        if not event_data:
            print("No event data found.")
            return
        # Create an updated list of event data with the specified event ID modified
        updated_data = []
        for event in event_data:
            if isinstance(event, dict) and "Event ID" in event and event["Event ID"] == event_id:
                updated_data.append(updated_event_data)
            else:
                updated_data.append(event)
        # Write the updated event data to the binary file
        with open("event_data_management.pkl", "wb") as file:
            for data in updated_data:
                pickle.dump(data, file)
