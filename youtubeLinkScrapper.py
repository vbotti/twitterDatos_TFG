import requests
import re
import json

import drogas
import enfermedades
import tf_server
import insultos
import Usuario
from nostril import nonsense
APIKey = 'AIzaSyAoqtFFwPZo9d4eBwyg2OzjFTl4mKp3-9Y'


def youtubeVideo(text, user):
    videos = re.findall('http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+', text)
    for url in videos:
        try:

            videoID = re.findall('^.*(?<=(=))(?s)(.*$)', url)
            #print(videoID)
            if videoID == []:

                videoID2 = re.findall('^.*(?<=(youtu.be/))(?s)(.*$)', url)
                videoID = videoID2
            #print(videoID)
            url = 'https://www.googleapis.com/youtube/v3/videos?key=' + APIKey + '&fields=items(snippet(title, description))&part=snippet,statistics&id=' + videoID[0][1]
            r = requests.get(url).json()

            title = [[123456, r['items'][0]['snippet']['title'], [0, 0, 0, 0, 0]]] #Posicion 0 --> Ubicacion (no se usa)Posicion 1 --> enfermedades, Pos 2 --> drogas, Pos 3 -->emociones, Pos 4 --> Insultos
            description = [[123456, r['items'][0]['snippet']['description'], [0, 0, 0, 0, 0]]]

            #print(title)
            #print(description)
            user.sumaVideos()
            title = drogas.drogas(title)
            title = enfermedades.enfermedades(title)
            title = tf_server.sentimentAnalysis(title)
            title = insultos.insultos(title)

            description = drogas.drogas(description)
            description = enfermedades.enfermedades(description)
            description = tf_server.sentimentAnalysis(description)
            description = insultos.insultos(description)

            titleVector = title[0][2]
            descriptionVector = description[0][2]
            #print(str(titleVector) + " " + str(descriptionVector))
            for x in [1, 2, 3, 4]:
                if titleVector[x] == 1 or descriptionVector[x] == 1:
                    user.sumaMalosVideos()

        except:
            print("No es un video de YT")


def nosese(text):
    print(len(text))
    if nonsense(text):
        print("nonsense")
    else:
        print("real")

#nosese("Holaaaa")
#youtubeVideo("https://youtu.be/45Mn9rOuA1I")