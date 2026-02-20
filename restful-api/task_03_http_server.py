#!/usr/bin/python3

from http.server import HTTPServer, BaseHTTPRequestHandler
import json


class SimpleHandler(BaseHTTPRequestHandler):

    def do_GET(self):
        try:
            if self.path == "/" or self.path == "":
                self.send_response(200)
                self.send_header("Content-Type", "text/plain; charset=utf-8")
                self.end_headers()
                self.wfile.write(b"Hello, this is a simple API!")

            elif self.path == "/data":
                self.send_response(200)
                self.send_header("Content-Type", "application/json; charset=utf-8")
                self.end_headers()
                data = {"name": "John", "age": 30, "city": "New York"}
                self.wfile.write(json.dumps(data).encode("utf-8"))

            elif self.path == "/info":
                self.send_response(200)
                self.send_header("Content-Type", "application/json; charset=utf-8")
                self.end_headers()
                info = {"version": "1.0", "description": "A simple API built with http.server"}
                self.wfile.write(json.dumps(info).encode("utf-8"))
            elif self.path == "/status":
                self.send_response(200)
                self.send_header("Content-Type", "text/plain; charset=utf-8")
                self.end_headers()
                self.wfile.write(b"OK")

            else:
                self.send_response(404)
                self.send_header("Content-Type", "text/plain; charset=utf-8")
                self.end_headers()
                self.wfile.write(b"Endpoint not found")

        except Exception as e:
            self.send_response(500)
            self.send_header("Content-Type", "text/plain; charset=utf-8")
            self.end_headers()
            self.wfile.write(f"Internal Server Error: {e}".encode("utf-8"))

server_address = ("", 8000)
httpd = HTTPServer(server_address, SimpleHandler)
print("Server running at http://localhost:8000")
httpd.serve_forever()
