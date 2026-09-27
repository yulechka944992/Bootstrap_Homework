from http.server import BaseHTTPRequestHandler, HTTPServer

hostName = "localhost"  # Адрес для доступа по сети
serverPort = 8080       # Порт для доступа по сети


class MyServer(BaseHTTPRequestHandler):
    """
        Класс, который отвечает за
        обработку входящих запросов от клиентов
    """
    def do_GET(self):
        """ Метод для обработки входящих GET-запросов """
        # Читаем содержимое HTML-файла
        with open("templates/contacts.html", "r", encoding="utf-8") as file:
            html = file.read()

        self.send_response(200)
        self.send_header("Content-type", "text/html; charset=utf-8")
        self.end_headers()
        self.wfile.write(html.encode("utf-8"))


if __name__ == "__main__":
    # Инициализация веб-сервера
    webServer = HTTPServer((hostName, serverPort), MyServer)
    print("Server started http://%s:%s" % (hostName, serverPort))

    try:
        # Старт веб-сервера
        webServer.serve_forever()
    except KeyboardInterrupt:
        # Корректный способ остановить сервер в сочетании клавиш Ctrl + C
        pass

    # Корректная остановка веб-сервера
    webServer.server_close()
    print("Server stopped.")