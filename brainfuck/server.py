#!/usr/bin/env python

import SocketServer
import SimpleHTTPServer
import socket, select
import cgi

from brainfuck import BFParser

class MyTCPHandler(SocketServer.BaseRequestHandler):
    def handle(self):
        code = self.request.recv(1024).strip()

        result = BFParser(code).result

        self.request.sendall(result)

class MyUDPHandler(SocketServer.BaseRequestHandler):
    def handle(self):
        code = self.request[0].strip()
        socket = self.request[1]

        result = BFParser(code).result

        socket.sendto(result, self.client_address)

class MyHTTPHandler(SimpleHTTPServer.SimpleHTTPRequestHandler):
    def do_POST(self):
        post_data = self.rfile.read(int(self.headers.getheader('content-length')))
        post_vars = cgi.parse_qs(post_data)
        code = post_vars['code'][0]

        result = BFParser(code).result

        self.send_response(200)
        self.end_headers()
        self.wfile.write('<html><body><pre>%s</pre></body></html>' % result)

    def do_GET(self):
        self.send_response(200)
        self.end_headers()
        self.wfile.write('<html><body><form method="POST"><textarea rows="24" cols="80" name="code"></textarea><br/><input type="submit"/></form></body></html>')
        

def main():
    HOST, PORT = "localhost", 1982
    tcp_server = SocketServer.TCPServer((HOST, PORT), MyTCPHandler)
    udp_server = SocketServer.UDPServer((HOST, PORT), MyUDPHandler)
    http_server = SocketServer.TCPServer((HOST, PORT+1), MyHTTPHandler)
    servers = [tcp_server, udp_server, http_server]

    running = True
    while running:
        try:
            r, w, e = select.select(servers, [], [])
            for i in r:
                i.handle_request()
        except KeyboardInterrupt:
            for server in servers:
                if hasattr(server, 'finish'):
                    server.finish()
                server.socket.close()

            running = False
