def broadcast_message(message):
    print(f"Broadcasting message: {message}")
    devices = ['Device 1', 'Device 2', 'Device 3']
    for device in devices:
        print(f"Message received by {device}")

# Simulate broadcasting
broadcast_message("Hello, Network!")
