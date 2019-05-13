import utils


def drogas(tweetList):
    with open("diccionarios/drogasYAlcohol.txt", 'r') as fichero:
        cont = fichero.read()
        arr = eval(cont)
        fichero.close()
        listaDrogas = arr

        setB = set(listaDrogas)

    for tweet in tweetList:
        tweetText = tweet[1]
        lista = utils.tweet_clean(tweetText)
        setA = set(lista)

        common = setA.intersection(setB)

        if common:
            tweet[2][2] = 1

    return tweetList
