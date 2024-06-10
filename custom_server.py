from http.server import HTTPServer, SimpleHTTPRequestHandler
import os

class CustomHTTPRequestHandler(SimpleHTTPRequestHandler):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, directory='.', **kwargs)

    def do_GET(self):
        if self.path == '/':
            self.send_response(302)
            self.send_header('Location', '/sv/index.html')
            self.end_headers()
        else:
            super().do_GET()

    def send_error(self, code, message=None):
        if code == 404:
            self.send_response(404)
            self.send_header('Content-type', 'text/html')
            self.end_headers()
            with open('404.html', 'rb') as f:
                self.copyfile(f, self.wfile)
        else:
            super().send_error(code, message)

# Skapa en HTTP-server med en anpassad förfrågningshanterare
server_address = ('', 8000)  # Ändra porten vid behov
httpd = HTTPServer(server_address, CustomHTTPRequestHandler)

# Starta servern
print('Server running on port 8000...')
httpd.serve_forever()
