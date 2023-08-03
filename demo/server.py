import os
from http.server import BaseHTTPRequestHandler, HTTPServer
import time
import sys

class MyServer(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.end_headers()
        self.wfile.write(bytes("<p>Server ID: <span style=\"color:red\">%s</span></p>" % os.getpid(), "utf-8"))

if __name__ == "__main__":
    serverPort = 8080
    if (sys.argv.__len__() > 1):
        serverPort = int(sys.argv[1])
    webServer = HTTPServer(("localhost", serverPort), MyServer)
    print("Server started http://%s:%s" % ("localhost", serverPort))
    try:
        webServer.serve_forever()
    except KeyboardInterrupt:
        pass

    webServer.server_close()
    print("Server stopped.")
