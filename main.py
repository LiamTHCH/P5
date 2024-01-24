from flask import Flask, jsonify, request



class Printer:
    def __init__(self, printer_id,ip_address,position):
        self.printer_id = printer_id
        self.status = "idle"
        self.ip_address = ip_address
        self.position = (0, 0)  # Initial position as a tuple (x, y)
    def get_status(self):
        return self.status

    def set_status(self, new_status):
        valid_statuses = ["idle", "printing", "error","wating_grabber"]
        if new_status.lower() in valid_statuses:
            self.status = new_status.lower()
        else:
            print("Invalid status. Status should be one of: {}".format(', '.join(valid_statuses)))

    def get_ip_address(self):
        return self.ip_address

    def set_ip_address(self, new_ip_address):
        self.ip_address = new_ip_address

    def get_position(self):
        return self.position

    def set_position(self, new_position):
        self.position = new_position



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






app = Flask(__name__)

@app.route('/')
def index():
    return 'Web App with Python Flask!'


grabbers = {
    1: Grabber(1, "192.168.1.1"),
    # Add more grabbers as needed
}

printers = {
    1: Printer(1, "192.168.1.1",(1,1)),
}


###### APP route for the printer

@app.route('/api/printers/<int:printer_id>/status', methods=['GET'])
def get_printer_status(printer_id):
    if printer_id in printers:
        printer = printers[printer_id]
        return jsonify(status=printer.get_status())
    else:
        return jsonify(message="Printer not found."), 404

# Endpoint to set the status of a specific printer
@app.route('/api/printers/<int:printer_id>/status', methods=['POST'])
def set_printer_status(printer_id):
    if printer_id in printers:
        printer = printers[printer_id]
        data = request.get_json()
        new_status = data.get('status')
        response = printer.set_status(new_status)
        return jsonify(message=response)
    else:
        return jsonify(message="Printer not found."), 404



@app.route('/api/printers/<int:printer_id>/position', methods=['GET'])
def get_printer_position(printer_id):
    if printer_id in printers:
        printer = printers[printer_id]
        return jsonify(position=printer.get_position())
    else:
        return jsonify(message="Printer not found."), 40

###### APP route for the Grabber

@app.route('/api/grabber/<int:grabber_id>/status', methods=['GET'])
def get_grabber_status(grabber_id):
    if grabber_id in grabbers:
        grabber = grabbers[grabber_id]
        return jsonify(status=grabber.get_status())
    else:
        return jsonify(message="Grabber not found."), 404

# Endpoint to set grabber status
@app.route('/api/grabber/<int:grabber_id>/status', methods=['POST'])
def set_grabber_status(grabber_id):
    if grabber_id in grabbers:
        grabber = grabbers[grabber_id]
        data = request.get_json()
        new_status = data.get('status')
        response = grabber.set_status(new_status)
        return jsonify(message=response)
    else:
        return jsonify(message="Grabber not found."), 404

# Endpoint to get grabber IP address
@app.route('/api/grabber/<int:grabber_id>/ip', methods=['GET'])
def get_grabber_ip(grabber_id):
    if grabber_id in grabbers:
        grabber = grabbers[grabber_id]
        return jsonify(ip_address=grabber.get_ip_address())
    else:
        return jsonify(message="Grabber not found."), 404

# Endpoint to set grabber IP address
@app.route('/api/grabber/<int:grabber_id>/ip', methods=['POST'])
def set_grabber_ip(grabber_id):
    if grabber_id in grabbers:
        grabber = grabbers[grabber_id]
        data = request.get_json()
        new_ip_address = data.get('ip_address')
        response = grabber.set_ip_address(new_ip_address)
        return jsonify(message=response)
    else:
        return jsonify(message="Grabber not found."), 404
    
@app.route('/api/grabber/job', methods=['GET'])
def get_printers_with_wating_status():
    waiting_printers = {
        printer_id: {"status": printer_info.get_status()}
        for printer_id, printer_info in printers.items()
        if printer_info.get_status() == "wating_grabber"
    }
    return jsonify(waiting_printers)



app.run(host='0.0.0.0', port=81)