import socket

class MyListener:
    def __init__(self, ip_address, port):
        self.ip_address = ip_address
        self.port = port

    def start_listening(self):
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server_socket:
            server_socket.bind((self.ip_address, self.port))
            server_socket.listen(1)
            print(f"Listening on {self.ip_address}:{self.port}")
            
            conn, addr = server_socket.accept()
            with conn:
                print(f"Connected by {addr}")
                
                # Чтение первых байтов для определения размера data_size
                size_bytes = bytearray()
                
                # Считаем до 6 байт (максимальный размер по заданию)
                for _ in range(6):
                    byte = conn.recv(1)
                    if not byte:
                        print("Failed to receive size data.")
                        return
                    size_bytes.append(byte[0])
                    # Прекращаем чтение, если достигли конца значащих байтов
                    if len(size_bytes) == 6 or size_bytes[0] != 0:
                        break
                
                # Преобразуем байты в целое число
                data_size = int.from_bytes(size_bytes, byteorder='big')
                
                print(f"Expecting to receive data of size: {data_size} bytes")

                # Чтение данных в соответствии с полученным размером
                data = conn.recv(data_size)
                print(f"Received data size: {len(data)} bytes")
                print(f"First 16 bytes in hex: {data[:16].hex()}")
