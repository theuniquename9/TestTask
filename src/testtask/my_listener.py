import socket

class MyListener:
    def __init__(self, ip_address, port):
        self.ip_address = ip_address
        self.port = port

    def start_listening(self):
        try:
            with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server_socket:
                server_socket.bind((self.ip_address, self.port))
                server_socket.listen(1)
                print(f"Listening on {self.ip_address}:{self.port}")
                
                conn, addr = server_socket.accept()
                with conn:
                    print(f"Connected by {addr}")
                    
                    # Получаем первые 4 байта, которые представляют размер данных
                    size_data = conn.recv(4)
                    if not size_data:
                        print("Failed to receive data size.")
                        return
                    
                    data_size = int.from_bytes(size_data, byteorder='big')
                    print(f"Expecting to receive data of size: {data_size} bytes")
                    
                    # Получаем сами данные (первые 16 байт для демонстрации)
                    data = conn.recv(min(data_size, 16))
                    if data:
                        print(f"First 16 bytes in hex: {data.hex()[:32]}")
                    else:
                        print("No data received.")
                        
        except Exception as e:
            print(f"An error occurred: {e}")
