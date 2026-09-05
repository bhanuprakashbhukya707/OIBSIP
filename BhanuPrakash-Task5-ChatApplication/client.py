import socket
import threading
from datetime import datetime

HOST = "127.0.0.1"
PORT = 5555


def receive_messages(client):
    while True:
        try:
            message = client.recv(1024).decode()

            if not message:
                break

            print("\n" + message)
            print("You: ", end="", flush=True)

        except:
            print("\nDisconnected from the server.")
            break


def start_client():
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    try:
        client.connect((HOST, PORT))
    except:
        print("Could not connect to the server.")
        return

    name = input("Enter your name: ")
    client.send(name.encode())

    print("\nConnected to the chat!")
    print("Type your message and press Enter.")
    print("Type 'exit' to leave the chat.\n")

    thread = threading.Thread(
        target=receive_messages,
        args=(client,)
    )
    thread.daemon = True
    thread.start()

    while True:
        try:
            message = input("You: ")

            if message.lower() == "exit":
                client.close()
                print("You left the chat.")
                break

            client.send(message.encode())

        except:
            client.close()
            break


start_client()