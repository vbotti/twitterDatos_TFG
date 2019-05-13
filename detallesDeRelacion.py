import utils
import re

emoji_pattern = re.compile("["
                               u"\U0001F618-\U0001F970" 
                               u"\U0001F63B" 
                               u"\U0001F48B-\U0001F5A4"
                               u"\U0001F469-\U0001F9D1"
                               "]+", flags=re.UNICODE)

def relaciones(tweetList):
    with open("diccionarios/relaciones.txt", 'r') as fichero:
        cont = fichero.read()
        arr = eval(cont)
        fichero.close()
        listarelaciones = arr
        setB = set(listarelaciones)

    for tweet in tweetList:
        tweetText = tweet[1]
        lista = utils.tweet_clean(tweetText)
        setA = set(lista)

        common = setA.intersection(setB)


        newTweet = emoji_pattern.sub(r'', tweet[1])

        if common or newTweet != tweet[1]:
            tweet[2][5] = 1

    for tweet in tweetList:
        tweetText = tweet[1]



    return tweetList
