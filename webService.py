from http.server import BaseHTTPRequestHandler, HTTPServer
import time
import json
import Spacy
import enfermedades
import drogas
import SentimentAnalysis
import insultos
import datosPersonalesIdentificables
import detallesDeRelacion
import tf_server

class S(BaseHTTPRequestHandler):
    def _set_headers(self):
        self.send_response(200)
        self.send_header('Content-type', 'application/json')
        self.end_headers()

    def _send_cors_headers(self):
        """ Sets headers required for CORS """
        self.send_header("Access-Control-Allow-Origin", "*")
        self.send_header("Access-Control-Allow-Methods", "GET,POST,OPTIONS")
        self.send_header("Access-Control-Allow-Headers", "x-api-key,Content-Type")

    def do_HEAD(self):
        self._set_headers()

    def do_OPTIONS(self):
        self.send_response(200)
        self._send_cors_headers()
        self.end_headers()

    def do_POST(self):
        self.send_response(200)
        self._send_cors_headers()
        self.send_header("Content-Type", "application/json")
        self.end_headers()
        content_len = int(self.headers.get('content-length', 0))
        post_body = self.rfile.read(content_len)

        post_body = post_body.decode('utf-8')
        msg_extracted = json.loads(post_body)

        lista = [[123456, msg_extracted['text'], [0, 0, 0, 0, 0, 0, 0]]]
        lista = Spacy.getLocations(lista)
        lista = enfermedades.enfermedades(lista)
        lista = drogas.drogas(lista)
        #lista = SentimentAnalysis.sentiment(lista)
        lista = tf_server.sentimentAnalysis(lista)
        lista = insultos.insultos(lista)
        lista = detallesDeRelacion.relaciones(lista)
        lista = datosPersonalesIdentificables.datos(lista)
        if msg_extracted['type'] == "categories":
            print(lista)
            vectorCategorias = [0,1,2,3,4,5,6]
            categorias_encontradas = "Se está revelando información sensible del tipo: "
            for tweet in lista:
                if all(v == 0 for v in tweet[2]):
                    tweet[2][6] = 1
                    self.wfile.write(bytes(' ', "utf-8"))
                else:
                    for x in vectorCategorias:
                        if tweet[2][x] == 1:
                            if x == 0:
                                categorias_encontradas += "Ubicación,"
                            elif x == 1:
                                categorias_encontradas += "Enfermedades,"
                            elif x == 2:
                                categorias_encontradas += "Drogas,"
                            elif x == 3:
                                categorias_encontradas += "Emociones,"
                            elif x == 4:
                                categorias_encontradas += "Insultos,"
                            elif x == 5:
                                categorias_encontradas += "Detalles personales,"
                            elif x == 6:
                                categorias_encontradas += "Neutro"

                    self.wfile.write(bytes(categorias_encontradas, "utf-8"))
        elif msg_extracted['type'] == "sensible" :
            print(lista)
            vectorCategorias = [0, 1, 2, 3, 4, 5, 6]
            sensibilidad = 0
            for tweet in lista:
                if all(v == 0 for v in tweet[2]):
                    tweet[2][6] = 1
                    self.wfile.write(bytes(' ', "utf-8"))
                else:
                    for x in vectorCategorias:
                        if tweet[2][x] == 1:
                            if x == 0:
                                sensibilidad += 0.5
                            elif x == 1:
                                sensibilidad += 0.3
                            elif x == 2:
                                sensibilidad += 0.4
                            elif x == 3:
                                sensibilidad += 0.2
                            elif x == 4:
                                sensibilidad += 0.6
                            elif x == 5:
                                sensibilidad += 0.8
                            elif x == 6:
                                sensibilidad += 0

                    if sensibilidad == 0.0:
                        sensibilidad_encontrada = "El grado de sensibilidad en el mensaje es nulo"
                    elif 0 > sensibilidad <= 4.0:
                        sensibilidad_encontrada = "El grado de sensibilidad en el mensaje es bajo"
                    elif 4.0 > sensibilidad <= 6.0:
                        sensibilidad_encontrada = "El grado de sensibilidad en el mensaje es medio"
                    elif sensibilidad > 6.0:
                        sensibilidad_encontrada = "El grado de sensibilidad en el mensaje es alto"

                    self.wfile.write(bytes(sensibilidad_encontrada, "utf-8"))


    #app.run(host='localhost', port=5000)

HOST_NAME = '0.0.0.0'
PORT_NUMBER = 80

server_class = HTTPServer
httpd = HTTPServer(('', PORT_NUMBER), S)

print(time.asctime(), "Server Starts - %s:%s" % (HOST_NAME, PORT_NUMBER))
try:
	httpd.serve_forever()
except KeyboardInterrupt:
	pass
httpd.server_close()
print(time.asctime(), "Server Stops - %s:%s" % (HOST_NAME, PORT_NUMBER))