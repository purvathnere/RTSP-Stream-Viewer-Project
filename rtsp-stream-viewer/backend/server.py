from http.server import SimpleHTTPRequestHandler, HTTPServer
import mimetypes

# Add m3u8 mime type
mimetypes.add_type('application/vnd.apple.mpegurl', '.m3u8')

class CustomHandler(SimpleHTTPRequestHandler):
    def end_headers(self):
        # To allow CORS (if frontend is on different origin)
        self.send_header('Access-Control-Allow-Origin', '*')
        SimpleHTTPRequestHandler.end_headers(self)

PORT = 8080
httpd = HTTPServer(('0.0.0.0', PORT), CustomHandler)
print(f"Serving at port {PORT}")
httpd.serve_forever()
