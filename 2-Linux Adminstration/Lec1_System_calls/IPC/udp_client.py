
import socket

# Create a UDP client socket
client_socket = socket.socket(
    socket.AF_INET,
    socket.SOCK_DGRAM
)

# Server IP and port
server_address = ('localhost', 12345)

# Prepare the message
message = "Hello Server"

# Send the message to the server
client_socket.sendto(message.encode(), server_address)

# Set a timeout to avoid waiting forever
client_socket.settimeout(5)

try:
    # Receive the server response
    response, address = client_socket.recvfrom(1024)

    # Display the response
    print("Server response:", response.decode())

except socket.timeout:
    print("No response received from server")

finally:
    # Close the client socket
    client_socket.close()
