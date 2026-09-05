# Task 5 - Chat Application

## Objective

Build a real-time two-user command-line chat application in Python using
sockets and threading.

## Features

-   Server script that listens for incoming client connections.
-   Client script that connects to the server.
-   Real-time, bidirectional messaging between connected clients.
-   Messages include a timestamp and username.
-   Users can join and leave the chat.
-   Other users are notified when a user joins or disconnects.
-   Runs locally using `127.0.0.1` (localhost).
-   Supports multiple client connections using Python threads.

## Technologies Used

-   Python
-   `socket` module
-   `threading` module
-   `datetime` module

## Project Structure

``` text
BhanuPrakash-Task5-ChatApplication/
│
├── server.py
├── client.py
└── README.md
```

## How to Run

### 1. Start the Server

Open a terminal in the project folder and run:

``` bash
python server.py
```

The server will display:

``` text
Server started on 127.0.0.1:5555
Waiting for clients...
```

Keep this terminal running.

### 2. Start Client 1

Open another terminal in the same project folder:

``` bash
python client.py
```

Enter a username when prompted, for example:

``` text
Enter your name: Alice
```

### 3. Start Client 2

Open a third terminal and run:

``` bash
python client.py
```

Enter another username:

``` text
Enter your name: Bob
```

Both clients can now exchange messages.

## Example

Alice may see:

``` text
Connected to the chat!
Type your message and press Enter.
Type 'exit' to leave the chat.

[11:09] Bob joined the chat.
[11:09] Bob: Hello Alice!
```

Bob can reply:

``` text
You: Hello Bob!
```

When a user leaves, the other client is notified:

``` text
[11:10] Bob disconnected.
```

To leave the chat, type:

``` text
exit
```

## How It Works

The server creates a TCP socket and listens on port `5555`.

When a client connects:

1.  The client sends its username to the server.
2.  The server creates a separate thread to handle that client.
3.  Messages received from a client are given a timestamp and username.
4.  The server broadcasts the message to the other connected clients.
5.  When a client disconnects, the server notifies the remaining
    clients.

The client also uses a separate receiving thread so that it can receive
messages while the user is typing.

## Security and Limitations

This project is designed for learning socket programming and is intended
for local use.

-   Messages are transmitted through a normal TCP connection and are
    **not end-to-end encrypted**.
-   The application does not provide authentication or password
    protection.
-   Messages are not permanently stored in a database.
-   The server keeps connected clients in memory while it is running.
-   For production use, encrypted transport such as TLS, authentication,
    input validation, and secure message storage should be added.

## Learning Resources

The networking concepts for this project are based on beginner Python
socket programming tutorials and the official Python documentation.

-   Python Socket Documentation:
    https://docs.python.org/3/library/socket.html
-   Python Threading Documentation:
    https://docs.python.org/3/library/threading.html

## Author

**Bhanu Prakash**

Oasis Infobyte Internship - Task 5
