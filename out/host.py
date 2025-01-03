from http.server import SimpleHTTPRequestHandler, HTTPServer
import urllib.parse


class ResultHandler(SimpleHTTPRequestHandler):
    def do_GET(self):
        if self.path.startswith("/results"):
            # Parsowanie parametrów URL
            query_components = urllib.parse.parse_qs(
                urllib.parse.urlparse(self.path).query
            )
            data = query_components.get("data", ["Brak danych"])[0].split(",")

            self.send_response(200)
            self.send_header("Content-type", "text/html")
            self.end_headers()
            html_content = """
            <!DOCTYPE html>
            <html lang="en">
            <head>
                <meta charset="UTF-8">
                <meta name="viewport" content="width=device-width, initial-scale=1.0">
                <title>Raport</title>
            </head>
            <body>
            <style>
            body {
            background-color: #121212;
            color: #ffffff;
            font-family: consolas;
            font-size: 20px;
            }
            .piramid {
                display: flex;
                align-items: center;
                justify-content: center;
                flex-direction: column;
                gap: 5px;
            }
            .footer {
                text-align: center;
                position: fixed;
                bottom: 0;
                width: 100%;
            }
            </style>
            <div class="piramid">
                <h1>Wynik raportu dla - "Odwrócona Piramida":</h1>
            """

            for item in data:
                html_content += f"<div>{item}</div>\n"

            html_content += """
            </div>
            <div class="footer">
                Piotr Dusiński
            </div>
            </body>
            </html>
            """
            self.wfile.write(html_content.encode("utf-8"))
        else:
            # Obsługa innych ścieżek
            super().do_GET()

    def log_message(self, format, *args):
        # Nadpisanie metody log_message, aby wyłączyć logi
        pass


# Uruchomienie serwera
PORT = 8080
server = HTTPServer(("localhost", PORT), ResultHandler)
print(f"Serwer HTTP uruchomiony na porcie {PORT}")
try:
    server.serve_forever()
except KeyboardInterrupt:
    print("Zatrzymywanie serwera...")
    server.server_close()
