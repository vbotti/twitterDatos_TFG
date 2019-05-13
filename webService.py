#!flask/bin/python
from flask import Flask
import time
from flask_cors import CORS
from flask import Flask
from flask import request
import Spacy
import enfermedades
import drogas
import SentimentAnalysis
import insultos
import datosPersonalesIdentificables
import detallesDeRelacion
import tagVectorComparison
app = Flask(__name__)
CORS(app)
@app.route('/contentAnalysis', methods=['POST'])
def post():
    start_time = time.time()
    content = request.get_json()
    print(request.remote_addr)
    print(content['text'])
    lista = [[123456, content['text'], [0, 0, 0, 0, 0, 0, 0]]]

    lista = Spacy.getLocations(lista)


    lista = enfermedades.enfermedades(lista)
    lista = drogas.drogas(lista)
    lista = SentimentAnalysis.sentiment(lista)
    lista = insultos.insultos(lista)
    lista = detallesDeRelacion.relaciones(lista)
    lista = datosPersonalesIdentificables.datos(lista)
    for tweet in lista:
        if all(v == 0 for v in tweet[2]):
            tweet[2][6] = 1
            return("")
        else:
            return("Se ha detectado que se esta revelando información sensible, puede cambiar el mensaje si lo desea ")
    elapsed_time = time.time() - start_time
    print(str(elapsed_time))
app.run(host='localhost', port=5000)