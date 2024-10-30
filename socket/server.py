import socket
import threading

def Accessing():
    while True:
        client_socket, address = server.accept()
        clientStr = (client_socket.recv(1024)).decode('utf-8')
        print(f"Client {clientStr} has joined party!")
        # это все еще должно нахоиться в другом месте
        client_socket.send(name.encode())
        message = input("Me: ")
        client_socket.send(message.encode())
        message = client_socket.recv(1024)
        message = message.decode()
        print(clientStr, ":", message)
        
# server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# server_socket.bind('127.0.0.1', 2000)

# буквально тоже самое только через заранее определенный метод
server = socket.create_server(('127.0.0.1', 2000))
# устанавливаем слушатель, который может иметь в очереди не более 4 клиентов
server.listen(4)
print("It starts")
name = input("Your name, please: ")
while True:
    thread = threading.Thread(target=Accessing(), deamon=True)
    thread.start()
    thread.join()
    


    