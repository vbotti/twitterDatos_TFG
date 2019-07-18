import datosPersonalesIdentificables
import drogas
import detallesDeRelacion
import enfermedades
import insultos
import Spacy
import tf_server
import Usuario
import youtubeLinkScrapper
import csv
from nostril import nonsense

import json
import re
listUsers = []


with open("/Users/victorbotti/Desktop/scripts/Thursday_July_18_2019.json", 'r') as fichero:
    AllUsersJSON = json.load(fichero)
    fichero.close()
    for userJSON in AllUsersJSON:
            username = userJSON["username"]
            userID = userJSON['userID']
            message = [[userID, userJSON["message"], [0,0,0,0,0,0]]]
            aux = True
            #print(userJSON["username"] + " " + userJSON["message"])



            for x in listUsers:
                if x.id == userID:
                    user = x
                    aux = False



            if aux:
                user = Usuario.Usuario(username, userID)
            user.sumaTotal()
            try:
                #print(userJSON["message"])
                if userJSON["message"] == "":
                    user.sumaImagenes()
                elif len(userJSON["message"]) < 6:
                    user.sumaSpam()
                elif nonsense(userJSON["message"]):
                    user.sumaSpam()
                else:
                    message = Spacy.getLocations(message)
                    message = enfermedades.enfermedades(message)
                    message = drogas.drogas(message)
                    message = tf_server.sentimentAnalysis(message)
                    message = detallesDeRelacion.relaciones(message)
                    message = datosPersonalesIdentificables.datos(message)
                    message = insultos.insultos(message)
                    youtubeLinkScrapper.youtubeVideo(userJSON["message"], user)

                    for x in [0,1,2,3,4,5]:
                        if message[0][2][x] == 1:
                            if x == 0:
                                user.sumaUbicación()
                            if x == 1:
                                user.sumaSalud()
                            if x == 2:
                                user.sumaDrogas()
                            if x == 3:
                                user.sumaSentiment()
                            if x == 4:
                                user.sumaInsultos()
                            if x == 5:
                                user.sumaDetallesPersonales()
            except:
                user.sumaSpam()

            if aux:
                listUsers.append(user)


with open('usuarios.csv', 'w') as csvfile:
    filewriter = csv.writer(csvfile, delimiter=',',
                            quotechar='|', quoting=csv.QUOTE_MINIMAL)
    filewriter.writerow(['userID', 'Usuario', 'Total mensajes', 'Spam', 'Ubicación', 'Salud', 'Drogas/Alcohol', 'Sentiment Negativo', 'Insultos', 'DetallesPersonales', 'Videos', 'Malos Videos', 'Imagenes/mensaje en blanco'])

    for user in listUsers:
        filewriter.writerow(
            [user.id, user.nombre, user.mensajesTotal, user.spam, user.ubicacion, user.salud, user.drogas, user.sentiment,
             user.insultos, user.detallesPersonales, user.videos, user.malosVideos, user.imagenes_blanco])