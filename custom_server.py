from http.server import HTTPServer, SimpleHTTPRequestHandler
from os import path

class CustomHTTPRequestHandler(SimpleHTTPRequestHandler):
    # Override the do_GET method to handle custom error pages
    def do_GET(self):
        # Check if the requested file exists
        if path.exists(self.translate_path(self.path)):
            # Serve the file if it exists
            return SimpleHTTPRequestHandler.do_GET(self)
        else:
            # Serve the custom 404 page if the file does not exist
            self.send_response(404)
            self.send_header('Content-type', 'text/html')
            self.end_headers()
            with open('/workspace/nordic_automation/404.html', 'rb') as f:
                self.copyfile(f, self.wfile)

# Create an HTTP server with custom request handler
server_address = ('', 8000)  # Change port as needed
httpd = HTTPServer(server_address, CustomHTTPRequestHandler)

# Start the server
print('Server running...')
httpd.serve_forever()
