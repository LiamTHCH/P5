import requests
import tkinter as tk
from tkinter import messagebox

BASE_URL = "http://127.0.0.1:81/api"

class PrinterGUI:
    def __init__(self, master):
        self.master = master
        master.title("Printer GUI")

        self.printer_id_label = tk.Label(master, text="Printer ID:")
        self.printer_id_label.grid(row=0, column=0, padx=5, pady=5)

        self.printer_id_entry = tk.Entry(master)
        self.printer_id_entry.grid(row=0, column=1, padx=5, pady=5)

        self.status_label = tk.Label(master, text="Status:")
        self.status_label.grid(row=1, column=0, padx=5, pady=5)

        self.status_var = tk.StringVar()
        self.status_var.set("idle")

        # Create a selection box for setting the status
        self.status_options = ["idle", "printing", "error", "waiting_grabber"]
        self.status_option_menu = tk.OptionMenu(master, self.status_var, *self.status_options)
        self.status_option_menu.grid(row=1, column=1, padx=5, pady=5)

        self.get_status_button = tk.Button(master, text="Get Status", command=self.get_status)
        self.get_status_button.grid(row=2, column=0, columnspan=2, pady=5)

        self.set_status_button = tk.Button(master, text="Set New Status", command=self.set_status)
        self.set_status_button.grid(row=1, column=2, columnspan=2, pady=5)

        self.get_position_button = tk.Button(master, text="Get Position", command=self.get_position)
        self.get_position_button.grid(row=4, column=0, columnspan=2, pady=5)

        self.set_position_label = tk.Label(master, text="Set Position (x, y):")
        self.set_position_label.grid(row=5, column=0, padx=5, pady=5)

        self.position_var = tk.StringVar()
        self.position_var.set("0, 0")

        self.position_entry = tk.Entry(master, textvariable=self.position_var)
        self.position_entry.grid(row=5, column=1, padx=5, pady=5)

        self.set_position_button = tk.Button(master, text="Set Position", command=self.set_position)
        self.set_position_button.grid(row=6, column=0, columnspan=2, pady=5)

    def get_status(self):
        printer_id = self.printer_id_entry.get()
        try:
            # Perform a GET request to get the status
            response = requests.get(f"{BASE_URL}/printers/{printer_id}/status")
            response_data = response.json()
            status = response_data.get('status')

            # If the status is received, update the OptionMenu
            if status:
                self.status_var.set(status)
                messagebox.showinfo("Printer Status", f"Printer {printer_id} status: {status}")
        except Exception as e:
            messagebox.showerror("Error", f"Error: {str(e)}")

    def set_status(self):
        printer_id = self.printer_id_entry.get()
        new_status = self.status_var.get()
        try:
            data = {"status": new_status}
            response = requests.post(f"{BASE_URL}/printers/{printer_id}/status", json=data)
            response_data = response.json()
            message = response_data.get('message')
            messagebox.showinfo("Set Status", message)
        except Exception as e:
            messagebox.showerror("Error", f"Error: {str(e)}")

    def get_position(self):
        printer_id = self.printer_id_entry.get()
        try:
            response = requests.get(f"{BASE_URL}/printers/{printer_id}/position")
            response_data = response.json()
            position = response_data.get('position')
            messagebox.showinfo("Printer Position", f"Printer {printer_id} position: {position}")
        except Exception as e:
            messagebox.showerror("Error", f"Error: {str(e)}")

    def set_position(self):
        printer_id = self.printer_id_entry.get()
        new_position = self.position_var.get()
        try:
            data = {"position": list(map(int, new_position.split(',')))}
            response = requests.post(f"{BASE_URL}/printers/{printer_id}/position", json=data)
            response_data = response.json()
            message = response_data.get('message')
            messagebox.showinfo("Set Position", message)
        except Exception as e:
            messagebox.showerror("Error", f"Error: {str(e)}")

if __name__ == '__main__':
    root = tk.Tk()
    app = PrinterGUI(root)
    root.mainloop()
