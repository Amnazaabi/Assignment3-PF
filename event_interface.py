import tkinter as tk
from tkinter import messagebox
from event import Event

class EventInterface:
    def __init__(self, root):
        self.root = root
        self.root.title("Event Management")

        # Set background color of the root window to black
        self.root.configure(bg="#5B180F")
        self.root.geometry("350x250")

        # Define gradient colors
        gradient_color1 = "#F99B99"  # Light blue
        gradient_color2 = "#C4615B"  # Dark blue
        
        button_width = 17

        # Define button style
        button_style = {"padx": 20, "pady": 10, "highlightthickness": 0, "bd": 0, "width": button_width, "bg": "#5B180F", "fg": "black"}
        
        # Create main menu
        self.create_main_menu(button_style, gradient_color1, gradient_color2)

    def create_main_menu(self, button_style, color1, color2):
        # Main menu buttons
        add_event_button = tk.Button(self.root, text="Add Event", command=self.add_event, **button_style)
        add_event_button.pack(pady=5)

        display_event_button = tk.Button(self.root, text="Display Events", command=self.display_events, **button_style)
        display_event_button.pack(pady=5)

        delete_event_button = tk.Button(self.root, text="Delete Event", command=self.delete_event, **button_style)
        delete_event_button.pack(pady=5)

        modify_event_button = tk.Button(self.root, text="Modify Event", command=self.modify_event, **button_style)
        modify_event_button.pack(pady=5)

        # Apply gradient background color
        self.apply_gradient(add_event_button, color1, color2)
        self.apply_gradient(display_event_button, color1, color2)
        self.apply_gradient(delete_event_button, color1, color2)
        self.apply_gradient(modify_event_button, color1, color2)

    def add_event(self):
        add_event_window = tk.Toplevel(self.root)
        add_event_window.title("Add Event")
        add_event_window.geometry("500x600")  # Increased width
        add_event_window.configure(bg="#5B180F")

        button_width = 17
        button_style = {"padx": 20, "pady": 10, "highlightthickness": 0, "bd": 0, "width": button_width, "bg": "#5B180F", "fg": "black"}

        label_font = ("Arial", 12)

        # Divide the fields into three columns
        column1_x = 20
        column2_x = 200  # Adjust as needed
        column3_x = 380  # Adjust as needed

        id_label = tk.Label(add_event_window, text="Event ID:", bg="#5B180F", fg="white", font=label_font)
        id_label.place(x=column1_x, y=20)
        id_entry = tk.Entry(add_event_window)
        id_entry.place(x=column2_x, y=20)

        event_type_label = tk.Label(add_event_window, text="Event Type:", bg="#5B180F", fg="white", font=label_font)
        event_type_label.place(x=column1_x, y=60)
        event_type_entry = tk.Entry(add_event_window)
        event_type_entry.place(x=column2_x, y=60)

        theme_label = tk.Label(add_event_window, text="Theme:", bg="#5B180F", fg="white", font=label_font)
        theme_label.place(x=column1_x, y=100)
        theme_entry = tk.Entry(add_event_window)
        theme_entry.place(x=column2_x, y=100)

        date_label = tk.Label(add_event_window, text="Date:", bg="#5B180F", fg="white", font=label_font)
        date_label.place(x=column1_x, y=140)
        date_entry = tk.Entry(add_event_window)
        date_entry.place(x=column2_x, y=140)

        time_label = tk.Label(add_event_window, text="Time:", bg="#5B180F", fg="white", font=label_font)
        time_label.place(x=column1_x, y=180)
        time_entry = tk.Entry(add_event_window)
        time_entry.place(x=column2_x, y=180)

        duration_label = tk.Label(add_event_window, text="Duration:", bg="#5B180F", fg="white", font=label_font)
        duration_label.place(x=column1_x, y=220)
        duration_entry = tk.Entry(add_event_window)
        duration_entry.place(x=column2_x, y=220)

        venue_address_label = tk.Label(add_event_window, text="Venue Address:", bg="#5B180F", fg="white", font=label_font)
        venue_address_label.place(x=column1_x, y=260)
        venue_address_entry = tk.Entry(add_event_window)
        venue_address_entry.place(x=column2_x, y=260)

        client_id_label = tk.Label(add_event_window, text="Client ID:", bg="#5B180F", fg="white", font=label_font)
        client_id_label.place(x=column1_x, y=300)
        client_id_entry = tk.Entry(add_event_window)
        client_id_entry.place(x=column2_x, y=300)

        guest_list_label = tk.Label(add_event_window, text="Guest List:", bg="#5B180F", fg="white", font=label_font)
        guest_list_label.place(x=column1_x, y=340)
        guest_list_entry = tk.Entry(add_event_window)
        guest_list_entry.place(x=column2_x, y=340)

        catering_company_label = tk.Label(add_event_window, text="Catering Company:", bg="#5B180F", fg="white", font=label_font)
        catering_company_label.place(x=column1_x, y=380)
        catering_company_entry = tk.Entry(add_event_window)
        catering_company_entry.place(x=column2_x, y=380)

        cleaning_company_label = tk.Label(add_event_window, text="Cleaning Company:", bg="#5B180F", fg="white", font=label_font)
        cleaning_company_label.place(x=column1_x, y=420)
        cleaning_company_entry = tk.Entry(add_event_window)
        cleaning_company_entry.place(x=column2_x, y=420)

        decorations_company_label = tk.Label(add_event_window, text="Decorations Company:", bg="#5B180F", fg="white", font=label_font)
        decorations_company_label.place(x=column1_x, y=460)
        decorations_company_entry = tk.Entry(add_event_window)
        decorations_company_entry.place(x=column2_x, y=460)

        entertainment_company_label = tk.Label(add_event_window, text="Entertainment Company:", bg="#5B180F", fg="white", font=label_font)
        entertainment_company_label.place(x=column1_x, y=500)
        entertainment_company_entry = tk.Entry(add_event_window)
        entertainment_company_entry.place(x=column2_x, y=500)

        furniture_company_label = tk.Label(add_event_window, text="Furniture Company:", bg="#5B180F", fg="white", font=label_font)
        furniture_company_label.place(x=column1_x, y=540)
        furniture_company_entry = tk.Entry(add_event_window)
        furniture_company_entry.place(x=column2_x, y=540)

        invoice_label = tk.Label(add_event_window, text="Invoice:", bg="#5B180F", fg="white", font=label_font)
        invoice_label.place(x=column1_x, y=580)
        invoice_entry = tk.Entry(add_event_window)
        invoice_entry.place(x=column2_x, y=580)

        # Column 3
        # Additional fields can be placed in this column

        def save_event():
            event_id = id_entry.get()
            event_type = event_type_entry.get()
            theme = theme_entry.get()
            date = date_entry.get()
            time = time_entry.get()
            duration = duration_entry.get()
            venue_address = venue_address_entry.get()
            client_id = client_id_entry.get()
            guest_list = guest_list_entry.get()
            catering_company = catering_company_entry.get()
            cleaning_company = cleaning_company_entry.get()
            decorations_company = decorations_company_entry.get()
            entertainment_company = entertainment_company_entry.get()
            furniture_company = furniture_company_entry.get()
            invoice = invoice_entry.get()

            # Create an event object and save it
            event = Event(event_id, event_type, theme, date, time, duration, venue_address, client_id, guest_list, catering_company, cleaning_company, decorations_company, entertainment_company, furniture_company, invoice)
            event.save_event()

            # Show success message and close the window
            messagebox.showinfo("Success", f"Event {event_id} added successfully.")
            add_event_window.destroy()

        save_button = tk.Button(add_event_window, text="Save", command=save_event, **button_style)
        save_button.place(x=180, y=650) 

        self.apply_gradient(save_button, "#F99B99", "#C4615B")

    def display_events(self):
        display_events_window = tk.Toplevel(self.root)
        display_events_window.title("Display Events")
        display_events_window.geometry("600x600")
        display_events_window.configure(bg="#5B180F")

        button_width = 17
        button_style = {"padx": 20, "pady": 10, "highlightthickness": 0, "bd": 0, "width": button_width, "bg": "#5B180F", "fg": "black"}

        label_font = ("Arial", 12)

        id_label = tk.Label(display_events_window, text="Enter Event ID:", bg="#5B180F", fg="white", font=label_font)
        id_label.pack(pady=5)
        id_entry = tk.Entry(display_events_window)
        id_entry.pack(pady=5)

        def display():
            event_id = id_entry.get()
            event = Event.get_event_by_id(event_id)
            if event:
                data_text.delete(1.0, tk.END)
                for key, value in event.items():
                    data_text.insert(tk.END, f"{key}: {value}\n")
            else:
                messagebox.showerror("Error", "Event ID not found.")

        data_text = tk.Text(display_events_window, bg="white", fg="black", font=label_font)
        data_text.pack(pady=5)

        display_button = tk.Button(display_events_window, text="Display", command=display, **button_style)
        display_button.pack(pady=10)

        data_label = tk.Label(display_events_window, text="", bg="#5B180F", fg="white", font=label_font)
        data_label.pack(pady=5)

        self.apply_gradient(display_button, "#F99B99", "#C4615B")

    def delete_event(self):
        delete_event_window = tk.Toplevel(self.root)
        delete_event_window.title("Delete Event")
        delete_event_window.geometry("300x300")
        delete_event_window.configure(bg="#5B180F")

        button_width = 17
        button_style = {"padx": 20, "pady": 10, "highlightthickness": 0, "bd": 0, "width": button_width, "bg": "#5B180F", "fg": "black"}

        label_font = ("Arial", 12)

        id_label = tk.Label(delete_event_window, text="Enter Event ID to Delete:", bg="#5B180F", fg="white", font=label_font)
        id_label.pack(pady=5)
        id_entry = tk.Entry(delete_event_window)
        id_entry.pack(pady=5)

        def delete():
            event_id = id_entry.get()
            if event_id:
                if messagebox.askyesno("Confirmation", "Are you sure you want to delete this event?"):
                    Event.delete_event_by_id(event_id)
                    messagebox.showinfo("Success", f"Event with ID {event_id} deleted successfully.")
                    delete_event_window.destroy()
            else:
                messagebox.showerror("Error", "Please enter Event ID.")

        delete_button = tk.Button(delete_event_window, text="Delete", command=delete, **button_style)
        delete_button.pack(pady=10)

        self.apply_gradient(delete_button, "#F99B99", "#C4615B")

    def modify_event(self):
        modify_event_window = tk.Toplevel(self.root)
        modify_event_window.title("Modify Event")
        modify_event_window.geometry("500x700")  # Increased width
        modify_event_window.configure(bg="#5B180F")

        button_width = 17
        button_style = {"padx": 20, "pady": 10, "highlightthickness": 0, "bd": 0, "width": button_width, "bg": "#5B180F", "fg": "black"}

        label_font = ("Arial", 12)

        # Divide the fields into three columns
        column1_x = 20
        column2_x = 200  # Adjust as needed
        column3_x = 380  # Adjust as needed

        id_label = tk.Label(modify_event_window, text="Enter Event ID to Modify:", bg="#5B180F", fg="white", font=label_font)
        id_label.place(x=column1_x, y=20)
        id_entry = tk.Entry(modify_event_window)
        id_entry.place(x=column2_x, y=20)

        event_type_label = tk.Label(modify_event_window, text="Event Type:", bg="#5B180F", fg="white", font=label_font)
        event_type_label.place(x=column1_x, y=60)
        event_type_entry = tk.Entry(modify_event_window)
        event_type_entry.place(x=column2_x, y=60)

        theme_label = tk.Label(modify_event_window, text="Theme:", bg="#5B180F", fg="white", font=label_font)
        theme_label.place(x=column1_x, y=100)
        theme_entry = tk.Entry(modify_event_window)
        theme_entry.place(x=column2_x, y=100)

        date_label = tk.Label(modify_event_window, text="Date:", bg="#5B180F", fg="white", font=label_font)
        date_label.place(x=column1_x, y=140)
        date_entry = tk.Entry(modify_event_window)
        date_entry.place(x=column2_x, y=140)

        time_label = tk.Label(modify_event_window, text="Time:", bg="#5B180F", fg="white", font=label_font)
        time_label.place(x=column1_x, y=180)
        time_entry = tk.Entry(modify_event_window)
        time_entry.place(x=column2_x, y=180)

        duration_label = tk.Label(modify_event_window, text="Duration:", bg="#5B180F", fg="white", font=label_font)
        duration_label.place(x=column1_x, y=220)
        duration_entry = tk.Entry(modify_event_window)
        duration_entry.place(x=column2_x, y=220)

        venue_address_label = tk.Label(modify_event_window, text="Venue Address:", bg="#5B180F", fg="white", font=label_font)
        venue_address_label.place(x=column1_x, y=260)
        venue_address_entry = tk.Entry(modify_event_window)
        venue_address_entry.place(x=column2_x, y=260)

        client_id_label = tk.Label(modify_event_window, text="Client ID:", bg="#5B180F", fg="white", font=label_font)
        client_id_label.place(x=column1_x, y=300)
        client_id_entry = tk.Entry(modify_event_window)
        client_id_entry.place(x=column2_x, y=300)

        guest_list_label = tk.Label(modify_event_window, text="Guest List:", bg="#5B180F", fg="white", font=label_font)
        guest_list_label.place(x=column1_x, y=340)
        guest_list_entry = tk.Entry(modify_event_window)
        guest_list_entry.place(x=column2_x, y=340)

        catering_company_label = tk.Label(modify_event_window, text="Catering Company:", bg="#5B180F", fg="white", font=label_font)
        catering_company_label.place(x=column1_x, y=380)
        catering_company_entry = tk.Entry(modify_event_window)
        catering_company_entry.place(x=column2_x, y=380)

        cleaning_company_label = tk.Label(modify_event_window, text="Cleaning Company:", bg="#5B180F", fg="white", font=label_font)
        cleaning_company_label.place(x=column1_x, y=420)
        cleaning_company_entry = tk.Entry(modify_event_window)
        cleaning_company_entry.place(x=column2_x, y=420)

        decorations_company_label = tk.Label(modify_event_window, text="Decorations Company:", bg="#5B180F", fg="white", font=label_font)
        decorations_company_label.place(x=column1_x, y=460)
        decorations_company_entry = tk.Entry(modify_event_window)
        decorations_company_entry.place(x=column2_x, y=460)

        entertainment_company_label = tk.Label(modify_event_window, text="Entertainment Company:", bg="#5B180F", fg="white", font=label_font)
        entertainment_company_label.place(x=column1_x, y=500)
        entertainment_company_entry = tk.Entry(modify_event_window)
        entertainment_company_entry.place(x=column2_x, y=500)

        furniture_company_label = tk.Label(modify_event_window, text="Furniture Company:", bg="#5B180F", fg="white", font=label_font)
        furniture_company_label.place(x=column1_x, y=540)
        furniture_company_entry = tk.Entry(modify_event_window)
        furniture_company_entry.place(x=column2_x, y=540)

        invoice_label = tk.Label(modify_event_window, text="Invoice:", bg="#5B180F", fg="white", font=label_font)
        invoice_label.place(x=column1_x, y=580)
        invoice_entry = tk.Entry(modify_event_window)
        invoice_entry.place(x=column2_x, y=580)

        def modify():
            event_id = id_entry.get()
            event = Event.get_event_by_id(event_id)
            if event:
                updated_event = {
                    "Event ID": event_id,
                    "Event Type": event_type_entry.get(),
                    "Theme": theme_entry.get(),
                    "Date": date_entry.get(),
                    "Time": time_entry.get(),
                    "Duration": duration_entry.get(),
                    "Venue Address": venue_address_entry.get(),
                    "Client ID": client_id_entry.get(),
                    "Guest List": guest_list_entry.get(),
                    "Catering Company": catering_company_entry.get(),
                    "Cleaning Company": cleaning_company_entry.get(),
                    "Decorations Company": decorations_company_entry.get(),
                    "Entertainment Company": entertainment_company_entry.get(),
                    "Furniture Company": furniture_company_entry.get(),
                    "Invoice": invoice_entry.get()
                }
                Event.modify_event_by_id(event_id, updated_event)
                messagebox.showinfo("Success", f"Event with ID {event_id} modified successfully.")
                modify_event_window.destroy()
            else:
                messagebox.showerror("Error", "Event ID not found.")

        save_button = tk.Button(modify_event_window, text="Save", command=modify, **button_style)
        save_button.place(x=200, y=630)  # Adjusted position

        self.apply_gradient(save_button, "#F99B99", "#C4615B")


    def apply_gradient(self, widget, color1, color2):
        # Apply gradient background color to widget
        widget.configure(bg=color1)
        widget.bind("<Enter>", lambda event, widget=widget, color=color2: widget.config(bg=color))
        widget.bind("<Leave>", lambda event, widget=widget, color=color1: widget.config(bg=color))

if __name__ == "__main__":
    root = tk.Tk()
    app = EventInterface(root)
    root.mainloop()
