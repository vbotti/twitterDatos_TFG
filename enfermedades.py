import utils

def enfermedades(tweetList):
    with open("diccionarios/enfermedades.txt", 'r') as fichero:
        cont = fichero.read()
        arr = eval(cont)
        fichero.close()
        listaEnfermedades = arr

        setB = set(listaEnfermedades)

    for tweet in tweetList:
        tweetText = tweet[1]
        lista = utils.tweet_clean(tweetText)
        setA = set(lista)

        common = setA.intersection(setB)

        if common:
            tweet[2][1] = 1

    return tweetList
