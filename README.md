# TestTask

## Описание проекта

Данный проект реализует TCP-сервис для передачи и приема данных. Функционал разделен на два класса: `MySender` для отправки данных и `MyListener` для приема. Программа может работать в двух режимах: отправителя и слушателя, управляемых через параметры командной строки.

## Структура проекта

- **src/main.py** - Основная функция `main`, которая обрабатывает параметры командной строки и запускает отправителя или слушателя в зависимости от роли.
- **src/testtask/my_sender.py** - Класс `MySender` для создания TCP-соединения и отправки данных.
- **src/testtask/my_listener.py** - Класс `MyListener` для запуска TCP-сервиса, приема данных и вывода их размера и первых 16 байт.
- **run_test.sh** - Bash-скрипт для автоматического запуска одного экземпляра слушателя и одного экземпляра отправителя.


## Отклонения от требований задания

В ходе выполнения задания были внесены некоторые изменения, чтобы учесть ограничения среды и упростить тестирование. 

1. **Ограничение размера данных в `MySender`**:
   - Согласно требованиям задания, метод `_generate_data` в классе `MySender` должен был поддерживать генерацию данных объемом до 8 ГБ. Однако генерация и передача такого объема данных может вызвать значительную нагрузку на память и систему, особенно при тестировании. Поэтому максимальный объем данных был временно ограничен до 1 КБ. Это значение можно изменить в константе `MAX_SIZE` в `MySender`, если потребуется протестировать передачу больших объемов данных.

2. **Использование статического IP-адреса `127.0.0.1`**:
   - Задание предусматривало автоматическое определение IPv4-адресов всех сетевых интерфейсов для использования их в качестве адресов слушателей. Однако, из-за различий в командах для получения IP-адресов в разных операционных системах (например, `hostname -I` в Linux и `ipconfig` в Windows), для упрощения тестирования я использовал статический IP `127.0.0.1` (localhost). Это позволяет тестировать функциональность на локальной машине без необходимости подключения к сети. Для полноценного использования всех интерфейсов можно добавить команду для получения IP-адресов, адаптированную под целевую операционную систему.
  
3. **Запуск одного экземпляра слушателя и отправителя в `run_test.sh`**:
   - В текущей реализации `run_test.sh` запускает только один экземпляр слушателя и один экземпляр отправителя. Задание предусматривало возможность запуска нескольких экземпляров, каждый на своем IP и порту. Для упрощения тестирования и во избежание конфликта портов было решено ограничиться одним экземпляром. Если потребуется запуск нескольких экземпляров, скрипт можно доработать, добавив цикл для инициализации дополнительных процессов на разных портах.

## Использование

```bash
# Запуск отправителя
python src/main.py sender <server_address> <port>

# Запуск слушателя
python src/main.py listener <ip_address> <port>
