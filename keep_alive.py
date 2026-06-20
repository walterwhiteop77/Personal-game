import os
import threading
import time
import urllib.request
from http.server import BaseHTTPRequestHandler, HTTPServer

import info


class _Handler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header("Content-Type", "text/plain")
        self.end_headers()
        self.wfile.write(b"OK")

    def log_message(self, *_):
        pass


def _serve():
    HTTPServer(("0.0.0.0", info.PORT), _Handler).serve_forever()


def _ping():
    time.sleep(60)                                          # let server come up first
    url = os.environ.get("RENDER_EXTERNAL_URL") or f"http://localhost:{info.PORT}"
    interval = info.PING_INTERVAL_MINUTES * 60
    print(f"[keep_alive] pinger → {url} every {info.PING_INTERVAL_MINUTES} min")
    while True:
        try:
            urllib.request.urlopen(url, timeout=10)
            print(f"[keep_alive] ping ok")
        except Exception as e:
            print(f"[keep_alive] ping failed: {e}")
        time.sleep(interval)


def keep_alive():
    threading.Thread(target=_serve, daemon=True).start()
    threading.Thread(target=_ping,  daemon=True).start()
    print(f"[keep_alive] HTTP server started on port {info.PORT}")
