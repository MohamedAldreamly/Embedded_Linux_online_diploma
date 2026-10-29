
import socket

# Create a UDP socket
# AF_INET: Use IPv4 addresses
# SOCK_DGRAM: Use UDP protocol
server_socket = socket.socket(
    socket.AF_INET,
    socket.SOCK_DGRAM
)

# Define the server IP address and port
# localhost: This computer (127.0.0.1)
# 12345: Port number
server_address = ('localhost', 12345)

# Bind the socket to the IP address and port
server_socket.bind(server_address)

print("UDP server up and listening")

# Keep the server running
while True:

    # Wait to receive data from a client
    # 1024: Maximum number of bytes to receive
    # recvfrom() returns data and client address
    message, client_address = server_socket.recvfrom(1024)

    # Convert bytes into a string and display it
    print(f"Received message from {client_address}: {message.decode()}")

    # Prepare a response
    response = "Message received"

    # Encode the response and send it to the client
    server_socket.sendto(response.encode(), client_address)


