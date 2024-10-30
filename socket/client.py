import socket

socket_client = socket.socket()

name = input('Your name, please:')
socket_client.connect(('127.0.0.1', 2000))
socket_client.send(name.encode())
socket_name = socket_client.recv(1024)
server_name = socket_name.decode()
print(server_name, "has joined")

while True:
    message = (socket_client.recv(1024)).decode()
    print(server_name, ":", message)
    message = input("Me: ")
    socket_client.send(message.encode())