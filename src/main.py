import sys
from testtask.my_sender import MySender
from testtask.my_listener import MyListener

def main():
    if len(sys.argv) < 2:
        print("Usage: main.py <role> [options]")
        sys.exit(1)

    role = sys.argv[1]

    if role == "sender":
        if len(sys.argv) != 4:
            print("Usage for sender: main.py sender <server_address> <port>")
            sys.exit(1)
        server_address = sys.argv[2]
        port = int(sys.argv[3])
        sender = MySender(server_address, port)
        sender.send_data()

    elif role == "listener":
        if len(sys.argv) != 4:
            print("Usage for listener: main.py listener <ip_address> <port>")
            sys.exit(1)
        ip_address = sys.argv[2]
        port = int(sys.argv[3])
        listener = MyListener(ip_address, port)
        listener.start_listening()

    else:
        print("Unknown role. Use 'sender' or 'listener'.")
        sys.exit(1)

if __name__ == "__main__":
    main()

