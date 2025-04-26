import random

def bootp_request():
    # BOOTP Request
    print("Device A: Requesting IP address from BOOTP server...")
    return "Request sent to BOOTP server"

def bootp_reply():
    # BOOTP Reply (Server assigns IP)
    ip_address = f"192.168.1.{random.randint(2, 100)}"  # Simulate IP assignment
    print(f"BOOTP Server: Replying with IP address {ip_address}")
    return ip_address

# Simulate BOOTP process
print(bootp_request())
assigned_ip = bootp_reply()
print(f"Device A: Assigned IP address is {assigned_ip}")
