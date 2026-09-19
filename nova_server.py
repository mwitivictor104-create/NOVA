from http.server import BaseHTTPRequestHandler, HTTPServer
import json

from chatbot import chat


HOST = "0.0.0.0"
PORT = 8080


class NovaHandler(BaseHTTPRequestHandler):

    def send_json(self, data, status=200):
        body = json.dumps(data, ensure_ascii=False).encode("utf-8")

        self.send_response(status)
        self.send_header("Content-Type", "application/json; charset=utf-8")
        self.send_header("Content-Length", str(len(body)))
        self.end_headers()

        self.wfile.write(body)

    def do_GET(self):
        if self.path == "/":
            self.send_json({
                "status": "online",
                "name": "NOVA",
                "message": "NOVA API is running"
            })
        else:
            self.send_json({
                "error": "Not found"
            }, 404)

    def do_POST(self):
        if self.path != "/chat":
            self.send_json({
                "error": "Not found"
            }, 404)
            return

        try:
            length = int(self.headers.get("Content-Length", "0"))
            raw = self.rfile.read(length)

            data = json.loads(raw.decode("utf-8"))
            message = str(data.get("message", "")).strip()

            if not message:
                self.send_json({
                    "error": "Message is empty"
                }, 400)
                return

            response = chat(message)

            self.send_json({
                "name": "NOVA",
                "message": str(response)
            })

        except Exception as e:
            self.send_json({
                "error": str(e)
            }, 500)

    def log_message(self, format, *args):
        print("[NOVA API]", format % args)


if __name__ == "__main__":
    print("=" * 40)
    print("       NOVA API SERVER")
    print("=" * 40)
    print(f"Listening on http://{HOST}:{PORT}")
    print("POST /chat")
    print("Press CTRL+C to stop.")
    print("=" * 40)

    server = HTTPServer((HOST, PORT), NovaHandler)

    try:
        server.serve_forever()
    except KeyboardInterrupt:
        print("\nNOVA API stopped.")
        server.server_close()
