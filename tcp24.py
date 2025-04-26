import time

def tcp_connection():
    print("Establishing TCP connection...")
    time.sleep(1)  # Simulating connection delay
    print("Connection established.")

def send_data(data):
    print(f"Sending data: {data}")
    time.sleep(1)  # Simulating data transfer
    print("Data sent successfully.")

def receive_acknowledgment():
    print("Waiting for acknowledgment...")
    time.sleep(1)  # Simulating acknowledgment delay
    print("Acknowledgment received.")

# Simulate TCP process
tcp_connection()
send_data("Hello, Device B!")
receive_acknowledgment()
