# import socket

# HOST = '127.0.0.1'  
# PORT = 8000        

# s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# server_address = (HOST, PORT)
# print('connecting to %s port ' + str(server_address))
# s.connect(server_address)

# try:
#     while True:
#         print(".\n")
#         msg = input('Client: ')
#         s.sendall(bytes(msg, "utf8"))

#         if msg == "quit":
#             break

#         data = s.recv(1024)
#         print('Server: ', data.decode("utf8"))
# finally:
#     s.close()
#     print("sv close")

import socket
import threading

# Hàm nhận tin nhắn từ server
def receive_messages(client_socket):
    while True:
        try:
            message = client_socket.recv(1024).decode('utf-8')
            if message:
                print(f"[SERVER] {message}")
            else:
                break
        except:
            print("An error occurred!")
            break

# Thiết lập client
def start_client(host='127.0.0.1', port=12345):
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect((host, port))

    # Bắt đầu luồng nhận tin nhắn
    thread = threading.Thread(target=receive_messages, args=(client,))
    thread.start()

    while True:
        message = input("Enter message: ")
        if message.lower() == 'exit':
            break
        client.send(message.encode('utf-8'))

    client.close()

if __name__ == "__main__":
    start_client()