# TCP Data Transfer Service

---

## Project Description

This project implements a TCP service for sending and receiving data. The main goal is to create an efficient and user-friendly tool for working with network connections.

The service supports two modes:

1. **Sender** — establishes a connection and sends data.
2. **Listener** — receives data, decodes it, and displays key information, including the size and the first 16 bytes of the transmitted block.

The functionality is implemented in two main classes:

- **`MySender`** — responsible for sending data over a TCP connection.
- **`MyListener`** — responsible for receiving data, processing size information, and outputting the first bytes of data.

---

## Project Structure

```plaintext
src/
├── main.py                   # Entry point. Handles command-line arguments and starts the sender or listener.
├── testtask/
│   ├── my_sender.py          # MySender class for TCP connection and data transmission.
│   ├── my_listener.py        # MyListener class for TCP server and data reception.
run_test.sh                   # Bash script for testing a single listener and sender.
```

---

## Implementation Details

### MySender

The **`MySender`** class performs the following functions:

- **Dynamic data size encoding**: The data size is encoded in the minimal number of bytes possible, reducing transmission overhead.
- **Configurable data size**: By default, the data size is limited to 1 KB for testing, but this value can be adjusted in the **`MAX_SIZE`** constant.

### MyListener

The **`MyListener`** class implements a TCP server that:

- Accepts data from the sender.
- Decodes the data size using a variable number of bytes.
- Outputs the data size and the first 16 bytes for verification.

### Testing Script

The **`run_test.sh`** script automates the process of starting one listener and one sender for local testing. By default, it uses the `127.0.0.1` (localhost) IP address for simplicity.

---

## Usage

### Running the Sender

```bash
python src/main.py sender <server_address> <port>
```

### Running the Listener

```bash
python src/main.py listener <ip_address> <port>
```

### Example

1. Start the listener:

   ```bash
   python src/main.py listener 127.0.0.1 12345
   ```

2. Start the sender:

   ```bash
   python src/main.py sender 127.0.0.1 12345
   ```

### Automated Testing

To run automated testing, execute:

```bash
bash run_test.sh
```

---

## Plans for Improvement

1. **Support for multiple instances**: Extend `run_test.sh` to allow running multiple sender and listener processes on different ports.
2. **Dynamic IP detection**: Implement logic to retrieve the IP addresses of all interfaces, tailored to the target operating system.
3. **Scalable data transfer**: Optimize the project to handle large data sizes (up to 8 GB).

---

## License

This project is open-source and free to use. Contributions and suggestions are welcome!


# TCP-сервис для передачи данных

---

## Описание проекта

Этот проект реализует TCP-сервис для передачи и приема данных. Основная цель — создание эффективного и удобного инструмента для работы с сетевыми соединениями. 

Сервис поддерживает два режима работы:

1. **Отправитель** — устанавливает соединение и отправляет данные.
2. **Слушатель** — принимает данные, декодирует их и выводит ключевую информацию, включая размер и первые 16 байт переданного блока.

Функционал реализован в двух основных классах:

- **`MySender`** — передает данные через TCP-соединение.
- **`MyListener`** — принимает данные, обрабатывает информацию о размере и выводит первые байты данных.

---

## Структура проекта

```plaintext
src/
├── main.py                   # Точка входа. Обрабатывает аргументы командной строки и запускает отправителя или слушателя.
├── testtask/
│   ├── my_sender.py          # Класс MySender для TCP-соединения и передачи данных.
│   ├── my_listener.py        # Класс MyListener для TCP-сервера и приема данных.
run_test.sh                   # Bash-скрипт для тестирования одного слушателя и отправителя.
```

---

## Детали реализации

### MySender

Класс **`MySender`** выполняет следующие функции:

- **Динамическое кодирование размера данных**: Размер данных кодируется в минимально возможное количество байт, что снижает объем передаваемой информации.
- **Настраиваемый размер данных**: По умолчанию размер данных ограничен 1 КБ для тестирования, но это значение можно изменить в константе **`MAX_SIZE`**.

### MyListener

Класс **`MyListener`** реализует TCP-сервер, который:

- Принимает данные от отправителя.
- Декодирует длину данных, используя переменное количество байт.
- Выводит размер данных и первые 16 байт для проверки.

### Скрипт тестирования

Скрипт **`run_test.sh`** автоматизирует запуск одного слушателя и одного отправителя для локального тестирования. По умолчанию используется IP-адрес `127.0.0.1` (localhost) для упрощения.

---

## Использование

### Запуск отправителя

```bash
python src/main.py sender <server_address> <port>
```

### Запуск слушателя

```bash
python src/main.py listener <ip_address> <port>
```

### Пример

1. Запустите слушателя:

   ```bash
   python src/main.py listener 127.0.0.1 12345
   ```

2. Запустите отправителя:

   ```bash
   python src/main.py sender 127.0.0.1 12345
   ```

### Автоматическое тестирование

Для автоматического тестирования запустите:

```bash
bash run_test.sh
```

---


## Лицензия

Проект является открытым и свободным для использования. Мы приветствуем любые предложения и доработки!
