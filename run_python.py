#!/usr/bin/env python

# simple python web server to run locally
# CORS restricted websites e.g.
# wasm or serviceWorker

import sys
import socketserver
from http.server import SimpleHTTPRequestHandler

class WasmHandler(SimpleHTTPRequestHandler):
    def end_headers(self):
        # Include additional response headers here. CORS for example:
        
        WasmHandler.extensions_map['.wasm'] = 'application/wasm'
        self.send_header('Access-Control-Allow-Origin', '*')
        self.send_header('Cross-Origin-Embedder-Policy', 'require-corp')
        self.send_header('Cross-Origin-Opener-Policy', 'same-origin')

        SimpleHTTPRequestHandler.end_headers(self)
        
WasmHandler.extensions_map['.wasm'] = 'application/wasm'

if __name__ == '__main__':
    PORT = 7878
    with socketserver.TCPServer(("", PORT), WasmHandler) as httpd:
        print("Listening on port {}. Press Ctrl+C to stop.".format(PORT))
        httpd.serve_forever()
