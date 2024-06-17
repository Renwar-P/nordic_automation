from http.server import HTTPServer, SimpleHTTPRequestHandler
import os

class CustomHTTPRequestHandler(SimpleHTTPRequestHandler):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, directory='.', **kwargs)

    def do_GET(self):
        # Redirect root path to /sv/index.html
        if self.path == '/':
            self.send_response(302)
            self.send_header('Location', 'index.html')
            self.end_headers()
        elif self.path.endswith('/'):
            # Handle paths ending with a slash (e.g., /somepath/)
            self.send_response(302)
            self.send_header('Location', self.path.rstrip('/') + '/index.html')
            self.end_headers()
        else:
            # Serve files normally
            super().do_GET()

    def send_error(self, code, message=None):
        if code == 404:
            self.send_response(404)
            self.send_header('Content-type', 'text/html')
            self.end_headers()
            try:
                custom_404_path = '/workspace/nordic_automation/404.html'
                print(f"Attempting to serve custom 404 page from: {custom_404_path}")
                with open(custom_404_path, 'rb') as f:
                    self.copyfile(f, self.wfile)
            except FileNotFoundError:
                print("Custom 404 page not found at specified path.")
                super().send_error(code, message)
        else:
            super().send_error(code, message)

# Create an HTTP server with the custom request handler
server_address = ('', 8000)  # Change the port if needed
httpd = HTTPServer(server_address, CustomHTTPRequestHandler)

# Start the server
print('Server running on port 8000...')
httpd.serve_forever()
