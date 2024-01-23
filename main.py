from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return 'Web App with Python Flask!'

app.run(host='0.0.0.0', port=81)



class Printer:
    def __init__(self, printer_id):
        self.printer_id = printer_id
        self.status = "idle"
        self.ip_address = ip_address
    def get_status(self):
        return self.status

    def set_status(self, new_status):
        valid_statuses = ["idle", "printing", "error"]
        if new_status.lower() in valid_statuses:
            self.status = new_status.lower()
        else:
            print("Invalid status. Status should be one of: {}".format(', '.join(valid_statuses)))

    def get_ip_address(self):
        return self.ip_address

    def set_ip_address(self, new_ip_address):
        self.ip_address = new_ip_address

class Grabber:
    def __init__(self, grabber_id, ip_address):
        self.grabber_id = grabber_id
        self.status = "idle"
        self.ip_address = ip_address

    def get_status(self):
        return self.status

    def set_status(self, new_status):
        valid_statuses = ["idle", "grabbing", "error", "waiting"]
        if new_status.lower() in valid_statuses:
            self.status = new_status.lower()
        else:
            print("Invalid status. Status should be one of: {}".format(', '.join(valid_statuses)))

    def get_ip_address(self):
        return self.ip_address

    def set_ip_address(self, new_ip_address):
        self.ip_address = new_ip_address