import socket
import threading

def receive_messages(client_socket):
    while True:
        try:
            message = ""
            message = client_socket.recv(1024).decode('utf-8')
            if message != "":
                print(f"{message}")
        except:
            print("Lost connection")
            break

def send_messages(client_socket, name):
    while True:
        message = input()
        client_socket.send(f"{name}: {message}".encode('utf-8'))

def start_client(host='127.0.0.1', port=5555):
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    name = input("Your name, please: ")
    client_socket.connect((host, port))
    
    thread_receive = threading.Thread(target=receive_messages, args=(client_socket,))
    thread_receive.start()
    
    thread_send = threading.Thread(target=send_messages, args=(client_socket, name,))
    thread_send.start()

start_client()