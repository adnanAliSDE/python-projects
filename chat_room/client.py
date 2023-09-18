import socket
import threading


def receive_messages(client_socket):
    while True:
        data = client_socket.recv(1024)
        print(data.decode('utf-8'))


def send_messages(client_socket, username):
    while True:
        message = input()
        client_socket.send(message.encode('utf-8'))


# Create a socket for the client
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_ip = input('Enter the server IP: ')
client.connect((server_ip, 9090))

# Ask for and send the username
username = input("Enter your username: ")
client.send(username.encode('utf-8'))

# Start threads for receiving and sending messages
receive_thread = threading.Thread(target=receive_messages, args=(client,))
send_thread = threading.Thread(target=send_messages, args=(client, username))

receive_thread.start()
send_thread.start()
