#!/usr/bin/python3
"""Module in Python's standard library provides
basic classes for implementing web servers
and handling HTTP requests.

"""

import http.server
import socketserver
import json

PORT = 8000


class Handler(http.server.BaseHTTPRequestHandler):

    def do_GET(self):
        """Handle GET requests."""

        if self.path == "/":
            self.send_response(200)
            self.send_header("Content-Type", "text/plain; charset=utf-8")
            self.end_headers()
            self.wfile.write("Bonjour, ceci est une Api simple !".encode("utf-8"))

        elif self.path == "/data":
            self.send_response(200)
            self.send_header("Content-Type", "application/json")
            self.end_headers()

            data = {"name": "John", "age": 30, "city": "New York"}

            self.wfile.write(json.dumps(data).encode("utf-8"))

        elif self.path == "/status":
            self.send_response(200)
            self.send_header("Content-Type", "text/plain")
            self.end_headers()
            self.wfile.write(b"OK")

        elif self.path == "/info":
            self.send_response(200)
            self.send_header("Content-Type", "application/json")
            self.end_headers()

            info = {
                "version": "1.0",
                "description": "Une API simple construite avec http.server"
            }

            self.wfile.write(json.dumps(info).encode("utf-8"))

        else:
            self.send_response(404)
            self.send_header("Content-Type", "text/plain; charset=utf-8")
            self.end_headers()
            self.wfile.write("Point de terminaison introuvable".encode("utf-8"))


with socketserver.TCPServer(("", PORT), Handler) as httpd:
    httpd.serve_forever()
