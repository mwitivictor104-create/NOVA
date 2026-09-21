from http.server import BaseHTTPRequestHandler, HTTPServer
import json

from chatbot import chat


HOST = "0.0.0.0"
PORT = 8080


CHAT_PAGE = """<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>NOVA</title>
<style>
  :root{color-scheme:dark;}
  *{box-sizing:border-box;}
  body{
    margin:0; height:100vh; display:flex; flex-direction:column;
    font-family:-apple-system,Segoe UI,Roboto,sans-serif;
    background:#0f1115; color:#e6e6e6;
  }
  header{
    padding:14px 16px; font-weight:600; font-size:18px;
    border-bottom:1px solid #23262e; background:#14161c;
  }
  #log{
    flex:1; overflow-y:auto; padding:16px; display:flex; flex-direction:column; gap:10px;
  }
  .msg{max-width:80%; padding:10px 14px; border-radius:14px; line-height:1.4; white-space:pre-wrap;}
  .user{align-self:flex-end; background:#3b82f6; color:white; border-bottom-right-radius:4px;}
  .nova{align-self:flex-start; background:#23262e; border-bottom-left-radius:4px;}
  form{
    display:flex; gap:8px; padding:12px; border-top:1px solid #23262e; background:#14161c;
  }
  input{
    flex:1; padding:12px 14px; border-radius:20px; border:1px solid #2c303a;
    background:#1a1d24; color:#e6e6e6; font-size:15px; outline:none;
  }
  button{
    padding:0 18px; border-radius:20px; border:none; background:#3b82f6;
    color:white; font-weight:600; font-size:15px;
  }
  button:disabled{opacity:0.5;}
</style>
</head>
<body>
  <header>NOVA</header>
  <div id="log"></div>
  <form id="f">
    <input id="m" autocomplete="off" placeholder="Message NOVA..." />
    <button type="submit">Send</button>
  </form>
<script>
  const log = document.getElementById('log');
  const form = document.getElementById('f');
  const input = document.getElementById('m');

  function addMsg(text, who){
    const el = document.createElement('div');
    el.className = 'msg ' + who;
    el.textContent = text;
    log.appendChild(el);
    log.scrollTop = log.scrollHeight;
  }

  form.addEventListener('submit', async (e) => {
    e.preventDefault();
    const text = input.value.trim();
    if(!text) return;
    addMsg(text, 'user');
    input.value = '';
    input.disabled = true;

    try{
      const res = await fetch('/chat', {
        method: 'POST',
        headers: {'Content-Type':'application/json'},
        body: JSON.stringify({message: text})
      });
      const data = await res.json();
      addMsg(data.message || data.error || '(no response)', 'nova');
    }catch(err){
      addMsg('Error: could not reach NOVA.', 'nova');
    }
    input.disabled = false;
    input.focus();
  });
</script>
</body>
</html>"""


class NovaHandler(BaseHTTPRequestHandler):

    def send_json(self, data, status=200):
        body = json.dumps(data, ensure_ascii=False).encode("utf-8")

        self.send_response(status)
        self.send_header("Content-Type", "application/json; charset=utf-8")
        self.send_header("Content-Length", str(len(body)))
        self.end_headers()

        self.wfile.write(body)

    def send_html(self, html, status=200):
        body = html.encode("utf-8")

        self.send_response(status)
        self.send_header("Content-Type", "text/html; charset=utf-8")
        self.send_header("Content-Length", str(len(body)))
        self.end_headers()

        self.wfile.write(body)

    def do_GET(self):
        if self.path == "/":
            self.send_html(CHAT_PAGE)
        elif self.path == "/status":
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
    print("GET  /        chat bar UI")
    print("GET  /status  health check")
    print("POST /chat    send a message")
    print("Press CTRL+C to stop.")
    print("=" * 40)

    server = HTTPServer((HOST, PORT), NovaHandler)

    try:
        server.serve_forever()
    except KeyboardInterrupt:
        print("\nNOVA API stopped.")
        server.server_close()
