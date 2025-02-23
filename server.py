import socket
import threading
import pytz
from datetime import datetime

HOST = '127.0.0.5'  
PORT = 8000     

# Hàm xử lý kết nối từ client
def handle_client(client_socket, addr):
    print(f"[NEW CONNECTION] {addr} connected.")
    
    while True:
        try:
            # Nhận tin nhắn từ client
            message = client_socket.recv(1024).decode('utf-8')
            if not message:
                break
            if(message == "check"):
                print(f"[MESSAGE FROM {addr}] {message}")
                client_socket.send(f"Server received: {"connected"}".encode('utf-8'))
                client_socket.send(f"Server received: {"xconnected"}".encode('utf-8'))
            else:
                print(f"[MESSAGE FROM {addr}] {message}")
                country_name = pytz.timezone(message)
                country_time = datetime.now(country_name)
                print(country_time.strftime("%d-%m-%y*%H:%M:%S"))

                client_socket.send(f"{country_time.strftime("%d-%m-%y*%H:%M:%S")}".encode('utf-8'))
            # Gửi lại tin nhắn đến client
             
        
        except ConnectionResetError:
            break

    print(f"[DISCONNECT] {addr} disconnected.")
    client_socket.close()

# Thiết lập server
def start_server(host=HOST, port=PORT):
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