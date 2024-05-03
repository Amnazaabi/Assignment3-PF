# Importing the pickle module for serialization
import pickle

# Defining a function to write data to a binary file
def write_to_binary_file(data, filename):
    # Opening the binary file in append binary mode
    with open(filename, "ab") as file:
        # Serializing the data and writing it to the file
        pickle.dump(data, file)

# Defining a function to read data from a binary file
def read_from_binary_file(filename):
    # Initializing an empty list to store the read data
    data = []
    # Opening the binary file in read binary mode
    with open(filename, "rb") as file:
        try:
            # Looping until the end of the file is reached
            while True:
                # Deserializing the data and appending it to the list
                item = pickle.load(file)
                data.append(item)
        # Handling the end of file error
        except EOFError:
            pass
    # Returning the read data
    return data
