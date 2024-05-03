# Importing the write_to_binary_file and read_from_binary_file functions from the binary_files_method module
from binary_files_method import write_to_binary_file, read_from_binary_file
# Importing the pickle module
import pickle

# Create a class called Employee
class Employee:
    # Create the constructor method for the class
    def __init__(self, name, employee_id, department, job_title, basic_salary, age, date_of_birth, passport_details):
        # Initialize attributes for employee data
        self.name = name
        self.employee_id = employee_id
        self.department = department
        self.job_title = job_title
        self.basic_salary = basic_salary
        self.age = age
        self.date_of_birth = date_of_birth
        self.passport_details = passport_details

    # Create a method to save employee data to a binary file
    def save_employee(self):
        # Create a dictionary containing employee data
        employee_data = {
            "Name": self.name,
            "Employee ID": self.employee_id,
            "Department": self.department,
            "Job Title": self.job_title,
            "Basic Salary": self.basic_salary,
            "Age": self.age,
            "Date of Birth": self.date_of_birth,
            "Passport Details": self.passport_details
        }

        # Call the write_to_binary_file function to write employee data to a binary file
        write_to_binary_file(employee_data, "employee_data_management.pkl")

    # Create a static method to get employee data by ID from the binary file
    @staticmethod
    def get_employee_by_id(employee_id):
        # Read employee data from the binary file
        employee_data = read_from_binary_file("employee_data_management.pkl")
        # Iterate through employee data
        for employee in employee_data:
            # Check if the employee ID matches the specified ID
            if employee["Employee ID"] == employee_id:
                return employee
        return None
    
    # Create a static method to delete employee data by ID from the binary file
    @staticmethod
    def delete_employee_by_id(employee_id):
        # Read employee data from the binary file
        employee_data = read_from_binary_file("employee_data_management.pkl")
        # Check if there is no employee data
        if not employee_data:
            print("No employee data found.")
            return
        
        # Create an empty list to store updated employee data
        updated_employee_data = []
        # Iterate through employee data
        for employee in employee_data:
            # Check if the employee is a dictionary and contains "Employee ID", and if the ID does not match the specified ID
            if isinstance(employee, dict) and "Employee ID" in employee and employee["Employee ID"] != employee_id:
                # Append the employee data to the updated list
                updated_employee_data.append(employee)

        # Open the binary file in write mode
        with open("employee_data_management.pkl", "wb") as file:
            # Iterate through updated employee data and write it to the file
            for employee in updated_employee_data:
                pickle.dump(employee, file)

    # Create a static method to modify employee data by ID in the binary file
    @staticmethod
    def modify_employee_by_id(employee_id, updated_employee_data):
        # Read employee data from the binary file
        employee_data = read_from_binary_file("employee_data_management.pkl")
        # Check if there is no employee data
        if not employee_data:
            print("No employee data found.")
            return
        
        # Create an empty list to store updated data
        updated_data = []
        # Iterate through employee data
        for employee in employee_data:
            # Check if the employee is a dictionary, contains "Employee ID", and if the ID matches the specified ID
            if isinstance(employee, dict) and "Employee ID" in employee and employee["Employee ID"] == employee_id:
                # Append the updated employee data to the updated list
                updated_data.append(updated_employee_data)
            else:
                # Append the original employee data to the updated list
                updated_data.append(employee)

        # Open the binary file in write mode
        with open("employee_data_management.pkl", "wb") as file:
            # Iterate through updated data and write it to the file
            for data in updated_data:
                pickle.dump(data, file)
