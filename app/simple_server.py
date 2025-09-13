from http.server import HTTPServer, SimpleHTTPRequestHandler
from routes.api import handle_post
import os

PORT = 8081
TEMPLATES_DIR = os.path.join(os.path.dirname(__file__), "templates")
STATIC_DIR = os.path.join(os.path.dirname(__file__), "static")

class Handler(SimpleHTTPRequestHandler):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, directory=TEMPLATES_DIR, **kwargs)

    def do_POST(self):
        length = int(self.headers['Content-Length'])
        post_data = self.rfile.read(length)
        handle_post(post_data.decode())
        self.send_response(200)
        self.send_header('Content-type','text/html')
        self.end_headers()
        self.wfile.write(b"Received your text!")

httpd = HTTPServer(("", PORT), Handler)
print(f"Server running on 0.0.0.0:{PORT}")
httpd.serve_forever()
