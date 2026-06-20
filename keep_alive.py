import os
import threading
import time
import urllib.request
from http.server import BaseHTTPRequestHandler, HTTPServer

PORT = int(os.environ.get("PORT", 8080))
PING_INTERVAL = 14 * 60  # 14 minutes — just under free-tier idle cutoff


class _Handler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header("Content-Type", "text/plain")
        self.end_headers()
        self.wfile.write(b"OK")

    def log_message(self, *_):
        pass  # silence request logs


def _run_server():
    server = HTTPServer(("0.0.0.0", PORT), _Handler)
    server.serve_forever()


def _run_pinger(url: str):
    time.sleep(60)  # wait for server to be ready before first ping
    while True:
        try:
            urllib.request.urlopen(url, timeout=10)
            print(f"[keep_alive] ping ok → {url}")
        except Exception as e:
            print(f"[keep_alive] ping failed: {e}")
        time.sleep(PING_INTERVAL)


def keep_alive():
    """
    Call this once before bot.run_polling().
    Starts two daemon threads:
      1. A tiny HTTP server so the host sees an open port.
      2. A self-pinger that hits the server every 14 minutes
         to prevent free-tier sleep (Render, Koyeb, Railway).
    """
    ping_url = os.environ.get("RENDER_EXTERNAL_URL") or f"http://localhost:{PORT}"

    threading.Thread(target=_run_server, daemon=True).start()
    threading.Thread(target=_run_pinger, args=(ping_url,), daemon=True).start()

    print(f"[keep_alive] HTTP server on port {PORT}, pinging {ping_url} every {PING_INTERVAL // 60} min")
