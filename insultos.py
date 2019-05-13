import utils


def insultos(tweetList):
    with open("diccionarios/insultos.txt", 'r') as fichero:
        cont = fichero.read()
        arr = eval(cont)
        fichero.close()
        listaInsultos = arr

        setB = set(listaInsultos)

    for tweet in tweetList:
        tweetText = tweet[1]
        lista = utils.tweet_clean(tweetText)
        setA = set(lista)

        common = setA.intersection(setB)

        if common:
            tweet[2][4] = 1
    return tweetList
