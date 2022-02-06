# A very basic http server that accepts POST http requests and invokes ML algorithm with request's input
# and then returns ML response
# inspired by 'https://gist.github.com/rochacbruno/f444466f06ecf88085ab363105d4c505'

from http.server import HTTPServer, BaseHTTPRequestHandler

import json
import labelizer_engine as engine
import dico as dico_api


class ServerHandler(BaseHTTPRequestHandler):
    
    def _set_headers(self):
        self.send_response(200)
        self.send_header("Content-type", "text/text")
        self.end_headers()
    

    def _html(self, message):
        """
            Encode the message to send as response.
        """
        return message.encode("utf8")  # NOTE: must return a bytes object!
    
    def do_GET(self):
        self._set_headers()
        self.wfile.write(self._html("hi from docker engine!"))

    def do_POST(self):
        content_length = int(self.headers['Content-Length']) # <--- Gets the size of data
        text = self.rfile.read(content_length).decode('utf-8') # <--- Gets the data itself

        #print (f"TEXT::: '{text}'")

        dico = dico_api.loadDico()
        themes = dico_api.computeThemeOccurences(text, dico)

        if (sum(themes) == 0): tag='Unrecognized text content. Plase provide some known words.'
        else: tag = engine.get_label(dico_api.generateTrainSet(dico), themes)

        self._set_headers()
        self.wfile.write(self._html(tag))


def run(server_class=HTTPServer, handler_class=ServerHandler, addr="0.0.0.0", port=4000):
    server_address = (addr, port)
    httpd = server_class(server_address, handler_class)

    print(f"Starting httpd server on {addr}:{port}")
    httpd.serve_forever()


if __name__ == "__main__":
    run()
