import socket
import random

class MySender:
    def __init__(self, server_address, port):
        self.server_address = server_address
        self.port = port

    def _generate_data(self, max_size=1024):  # Ограничение данных до 1 КБ для тестирования
        size = random.randint(1, max_size)
        return bytes(random.getrandbits(8) for _ in range(size))

    def _get_minimum_bytes_for_size(self, size):
        # Вычисляем минимальное количество байт, необходимое для представления размера данных
        # size.bit_length() возвращает количество бит, требуемых для представления size
        # (size.bit_length() + 7) // 8 вычисляет количество байт для этого количества бит
        byte_length = (size.bit_length() + 7) // 8
        return size.to_bytes(byte_length, byteorder='big')

    def send_data(self):
        data = self._generate_data()
        # Получаем длину данных и представляем её в минимально необходимом количестве байт
        data_size = self._get_minimum_bytes_for_size(len(data))
        
        for attempt in range(3):  # Попытки подключения
            try:
                # Создаем TCP-соединение с сервером
                with socket.create_connection((self.server_address, self.port), timeout=10) as sock:
                    # Отправляем сначала размер данных в формате <размер><данные>
                    sock.sendall(data_size + data)
                    print("Data sent successfully.")
                    break
            except (socket.timeout, ConnectionRefusedError) as e:
                # В случае неудачи соединения ждем 10 секунд и пробуем снова
                print(f"Attempt {attempt + 1} failed ({e}). Retrying in 10 seconds...")
                time.sleep(10)
        else:
            # Если все три попытки неудачны, выводим сообщение об ошибке
            print("Failed to send data after 3 attempts.")
