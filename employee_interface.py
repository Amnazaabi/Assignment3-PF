import tkinter as tk
from tkinter import messagebox
from employee import Employee

class EmployeeInterface:
    def __init__(self, root):
        self.root = root
        self.root.title("Employee Management")

        # Set background color of the root window to black
        self.root.configure(bg="#5B180F")
        self.root.geometry("270x280")  # Set the initial window size

        # Define gradient colors
        gradient_color1 = "#F99B99"  # Light blue
        gradient_color2 = "#C4615B"  # Dark blue
        
        button_width = 17

        # Define button style for the add employee window
        button_style = {"padx": 20, "pady": 10, "highlightthickness": 0, "bd": 0, "width": button_width, "bg": "#5B180F", "fg": "black"}

        # Create main menu
        self.create_main_menu(button_style, gradient_color1, gradient_color2)

    def create_main_menu(self, button_style, color1, color2):
        # Main menu buttons
        add_employee_button = tk.Button(self.root, text="Add Employee", command=self.add_employee, **button_style)
        add_employee_button.pack(pady=5)

        display_employee_button = tk.Button(self.root, text="Display Employees", command=self.display_employees, **button_style)
        display_employee_button.pack(pady=5)

        delete_employee_button = tk.Button(self.root, text="Delete Employee", command=self.delete_employee, **button_style)
        delete_employee_button.pack(pady=5)

        modify_employee_button = tk.Button(self.root, text="Modify Employee", command=self.modify_employee, **button_style)
        modify_employee_button.pack(pady=5)

        # Apply gradient background color
        self.apply_gradient(add_employee_button, color1, color2)
        self.apply_gradient(display_employee_button, color1, color2)
        self.apply_gradient(delete_employee_button, color1, color2)
        self.apply_gradient(modify_employee_button, color1, color2)

    def add_employee(self):
        # Open a new window for adding employee
        add_employee_window = tk.Toplevel(self.root)
        add_employee_window.title("Add Employee")
        add_employee_window.geometry("270x550")  # Set geometry for the add employee window

        # Set background color of the add employee window
        add_employee_window.configure(bg="#5B180F")

        button_width = 17

        # Define button style for the add employee window
        button_style = {"padx": 20, "pady": 10, "highlightthickness": 0, "bd": 0, "width": button_width, "bg": "#5B180F", "fg": "black"}

        # Input fields for adding employee
        name_label = tk.Label(add_employee_window, text="Name:", bg="#5B180F", fg="white")
        name_label.pack(pady=5)
        name_entry = tk.Entry(add_employee_window)
        name_entry.pack(pady=5)

        employee_id_label = tk.Label(add_employee_window, text="Employee ID:", bg="#5B180F", fg="white")
        employee_id_label.pack(pady=5)
        employee_id_entry = tk.Entry(add_employee_window)
        employee_id_entry.pack(pady=5)

        department_label = tk.Label(add_employee_window, text="Department:", bg="#5B180F", fg="white")
        department_label.pack(pady=5)
        department_entry = tk.Entry(add_employee_window)
        department_entry.pack(pady=5)

        job_title_label = tk.Label(add_employee_window, text="Job Title:", bg="#5B180F", fg="white")
        job_title_label.pack(pady=5)
        job_title_entry = tk.Entry(add_employee_window)
        job_title_entry.pack(pady=5)

        basic_salary_label = tk.Label(add_employee_window, text="Basic Salary:", bg="#5B180F", fg="white")
        basic_salary_label.pack(pady=5)
        basic_salary_entry = tk.Entry(add_employee_window)
        basic_salary_entry.pack(pady=5)

        age_label = tk.Label(add_employee_window, text="Age:", bg="#5B180F", fg="white")
        age_label.pack(pady=5)
        age_entry = tk.Entry(add_employee_window)
        age_entry.pack(pady=5)

        date_of_birth_label = tk.Label(add_employee_window, text="Date of Birth:", bg="#5B180F", fg="white")
        date_of_birth_label.pack(pady=5)
        date_of_birth_entry = tk.Entry(add_employee_window)
        date_of_birth_entry.pack(pady=5)

        passport_details_label = tk.Label(add_employee_window, text="Passport Details:", bg="#5B180F", fg="white")
        passport_details_label.pack(pady=5)
        passport_details_entry = tk.Entry(add_employee_window)
        passport_details_entry.pack(pady=5)

        # Function to validate Employee ID
        def validate_employee_id():
            employee_id = employee_id_entry.get()
            if not employee_id.isdigit():
                messagebox.showerror("Error", "Employee ID must contain only digits.")
                return False
            return True

        # Function to save employee details with validation
        def save_employee():
            if not all(entry.get() for entry in (name_entry, employee_id_entry, department_entry, job_title_entry, basic_salary_entry, age_entry, date_of_birth_entry, passport_details_entry)):
                messagebox.showerror("Error", "All fields are required.")
                return
            if not validate_employee_id():
                return

            # Save employee details
            self.save_employee_details(name_entry.get(), employee_id_entry.get(), department_entry.get(), job_title_entry.get(), basic_salary_entry.get(), age_entry.get(), date_of_birth_entry.get(), passport_details_entry.get())

        # Save button to add employee with gradient style
        save_button = tk.Button(add_employee_window, text="Save", command=save_employee, **button_style)
        save_button.pack(pady=10)

        # Apply gradient background color to save button
        self.apply_gradient(save_button, "#F99B99", "#C4615B")

    def save_employee(self, name, employee_id, department, job_title, basic_salary, age, date_of_birth, passport_details):
        # Create an Employee object with the provided data
        employee = Employee(name, employee_id, department, job_title, basic_salary, age, date_of_birth, passport_details)

        # Call the save_employee method from Employee class to save the employee data
        employee.save_employee()

        messagebox.showinfo("Success", f"Employee {name} added successfully.")

    def display_employees(self):
            # Open a new window to display employee
            display_employee_window = tk.Toplevel(self.root)
            display_employee_window.title("Display Employee")

            # Set background color of the display employee window
            display_employee_window.configure(bg="#5B180F")
            display_employee_window.geometry("600x600")

            button_width = 17

            # Define button style for the add employee window
            button_style = {"padx": 20, "pady": 10, "highlightthickness": 0, "bd": 0, "width": button_width, "bg": "#5B180F", "fg": "black"}

            label_font = ("Arial", 12)

            # Create a label and entry for employee ID
            id_label = tk.Label(display_employee_window, text="Enter Employee ID:", bg="#5B180F", fg="white", font=label_font)
            id_label.pack(pady=5)
            id_entry = tk.Entry(display_employee_window)
            id_entry.pack(pady=5)

            def display():
                employee_id = id_entry.get()
                employee = Employee.get_employee_by_id(employee_id)
                if employee:
                    # Clear previous data
                    data_text.delete(1.0, tk.END)
                    # Display employee data
                    for key, value in employee.items():
                        data_text.insert(tk.END, f"{key}: {value}\n")
                else:
                    messagebox.showerror("Error", "Employee ID not found.")

            # Text widget to display employee data
            data_text = tk.Text(display_employee_window, bg="white", fg="black", font=label_font)
            data_text.pack(pady=5)

            # Button to display employee data
            display_button = tk.Button(display_employee_window, text="Display", command=display, **button_style)
            display_button.pack(pady=10)

            # Label to show employee data
            data_label = tk.Label(display_employee_window, text="", bg="#5B180F", fg="white", font=label_font)
            data_label.pack(pady=5)

            # Apply gradient background color to display button
            self.apply_gradient(display_button, "#F99B99", "#C4615B")
    
    def delete_employee(self):
        # Open a new window to delete employee
        delete_employee_window = tk.Toplevel(self.root)
        delete_employee_window.title("Delete Employee")

        # Set background color of the delete employee window
        delete_employee_window.configure(bg="#5B180F")

        delete_employee_window.geometry("300x300")

        button_width = 17

        # Define button style for the add employee window
        button_style = {"padx": 20, "pady": 10, "highlightthickness": 0, "bd": 0, "width": button_width, "bg": "#5B180F", "fg": "black"}


        label_font = ("Arial", 12)

        # Create a label and entry for employee ID
        id_label = tk.Label(delete_employee_window, text="Enter Employee ID to Delete:", bg="#5B180F", fg="white", font=label_font)
        id_label.pack(pady=5)
        id_entry = tk.Entry(delete_employee_window)
        id_entry.pack(pady=5)

        # Function to delete employee
        def delete():
            employee_id = id_entry.get()
            if employee_id:
                if messagebox.askyesno("Confirmation", "Are you sure you want to delete this employee?"):
                    Employee.delete_employee_by_id(employee_id)
                    messagebox.showinfo("Success", f"Employee with ID {employee_id} deleted successfully.")
                    delete_employee_window.destroy()
            else:
                messagebox.showerror("Error", "Please enter Employee ID.")

        # Button to delete employee
        delete_button = tk.Button(delete_employee_window, text="Delete", command=delete, **button_style)
        delete_button.pack(pady=10)

        # Apply gradient background color to delete button
        self.apply_gradient(delete_button, "#F99B99", "#C4615B")    

    def modify_employee(self):
        # Open a new window to modify employee
        modify_employee_window = tk.Toplevel(self.root)
        modify_employee_window.title("Modify Employee")

        # Set background color of the modify employee window
        modify_employee_window.configure(bg="#5B180F")
        modify_employee_window.geometry("270x550")  # Set geometry for the modify employee window

        button_width = 17

        # Define button style for the modify employee window
        button_style = {"padx": 20, "pady": 10, "highlightthickness": 0, "bd": 0, "width": button_width, "bg": "#5B180F", "fg": "black"}

        label_font = ("Arial", 12)

        # Create a label and entry for employee ID
        id_label = tk.Label(modify_employee_window, text="Enter Employee ID to Modify:", bg="#5B180F", fg="white", font=label_font)
        id_label.pack(pady=5)
        id_entry = tk.Entry(modify_employee_window)
        id_entry.pack(pady=5)

        # Input fields for modifying employee
        name_label = tk.Label(modify_employee_window, text="Name:", bg="#5B180F", fg="white")
        name_label.pack(pady=5)
        name_entry = tk.Entry(modify_employee_window)
        name_entry.pack(pady=5)

        department_label = tk.Label(modify_employee_window, text="Department:", bg="#5B180F", fg="white")
        department_label.pack(pady=5)
        department_entry = tk.Entry(modify_employee_window)
        department_entry.pack(pady=5)

        job_title_label = tk.Label(modify_employee_window, text="Job Title:", bg="#5B180F", fg="white")
        job_title_label.pack(pady=5)
        job_title_entry = tk.Entry(modify_employee_window)
        job_title_entry.pack(pady=5)

        basic_salary_label = tk.Label(modify_employee_window, text="Basic Salary:", bg="#5B180F", fg="white")
        basic_salary_label.pack(pady=5)
        basic_salary_entry = tk.Entry(modify_employee_window)
        basic_salary_entry.pack(pady=5)

        age_label = tk.Label(modify_employee_window, text="Age:", bg="#5B180F", fg="white")
        age_label.pack(pady=5)
        age_entry = tk.Entry(modify_employee_window)
        age_entry.pack(pady=5)

        date_of_birth_label = tk.Label(modify_employee_window, text="Date of Birth:", bg="#5B180F", fg="white")
        date_of_birth_label.pack(pady=5)
        date_of_birth_entry = tk.Entry(modify_employee_window)
        date_of_birth_entry.pack(pady=5)

        passport_details_label = tk.Label(modify_employee_window, text="Passport Details:", bg="#5B180F", fg="white")
        passport_details_label.pack(pady=5)
        passport_details_entry = tk.Entry(modify_employee_window)
        passport_details_entry.pack(pady=5)

        # Function to modify employee
        def modify():
            employee_id = id_entry.get()
            employee = Employee.get_employee_by_id(employee_id)
            if employee:
                updated_employee = {
                    "Name": name_entry.get(),
                    "Employee ID": employee_id,
                    "Department": department_entry.get(),
                    "Job Title": job_title_entry.get(),
                    "Basic Salary": basic_salary_entry.get(),
                    "Age": age_entry.get(),
                    "Date of Birth": date_of_birth_entry.get(),
                    "Passport Details": passport_details_entry.get()
                }
                Employee.modify_employee_by_id(employee_id, updated_employee)
                messagebox.showinfo("Success", f"Employee with ID {employee_id} modified successfully.")
                modify_employee_window.destroy()
            else:
                messagebox.showerror("Error", "Employee ID not found.")

        # Save button to modify employee with gradient style
        save_button = tk.Button(modify_employee_window, text="Save", command=modify, **button_style)
        save_button.pack(pady=10)

        # Apply gradient background color to save button
        self.apply_gradient(save_button, "#F99B99", "#C4615B")

    def apply_gradient(self, widget, color1, color2):
        # Apply gradient background color to widget
        widget.configure(bg=color1)
        widget.bind("<Enter>", lambda event, widget=widget, color=color2: widget.config(bg=color))
        widget.bind("<Leave>", lambda event, widget=widget, color=color1: widget.config(bg=color))

if __name__ == "__main__":
    root = tk.Tk()
    app = EmployeeInterface(root)
    root.mainloop()
