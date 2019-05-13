import Sqlite


def iniTagVector(id):
    vector = [0, 0, 0, 0, 0, 0, 0]
    tags = Sqlite.recuperarEtiquetas(str(id))
    for tagger in tags:
        for tag in tagger:
            try:
                tag = int(tag)
                if (tag == 0):
                    vector[0] = 1
                if (tag == 1):
                    vector[1] = 1
                if (tag == 2):
                    vector[2] = 1
                if (tag == 3):
                    vector[3] = 1
                if (tag == 4):
                    vector[4] = 1
                if (tag == 5):
                    continue
                    #vector[4] = 1
                if (tag == 6):
                    vector[5] = 1
                if (tag == 7):
                    vector[5] = 1
                if (tag == 8):
                    vector[5] = 1
                if (tag == 9):
                    vector[6] = 1
            except:
                continue

    return vector

def vectorComparisonTweet(tweet):
    clasificado = tweet[2]
    etiquetado = tweet[3]
    cont = 0
    for i in [0,1,2,3,4,5,6]:
        if clasificado[i] == etiquetado[i]:
            cont = cont + 1
    res = (cont/7) * 100
    return res

def vectorComparisonAllTweets(tweetList):
    numTweets = len(tweetList)
    numEtiquetas = numTweets * 7  #6 es el numero de etiquetas que hay
    cont = 0
    for tweet in tweetList:
        clasificado = tweet[2]
        etiquetado = tweet[3]
        for i in [0,1,2,3,4,5,6]:
            if clasificado[i] == etiquetado[i]:
                cont = cont + 1
    res = (cont/numEtiquetas) * 100
    print("** El nivel de acuerdo total es de un " + str(res) + "%")

def precisionAndRecall(tweetList):
    fn = [0, 0, 0, 0, 0, 0, 0]
    fp = [0, 0, 0, 0, 0, 0, 0]
    vp = [0, 0, 0, 0, 0, 0, 0]
    vn = [0, 0, 0, 0, 0, 0, 0]
    for tweet in tweetList:
        #print(tweetList)
        #print(tweet)
        tagsFiltro = tweet[2]

        tagsOriginales = tweet[3]
        #print(tagsOriginales)
        #print(tagsFiltro)
        #print("----------------")
        listSize = len(tweetList)

        for i in [0, 1, 2, 3, 4, 5, 6]:
            if tagsFiltro[i] == 1 and tagsOriginales[i] == 1:
                vp[i] += 1
            elif tagsFiltro[i] == 0 and tagsOriginales[i] == 0:
                vn[i] += 1
            elif tagsFiltro[i] == 1 and tagsOriginales[i] == 0:
                fp[i] += 1
            elif tagsFiltro[i] == 0 and tagsOriginales[i] == 1:
                fn[i] += 1
    print("-------------")
    print("Falsos negativos --> " + str(fn))
    print("Falsos positivos --> " + str(fp))
    print("Verdaros Negativos --> " + str(vn))
    print("Verdaderos positivos --> " + str(vp))

    print("-------------")
    for f in [0,1,2,3,4,5,6]:

        precision = vp[f]/(vp[f] + fp[f])
        recall = vp[f]/(vp[f] + fn[f])
        acierto = ((vp[f] + vn[f])/ listSize) * 100
        media_harmonica = 2*((precision * recall)/(precision+recall))


        print("Para la clase " + str(f) + " Precision = " + str(precision) + ", Recall = " + str(recall) + ", Acierto = " + str(acierto) + "%, Media Harmonica = " + str(media_harmonica) )

        print()


'''''with open("/Users/victorbotti/Desktop/categorizar.json", 'r') as fichero:
    lista = []
    for line in fichero:
    #print(cont)
        line = eval(line)
        lista.append(line)
    #lista = lista[:20]
    precisionAndRecall(lista)
'''''






