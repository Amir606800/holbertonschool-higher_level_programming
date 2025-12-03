#!/usr/bin/env python3
""" Simple HTTP server """
from http.server import BaseHTTPRequestHandler, HTTPServer
import json
class MyClass(BaseHTTPRequestHandler):
    def do_GET(self):
        if self.path == "/":
            self.send_response(200)
            self.send_header("Content-type", "text/html")
            self.end_headers()
            self.wfile.write(b"Hello, this is a simple API!\n")
        elif self.path == "/data":
            self.send_response(200)
            self.send_header("Content-type", "application/json")
            self.end_headers()
            self.wfile.write(b'{"name": "John", "age": 30, "city": "New York"}\n')
        elif self.path == "/info":
            self.send_response(200)
            self.send_header("Content-type", "application/json")
            self.end_headers()
            self.wfile.write(b'{"version": "1.0", "description": "A simple API built with http.server"}\n')
        else:
            self.send_response(404)
            self.send_header('Content-type', "text/html")
            self.end_headers()
            self.wfile.write(b'Endpoint not found\n')
    def do_POST(self):
        length = int(self.headers.get('Content-Length'))
        body = self.rfile.read(length)
        self.send_response(200)
        self.send_header('Content-type','application/json')
        self.end_headers()
        self.wfile.write(json.dumps(json.loads(body)).encode())
def run(server_class=HTTPServer, handler_class=MyClass):
    server_address = ('', 8000)
    httpd = server_class(server_address, handler_class)
    httpd.serve_forever()

run()
