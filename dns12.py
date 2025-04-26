import socket

# Scenario: You just bought the domain aishasart.com
domain_name = "aishasart.com"

# Find the IP address for the domain
try:
    ip_address = socket.gethostbyname(domain_name)
    print(f"The IP address of {domain_name} is {ip_address}")
except socket.gaierror:
    print(f"Unable to resolve {domain_name}")
