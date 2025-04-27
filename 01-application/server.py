from http.server import BaseHTTPRequestHandler, HTTPServer
import socket
import os

HOST, PORT = '', 8000

# Получаем значение переменной окружения AUTHOR или используем значение по умолчанию
AUTHOR = os.getenv('AUTHOR', 'Konstantin Yakovlev')

# Создаем класс обработчика HTTP-запросов, наследуясь от BaseHTTPRequestHandler
class Handler(BaseHTTPRequestHandler):
    def do_GET(self):
        info = f"""
        <html><meta charset="utf-8">
        <body>
        <p>Сервер: {socket.gethostname()}</p>
        <p>IP: {socket.gethostbyname(socket.gethostname())}</p>
        <p>Автор: {AUTHOR}</p>
        </body></html>
        """
        
        self.send_response(200)
        self.send_header('Content-type', 'text/html; charset=utf-8')
        self.end_headers()
        self.wfile.write(info.encode('utf-8'))

# Запускаем сервер
# Выводим информацию о запуске
print(f"Сервер запущен на http://{HOST}:{PORT}")

# Запускаем бесконечный цикл обработки запросов
HTTPServer((HOST, PORT), Handler).serve_forever()