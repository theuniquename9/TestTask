import socket
import random

class MySender:
    def __init__(self, server_address, port):
        self.server_address = server_address
        self.port = port

    def _generate_data(self, max_size=1024):  # Ограничение данных до 1 КБ для тестирования
        size = random.randint(1, max_size)
        return bytes(random.getrandbits(8) for _ in range(size))

    def send_data(self):
        data = self._generate_data()
        data_size = len(data).to_bytes(4, byteorder='big')
        
        for attempt in range(3):  # Попытки подключения
            try:
                with socket.create_connection((self.server_address, self.port), timeout=10) as sock:
                    sock.sendall(data_size + data)  # Отправка данных в формате <размер><данные>
                    print("Data sent successfully.")
                    break
            except (socket.timeout, ConnectionRefusedError):
                print(f"Attempt {attempt + 1} failed. Retrying in 10 seconds...")
        else:
            print("Failed to send data after 3 attempts.")
