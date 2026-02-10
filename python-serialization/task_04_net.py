#!/usr/bin/python3
"""
Module for Client-Server application with serialization.
"""

import socket
import json


def start_server():
    """Starts a TCP server that listens on port 65432,
    receives JSON data, deserializes it, and prints it."""
    host = "localhost"
    port = 65432

    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind((host, port))
    server_socket.listen(1)
    print(f"Server listening on port {port}...")

    while True:
        client_socket, addr = server_socket.accept()
        print(f"Connection from {addr} established.")

        data = client_socket.recv(1024).decode("utf-8")
        if data:
            deserialized_data = json.loads(data)
            print("Received data:")
            print(deserialized_data)

        client_socket.close()


def send_data(data, host="localhost", port=65432):
    """Connects to the server and sends JSON data."""
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect((host, port))

    serialized_data = json.dumps(data)
    client_socket.sendall(serialized_data.encode("utf-8"))

    print(f"Data sent to server at {host}:{port}.")
    client_socket.close()
