import Sqlite

def aplanar_tags(tweetList):
    lista_total_etiquetas = []
    for tweet in tweetList:
        id = tweet[0]
        listaEtiquetas = Sqlite.recuperarEtiquetas(str(id))
        aux = []
        for tag in listaEtiquetas:  # cambio los vectores ['0', '1', '0,2,4', '5']  -->  ['0', '1', '5', '0', '2', '4']
            if "," in tag:
                tags = tag.split(",")
                # print(tags)
                for subTag in tags:
                    aux.append(subTag)
            elif tag == "":
                continue
            else:
                aux.append(tag)
        lista_total_etiquetas.append(aux)
    return lista_total_etiquetas

def acuerdo_por_categoria(tweetList):
    categorias = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    lista_total_etiquetas = aplanar_tags(tweetList)

    for tags in lista_total_etiquetas:
        for tag in tags:

            tag = int(tag)
            if tag == 0:
                categorias[0] += 1
            elif tag == 1:
                categorias[1] += 1
            elif tag == 2:
                categorias[2] += 1
            elif tag == 3:
                categorias[3] += 1
            elif tag == 4:
                categorias[4] += 1
            elif tag == 5:
                categorias[5] += 1
            elif tag == 6:
                categorias[6] += 1
            elif tag == 7:
                categorias[7] += 1
            elif tag == 8:
                categorias[8] += 1
            elif tag == 9:
                categorias[9] += 1

    for x in [0,1,2,3,4,5,6,7,8,9]:
        totalCat = categorias[x]
        totalTweets = len(tweetList)
        raters = 4
        Nxn = totalTweets * raters
        kappa = totalCat/Nxn
        print("\n########################")
        print("El nivel de acuerdo de la clase " + str(x) + " ha sido = " + str(kappa))
        print("Total de veces que se ha seleccionado la categoria " + str(x) + " = " + str(totalCat))
        print("Numero total de tweets = " + str(totalTweets))
        print("Numero total de etiquetadores = " + str(raters))
        print("TotalTweets * raters = " + str(Nxn))


def kappa_por_categoria(tweetList):
    lista_total_etiquetas = aplanar_tags(tweetList)
    list = [[], [], [], [], [], [], [], [], [], []]
    list_neg = [[], [], [], [], [], [], [], [], [], []]
    for i in [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]:
        for tags in lista_total_etiquetas:
            cont = 0
            for tag in tags:
                if str(i) == tag:
                    cont += 1

            list[i].append(cont)
            list_neg[i].append(4-cont)

    Nxn = 4 * len(tweetList)
    for n in [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]:
        sumP2 = 0
        cont1 = 0
        cont2 = 0
        for x in list[n]:
            cont1 += x

        p1_SI = cont1/Nxn

        for i in list_neg[n]:
            cont2 += i

        p1_NO = cont2/Nxn

        Pe = pow(p1_SI, 2) + pow(p1_NO, 2)

        for x in range(len(tweetList)):
            sumP2 += (1/(4*(4-1)))*(pow(list[n][x],2) + pow(list_neg[n][x],2) - 4)

        P = (1/len(tweetList)) * sumP2

        k = (P - Pe)/(1 - Pe)

        PABAK = 2 * P - 1
        print("Para la catagoria " + str(n) + " ha habido un k = " + str(k))
        print("P1_SI " + str(p1_SI))
        print("P1_NO " + str(p1_NO))
        print("Pe " + str(Pe))
        print("sumP2 " + str(sumP2))
        print("P " + str(P))
        print("Pabak =" + str(PABAK))
        print()

    '''csv = ""
    for x in [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]:

        for cat in list[x]:
            csv += str(cat) + ","
        temp = len(csv)
        csv = csv[:temp - 1]
        csv += "\n"

        for cat in list_neg[x]:
            csv += str(cat) + ","
        temp = len(csv)
        csv = csv[:temp - 1]
        csv += "\n"

    f = open("/Users/victorbotti/Desktop/etiquetas.csv", 'w')
    f.write(csv)
    f.close()'''


with open("/Users/victorbotti/Desktop/BD_sqlite/allTweets.json", 'r') as fichero:
    cont = fichero.read()
    arr = eval(cont)
    lista = arr
    fichero.close()

kappa_por_categoria(lista)