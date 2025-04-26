import requests

def application_layer():
    print("Application Layer: Making an HTTP GET request...")
    response = requests.get('https://www.example.com')
    print(f"Response Status Code: {response.status_code}")
    print(f"Response Content: {response.text[:100]}...")

application_layer()