import requests
import tkinter as tk
from tkinter import messagebox

BASE_URL = "http://127.0.0.1:81/api"

class grabberGUI:
    def __init__(self, master):
        self.master = master
        master.title("grabber GUI")

        self.grabber_id_label = tk.Label(master, text="grabber ID:")
        self.grabber_id_label.grid(row=0, column=0, padx=5, pady=5)

        self.grabber_id_entry = tk.Entry(master)
        self.grabber_id_entry.grid(row=0, column=1, padx=5, pady=5)

        self.status_label = tk.Label(master, text="Status:")
        self.status_label.grid(row=1, column=0, padx=5, pady=5)

        self.status_var = tk.StringVar()
        self.status_var.set("idle")

        # Create a selection box for setting the status
        self.status_options = ["idle", "grabbing", "error", "waiting"]
        self.status_option_menu = tk.OptionMenu(master, self.status_var, *self.status_options)
        self.status_option_menu.grid(row=1, column=1, padx=5, pady=5)

        self.get_status_button = tk.Button(master, text="Get Status", command=self.get_status)
        self.get_status_button.grid(row=2, column=0, columnspan=2, pady=5)

        self.set_status_button = tk.Button(master, text="Set New Status", command=self.set_status)
        self.set_status_button.grid(row=1, column=2, columnspan=2, pady=5)



    def get_status(self):
        grabber_id = self.grabber_id_entry.get()
        try:
            # Perform a GET request to get the status
            response = requests.get(f"{BASE_URL}/grabber/{grabber_id}/status")
            response_data = response.json()
            status = response_data.get('status')

            # If the status is received, update the OptionMenu
            if status:
                self.status_var.set(status)
                messagebox.showinfo("grabber Status", f"grabber {grabber_id} status: {status}")
        except Exception as e:
            messagebox.showerror("Error", f"Error: {str(e)}")

    def set_status(self):
        grabber_id = self.grabber_id_entry.get()
        new_status = self.status_var.get()
        try:
            data = {"status": new_status}
            response = requests.post(f"{BASE_URL}/grabber/{grabber_id}/status", json=data)
            response_data = response.json()
            message = response_data.get('message')
            messagebox.showinfo("Set Status", message)
        except Exception as e:
            messagebox.showerror("Error", f"Error: {str(e)}")

   

if __name__ == '__main__':
    root = tk.Tk()
    app = grabberGUI(root)
    root.mainloop()
