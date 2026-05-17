from http.server import HTTPServer, BaseHTTPRequestHandler
import json
from cotacao import buscar_cotacao_dolar

class Handler(BaseHTTPRequestHandler):
    def do_GET(self):
        cotacao = buscar_cotacao_dolar()
        self.send_response(200)
        self.send_header("Content-type", "application/json")
        self.end_headers()
        response = {
            "projeto": "Controle de Estoque Micro",
            "cotacao_dolar": cotacao,
            "status": "online"
        }
        self.wfile.write(json.dumps(response).encode())

    def log_message(self, format, *args):
        pass

if __name__ == "__main__":
    server = HTTPServer(("0.0.0.0", 10000), Handler)
    print("Servidor rodando na porta 10000")
    server.serve_forever()
