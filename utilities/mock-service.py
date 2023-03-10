import datetime
import hashlib
import hmac
import json
from ast import literal_eval
from http.server import BaseHTTPRequestHandler, HTTPServer
import config
# hostName = "0.0.0.0"
# serverPort = 8887


class WebService(BaseHTTPRequestHandler):
    def do_POST(self):
        self.process_message()

    def do_GET(self):
        self.process_message()

    def respond(self, code, response_message):
        self.send_response(code)
        self.send_header("Content-type", "application/json; charset=utf-8")
        self.end_headers()
        self.wfile.write(response_message.encode(encoding='utf_8'))

    def process_message(self):
        global file
        try:
            file = open('./logs/service.log', 'a')
            timestamp = datetime.datetime.now()
            file.write(f'{timestamp} : {self.path} \n')
            print(f'{timestamp} : {self.path}')
            for h in self.headers:
                # loging headers
                file.write(f'{h}:{self.headers.get(h)} \n')
                # printing headers
                print(f'{h}:{self.headers.get(h)}')

            if 'Content-Length' in self.headers:
                content_len = int(self.headers.get('Content-Length'))
                message = literal_eval(self.rfile.read(content_len).decode('utf-8'))
                json_message = json.dumps(message, indent=4, sort_keys=False)
                # logging request body
                file.write(f'{json_message} \n')
                # printing request body
                print(f'{json_message}')

            # handling reqeust to /sign-in endpoint
            if self.path == '/sign-in':
                print('Login request')
                # getting response
                jsonfile = open('./test-data/sign-in-resp.json')
                data = json.load(jsonfile)
                # sending response
                self.respond(401, json.dumps(data))
        except Exception as e:
            print(f'Exception while processing the request: {e}')
        finally:
            file.close()


if __name__ == "__main__":
    # getting host and port configurations
    hostName = config.get()['MOCK_SERVICE']['hostName']
    serverPort = config.get()['MOCK_SERVICE']['serverPort']

    webServer = HTTPServer((hostName, serverPort), WebService)
    print("WebService server started http://%s:%s" % (hostName, serverPort))

    try:
        webServer.serve_forever()
    except KeyboardInterrupt:
        pass

    webServer.server_close()
    print("WebService server stopped.")
