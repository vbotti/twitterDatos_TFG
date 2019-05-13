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
totalRaters = 0


def defecto():
    global cont0, cont1,cont2,cont3,cont4,cont5,cont6,cont7,cont8,cont9,totalRaters
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


def kappa(raters):
    defecto()
    global totalRaters
    for rater in raters:

        if "," in rater:
            x = rater.split(",")
            pesosKappa(x)
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

    P = 1/(totalRaters*(totalRaters-1)) * ((pow(cont0, 2) + pow(cont1, 2) + pow(cont2, 2) + pow(cont3, 2) + pow(cont4, 2 ) + pow(cont5, 2) + pow(cont6, 2)
                                           + pow(cont7, 2) + pow(cont8, 2) + pow(cont9, 2) - totalRaters))
    #print(cont0 , cont1 ,cont2 ,cont3 ,cont4 , cont5 ,cont6 , cont7 ,cont8 ,cont9)
    #print(totalRaters)
    return P


def pesosKappa(raters):
    global totalRaters
    lon = len(raters)
    peso = 1/lon
    #print(peso)
    for rater in raters:

        if "0" in rater:
            global cont0
            cont0 += peso

        elif "1" in rater:
            global cont1
            cont1 += peso

        elif "2" in rater:
            global cont2
            cont2 += peso

        elif "3" in rater:
            global cont3
            cont3 += peso

        elif "4" in rater:
            global cont4
            cont4 += peso

        elif "5" in rater:
            global cont5
            cont5 += peso

        elif "6" in rater:
            global cont6
            cont6 += peso

        elif "7" in rater:
            global cont7
            cont7 += peso

        elif "8" in rater:
            global cont8
            cont8 += peso

        elif "9" in rater:
            global cont9
            cont9 += peso

