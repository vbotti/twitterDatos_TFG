import math

cont0 = 0
cont1 = 0
cont2 = 0
cont3 = 0
cont4 = 0
cont5 = 0
cont6 = 0
cont7 = 0
cont8 = 0
cont9 = 0
catMax = 0
totalRaters = 0


def categoriaMaxima(tags):
    listaNums= []
    listaNumsNoRep =[]
    listaFinal = []
    max = 0
    global catMax
    for tag in tags:
        if '' in tag:
            continue
        if ',' in tag:
            x = tag.split(',')
            for num in x:
                listaNums.append(int(num))
        else:
            listaNums.append(int(tag))
    listaNumsNoRep = set(listaNums)
    for num in listaNumsNoRep:
        cont = listaNums.count(num)
        if cont > max:
            max = cont
            catMax = num
    return catMax
    print(catMax)


def defecto():
    global cont0, cont1,cont2,cont3,cont4,cont5,cont6,cont7,cont8,cont9,totalRaters, catMax
    cont0 = 0
    cont1 = 0
    cont2 = 0
    cont3 = 0
    cont4 = 0
    cont5 = 0
    cont6 = 0
    cont7 = 0
    cont8 = 0
    cont9 = 0
    totalRaters = 0


def kappaConMaximos(raters):
    defecto()
    categoriaMaxima(raters)
    global totalRaters
    global catMax
    for rater in raters:
        if "," in rater:
            maximoKappa(rater)
            totalRaters += 1

        elif "0" in rater:
            global cont0
            cont0 += 1
            totalRaters += 1

        elif "1" in rater:
            global cont1
            cont1 += 1
            totalRaters += 1

        elif "2" in rater:
            global cont2
            cont2 += 1
            totalRaters += 1

        elif "3" in rater:
            global cont3
            cont3 += 1
            totalRaters += 1

        elif "4" in rater:
            global cont4
            cont4 += 1
            totalRaters += 1

        elif "5" in rater:
            global cont5
            cont5 += 1
            totalRaters += 1

        elif "6" in rater:
            global cont6
            cont6 += 1
            totalRaters += 1

        elif "7" in rater:
            global cont7
            cont7 += 1
            totalRaters += 1

        elif "8" in rater:
            global cont8
            cont8 += 1
            totalRaters += 1

        elif "9" in rater:
            global cont9
            cont9 += 1
            totalRaters += 1

    if totalRaters == 1: return 1
    if totalRaters == 0: return 0

    P = 1/(totalRaters*(totalRaters-1)) * ((pow(cont0, 2) + pow(cont1, 2) + pow(cont2, 2) + pow(cont3, 2) + pow(cont4, 2 ) + pow(cont5, 2) + pow(cont6, 2)
                                           + pow(cont7, 2) + pow(cont8, 2) + pow(cont9, 2) - totalRaters))
    #print(cont0 , cont1 ,cont2 ,cont3 ,cont4 , cont5 ,cont6 , cont7 ,cont8 ,cont9)
    #print(totalRaters)
    return P

def maximoKappa(rater):
    global totalRaters
    global cont0, cont1, cont2, cont3, cont4, cont5, cont6, cont7, cont8, cont9, catMax
    #print(peso)
    if str(catMax) in rater:
        if catMax == 0:
            cont0 += 1
        elif catMax == 1:
            cont1 += 1
        elif catMax == 2:
            cont2 += 1
        elif catMax == 3:
            cont3 += 1
        elif catMax == 4:
            cont4 += 1
        elif catMax == 5:
            cont5 += 1
        elif catMax == 6:
            cont6 += 1
        elif catMax == 7:
            cont7 += 1
        elif catMax == 8:
            cont8 += 1
        elif catMax == 9:
            cont9 += 1
    else:
        x = rater.split(",")
        val = int(x[0])
        if val == 0:
            cont0 += 1
        elif val == 1:
            cont1 += 1
        elif val == 2:
            cont2 += 1
        elif val == 3:
            cont3 += 1
        elif val == 4:
            cont4 += 1
        elif val == 5:
            cont5 += 1
        elif val == 6:
            cont6 += 1
        elif val == 7:
            cont7 += 1
        elif val == 8:
            cont8 += 1
        elif val == 9:
            cont9 += 1




#kappaConMaximos(['1,2,3','2,3,4','2,5,6,7','9,8'])