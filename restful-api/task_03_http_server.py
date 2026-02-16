#!/usr/bin/python3
"""Module in Python's standard library provides
basic classes for implementing web servers
and handling HTTP requests.

"""

from http.server import BaseHTTPRequestHandler, HTTPServer
import json

HOST = "localhost"
PORT = 8000


class Handler(BaseHTTPRequestHandler):

    def do_GET(self):
        """Handle GET requests."""

        if self.path == "/":
            self.send_response(200)
            self.send_header("Content-Type", "text/plain")
            self.end_headers()
            self.wfile.write(b"Hello, this is a simple API!")

        elif self.path == "/data":
            data = {
                "name": "John",
                "age": 30,
                "city": "New York"
            }

            json_data = json.dumps(data)

            self.send_response(200)
            self.send_header("Content-Type", "application/json")
            self.end_headers()
            self.wfile.write(json.dumps(data).encode("utf-8"))

        elif self.path == "/status":
            self.send_response(200)
            self.send_header("Content-Type", "text/plain")
            self.end_headers()
            self.wfile.write(b"OK")

        elif self.path == "/info":
            info = {
                "version": "1.0",
                    "description": "A simple API built with http.server"
                }

            json_info = json.dumps(info)

            self.send_response(200)
            self.send_header("Content-Type", "application/json")
            self.end_headers()
            self.wfile.write(json.dumps(info).encode("utf-8"))

        else:
            self.send_response(404)
            self.send_header("Content-Type", "text/plain")
            self.end_headers()
            self.wfile.write(b"Endpoint not found")


def run():
    """Run the HTTP server."""

    server = HTTPServer((HOST, PORT), Handler)
    print(f"Server running at http://{HOST}:{PORT}/")
    server.serve_forever()

if __name__ == "__main__":
    run()
