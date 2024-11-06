#!/bin/bash

# Устанавливаем базовый порт
MIN_PORT=60000

# Задаем список IP-адресов вручную для тестирования
ILIST=("127.0.0.1")

# Выводим IP-адреса для проверки
echo "IP addresses to be used: ${ILIST[@]}"

# Функция для запуска слушателя в фоновом режиме
start_listener() {
    local ip=$1
    local port=$2
    # Запускаем слушателя в фоновом режиме и перенаправляем вывод в файл
    python ./src/main.py listener "$ip" "$port" > "listener_${ip}_${port}.log" 2>&1 &
    echo $!  # Выводим PID процесса
}

# Функция для запуска отправителя
start_sender() {
    local ip=$1
    local port=$2
    # Запускаем отправителя в фоновом режиме
    python ./src/main.py sender "$ip" "$port" > "sender_${ip}_${port}.log" 2>&1 &
}

# Массив для хранения PID слушателей
listener_pids=()

# Запускаем слушателей и отправителей
for index in "${!ILIST[@]}"; do
    ip="${ILIST[$index]}"
    port=$((MIN_PORT + index))
    
    # Запускаем слушателя и сохраняем его PID
    listener_pid=$(start_listener "$ip" "$port")
    listener_pids+=($listener_pid)
    
    # Запускаем отправителя
    start_sender "$ip" "$port"
    
    echo "Started listener on $ip:$port with PID $listener_pid"
    echo "Started sender connecting to $ip:$port"
done

# Ожидание завершения отправки
echo "Done. Press any key to exit."
read -n 1  # Ожидание нажатия любой клавиши

# Завершаем процессы слушателей
for pid in "${listener_pids[@]}"; do
    echo "Terminating listener with PID $pid"
    kill $pid
done

# Удаляем временные файлы
rm -f listener_*.log sender_*.log
echo "All listeners terminated and log files deleted."
