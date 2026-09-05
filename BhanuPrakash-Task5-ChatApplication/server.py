import socket
import threading
from datetime import datetime

HOST = "127.0.0.1"
PORT = 5555

clients = []
names = []


def broadcast(message, sender):
    for client in clients:
        if client != sender:
            try:
                client.send(message.encode())
            except:
                remove_client(client)


def remove_client(client):
    if client in clients:
        index = clients.index(client)
        clients.remove(client)
        name = names[index]
        names.remove(name)
        client.close()

        message = f"[{datetime.now().strftime('%H:%M')}] {name} disconnected."
        broadcast(message, None)


def handle_client(client):
    try:
        name = client.recv(1024).decode()
        names.append(name)
        clients.append(client)

        print(f"{name} connected.")

        welcome = f"[{datetime.now().strftime('%H:%M')}] {name} joined the chat."
        broadcast(welcome, client)

        while True:
            message = client.recv(1024).decode()

            if not message:
                break

            timestamp = datetime.now().strftime("%H:%M")
            full_message = f"[{timestamp}] {name}: {message}"

            print(full_message)
            broadcast(full_message, client)

    except:
        pass

    finally:
        remove_client(client)


def start_server():
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind((HOST, PORT))
    server.listen()

    print(f"Server started on {HOST}:{PORT}")
    print("Waiting for clients...")

    while True:
        client, address = server.accept()
        print(f"Connection from {address}")

        thread = threading.Thread(target=handle_client, args=(client,))
        thread.start()


start_server()