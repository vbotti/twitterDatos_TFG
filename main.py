import Spacy
import enfermedades
import drogas
import SentimentAnalysis
import insultos
import datosPersonalesIdentificables
import detallesDeRelacion
import tagVectorComparison
from time import time

Inicio = time()

with open("/Users/victorbotti/Desktop/BD_sqlite/allTweets.json", 'r') as fichero:
    cont = fichero.read()
    arr = eval(cont)
    lista = arr
    for tweet in lista:
        #tweet.append([0,0,0,0,0,0,0,0,0,0])
        tweet.append([0, 0, 0, 0, 0, 0, 0])
        tweet.append(tagVectorComparison.iniTagVector(tweet[0]))
    #lista = lista[:20]

termina_cargaDatos = time() - Inicio
print("Termina la carga de datos: " + str(termina_cargaDatos))

inicio_Spacy = time()
lista = Spacy.getLocations(lista)
termina_Spacy = time() - inicio_Spacy
print("Tiempo localización: " + str(termina_Spacy))

inicio_enfermedades = time()
lista = enfermedades.enfermedades(lista)
termina_enfermedades = time() - inicio_enfermedades
print("tiempo salud: " + str(termina_enfermedades))

inicio_drogas = time()
lista = drogas.drogas(lista)
termina_drogas = time() - inicio_drogas
print("tiempo drogas: " + str(termina_drogas))

inicio_sentiment = time()
lista = SentimentAnalysis.sentiment(lista)
termina_sentiment = time() - inicio_sentiment
print("tiempo sentiment: " + str(termina_sentiment))

inicio_insultos = time()
lista = insultos.insultos(lista)
termina_insultos = time() - inicio_insultos
print("tiempo insultos: "+ str(termina_insultos))

inicio_relacion = time()
lista = detallesDeRelacion.relaciones(lista)
termina_relacion = time() - inicio_relacion
print("tiempo detalles de relación: " + str(termina_relacion))

inicio_personales = time()
lista = datosPersonalesIdentificables.datos(lista)
termina_personales = time() - inicio_personales
print("tiempo datos personales: " + str(termina_personales))

for tweet in lista:
    if all(v == 0 for v in tweet[2]):
        tweet[2][6] = 1

    #acuerdo = tagVectorComparison.vectorComparisonTweet(tweet)
    #tweet.append("Nivel de acuerdo = " + str(acuerdo) + "%")
    # print(lista)

tagVectorComparison.precisionAndRecall(lista)
f = open("/Users/victorbotti/Desktop/categorizar.json", "w")
for element in lista:
    f.write(str(element) + "\n")
f.close()

print("tiempo total " + str((time() - Inicio)))