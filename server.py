# import socket

# HOST = '127.0.0.1'  
# PORT = 8000        

# s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# s.bind((HOST, PORT))
# s.listen(200)

# while True:
#     client, addr = s.accept()
    
#     try:
#         print('Connected by', addr)
#         while True:
#             print("-\n")
#             data = client.recv(1024)
#             str_data = data.decode("utf8")
#             if str_data == "quit":
#                 break
#             """if not data:
#                 break
#             """
#             print("Client: " + str_data)

#             msg = input("Server: ")
                
#     finally:
#         client.close()
#         print("sv close")
# s.close()


import socket
import threading

# Hàm xử lý kết nối từ client
def handle_client(client_socket, addr):
    print(f"[NEW CONNECTION] {addr} connected.")
    
    while True:
        try:
            # Nhận tin nhắn từ client
            message = client_socket.recv(1024).decode('utf-8')
            if not message:
                break
            
            print(f"[MESSAGE FROM {addr}] {message}")
            
            # Gửi lại tin nhắn đến client
            client_socket.send(f"Server received: {message}".encode('utf-8'))
        
        except ConnectionResetError:
            break

    print(f"[DISCONNECT] {addr} disconnected.")
    client_socket.close()

# Thiết lập server
def start_server(host='0.0.0.0', port=12345):
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind((host, port))
    server.listen(5)
    print(f"[LISTENING] Server is listening on {host}:{port}")

    while True:
        client_socket, addr = server.accept()
        client_handler = threading.Thread(target=handle_client, args=(client_socket, addr))
        client_handler.start()

if __name__ == "__main__":
    start_server()