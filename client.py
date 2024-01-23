import requests

# Replace this with the appropriate base URL for your Flask API
BASE_URL = "http://127.0.0.1:81"

# Function to print response content in a formatted way
def print_response(response):
    print(f"Status Code: {response.status_code}")
    print("Response:")
    print(response.json())
    print()

# Example usage:

# Get grabber status
response = requests.get(f"{BASE_URL}/grabber/1/status")
print("Get Grabber Status:")
print_response(response)

# Set grabber status to 'grabbing'
data = {"status": "grabbing"}
response = requests.post(f"{BASE_URL}/grabber/1/status", json=data)
print("Set Grabber Status:")
print_response(response)


response = requests.get(f"{BASE_URL}/grabber/1/status")
print("New Grabber Status:")
print_response(response)

# Get grabber IP address
response = requests.get(f"{BASE_URL}/grabber/1/ip")
print("Get Grabber IP:")
print_response(response)
