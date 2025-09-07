import http.server
import socketserver

PORT = 8081

class Handler(http.server.SimpleHTTPRequestHandler):
    def do_POST(self):
        content_length = int(self.headers['Content-Length'])
        post_data = self.rfile.read(content_length)
        print(f"Received: {post_data.decode('utf-8')}")
        self.send_response(200)
        self.end_headers()
        self.wfile.write(b"Data received")

with socketserver.TCPServer(("", PORT), Handler) as httpd:
    # "" binds to all interfaces (0.0.0.0)
    ip, port = httpd.server_address
    print(f"Server running on {ip}:{port}")  # <-- print bound IP and port
    httpd.serve_forever()

