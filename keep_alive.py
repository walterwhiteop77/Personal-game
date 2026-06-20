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


def _run_server():
    HTTPServer(("0.0.0.0", info.PORT), _Handler).serve_forever()


def _run_pinger():
    time.sleep(60)
    interval = info.PING_INTERVAL_MINUTES * 60
    while True:
        try:
            urllib.request.urlopen(info.PING_URL, timeout=10)
            print(f"[keep_alive] ping ok → {info.PING_URL}")
        except Exception as e:
            print(f"[keep_alive] ping failed: {e}")
        time.sleep(interval)


def keep_alive():
    threading.Thread(target=_run_server, daemon=True).start()
    threading.Thread(target=_run_pinger, daemon=True).start()
    print(f"[keep_alive] HTTP server on port {info.PORT}, "
          f"pinging every {info.PING_INTERVAL_MINUTES} min")
