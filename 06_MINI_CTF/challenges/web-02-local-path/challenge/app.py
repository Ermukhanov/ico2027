from http.server import BaseHTTPRequestHandler, HTTPServer
from pathlib import Path
from urllib.parse import urlsplit, parse_qs, unquote

BASE = Path(__file__).resolve().parent


def route(path):
    """Return (status, body) for one local viewer request."""
    query = urlsplit(path)
    if query.path == "/":
        return 200, (BASE / "www/index.html").read_bytes()
    if query.path == "/read":
        name = parse_qs(query.query).get("name", [""])[0]
        try:
            # Intentionally vulnerable: no check that the resolved path stays in www/.
            return 200, (BASE / "www" / unquote(name)).read_bytes()
        except OSError:
            return 404, b"not found\n"
    return 404, b"not found\n"


class H(BaseHTTPRequestHandler):
    def do_GET(self):
        status, body = route(self.path)
        self.send_response(status)
        self.end_headers()
        self.wfile.write(body)


if __name__ == "__main__":
    HTTPServer(("127.0.0.1", 8008), H).serve_forever()
