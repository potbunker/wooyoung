from http.server import BaseHTTPRequestHandler, HTTPServer


class testHTTPServer_RequestHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header('Content-Type', 'text/html')
        self.end_headers()
        message = "Hello World!"
        self.wfile.write(bytes(message, "utf8"))
        return


def run():
    print('starting server...')
    server_address = ('192.168.1.112', 8081)
    httpd = HTTPServer(server_address, testHTTPServer_RequestHandler)
    print('running server...')
    httpd.serve_forever()


run()
