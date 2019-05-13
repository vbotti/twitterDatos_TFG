from classifier import SentimentClassifier
import Sqlite
import fleissKappaMaximo
from matplotlib import pyplot
from matplotlib.font_manager import FontProperties
import traductor
from nltk.sentiment.vader import SentimentIntensityAnalyzer
import re
from string import punctuation

def sentimientoYKappa():
    clf = SentimentClassifier()
    PoorAgreement = 0
    SlightAgreement = 0
    FairAgreement = 0
    ModerateAgreement = 0
    SubstantialAgreement = 0
    AlmostPerfectAgreement = 0
    contador = 0
    with open("/Users/victorbotti/Desktop/BD_sqlite/categorias/TweetsCategoria3.json", 'r') as fichero:
        cont = fichero.read()
        arr = eval(cont)
        lista = arr
        print(len(lista))

    f = open('/Users/victorbotti/Desktop/sentimentKappaMaximosAllTweets.txt', 'a')
    for tweet in lista:
        # print("///////////////////////")
        texto = tweet[1]
        sentiment_int = '%.5f' % clf.predict(texto)
        sentiment_int = float(sentiment_int)
        sentiment = texto + ' ==> %.5f' % clf.predict(texto)
        if sentiment_int > 0.25 and sentiment_int < 0.75:
            continue
        # print(sentiment)
        contador += 1
        tags = Sqlite.recuperarEtiquetas(str(tweet[0]))
        kappa = fleissKappaMaximo.kappaConMaximos(tags)
        # print("nivel de acuerdo = " + str(kappa))
        f.write(
            "//////////////////////////// \n" + sentiment + "\n" + str(tags) + "\n" + "Acuerdo: " + str(kappa) + "\n")

        if kappa < 0:
            PoorAgreement += 1
        elif 0.01 <= kappa <= 0.20:
            SlightAgreement += 1
        elif 0.21 <= kappa <= 0.40:
            FairAgreement += 1
        elif 0.41 <= kappa <= 0.60:
            ModerateAgreement += 1
        elif 0.61 <= kappa <= 0.80:
            SubstantialAgreement += 1
        elif 0.81 <= kappa <= 1:
            AlmostPerfectAgreement += 1

    pyplot.bar([1], [PoorAgreement], label="PoorAgreement", color='red')
    pyplot.bar([2], [SlightAgreement], label="SlightAgreement", color='blue')
    pyplot.bar([3], [FairAgreement], label="FairAgreement", color='yellow')
    pyplot.bar([4], [ModerateAgreement], label="ModerateAgreement", color='gray')
    pyplot.bar([5], [SubstantialAgreement], label="SubstantialAgreement", color='green')
    pyplot.bar([6], [AlmostPerfectAgreement], label="AlmostPerfectAgreementt", color='brown')
    fontP = FontProperties()
    fontP.set_size('small')
    pyplot.legend(prop=fontP)

    pyplot.xlabel("Acuerdo")
    pyplot.ylabel("Num Tweets")
    pyplot.title('Grafica de Acuerdo dataset')
    pyplot.savefig('/Users/victorbotti/Desktop/FiguraacuerdoCat3.png')
    print(
        "PoorAgreement " + str(PoorAgreement) + "\n" +
        "SlightAgreemen " + str(SlightAgreement) + "\n" +
        "FairAgreement " + str(FairAgreement) + "\n" +
        "ModerateAgreemen " + str(ModerateAgreement) + "\n" +
        "SubstantialAgreement " + str(SubstantialAgreement) + "\n" +
        "AlmostPerfectAgreement " + str(AlmostPerfectAgreement) + "\n" +
        "contador" + str(contador)
    )

    f.close()


def sentiment(tweetList):
    clf = SentimentClassifier()
    for tweet in tweetList:
        texto = tweet[1]
        sentiment_int = '%.5f' % clf.predict(texto)
        sentiment_int = float(sentiment_int)
        if sentiment_int <= 0.25 or sentiment_int >= 0.75:
            tweet[2][3] = 1
    return tweetList
    # print(tweet)
    # print(sentiment)

def sentimentIngles(tweetList):
    sid = SentimentIntensityAnalyzer()
    for tweet in tweetList:
        tweetText = re.sub(r'@\w*', '', tweet[1])
        tweetText = re.sub(r'#\w*', '', tweetText)
        tweetText = re.sub(r'RT\w*', '', tweetText)
        tweetText = re.sub(r'#\w*', '', tweetText)
        tweetText = re.sub(r'[' + punctuation.replace('@', '') + ']+', ' ', tweetText)
        tweetText = re.sub(r'…\w*', '', tweetText)
        tweetText = re.sub(r'[^\w]', ' ', tweetText)

        text = traductor.translate(tweetText)
        #print(text.text)
        ss = sid.polarity_scores(text.text)
        list = []
        for k in ss:
            list.append('{1}'.format(k, ss[k]))
        #print(str(list))
        '''print()
        print(tweet[1])
        print(text)
        print(list[3])'''
        if (abs(float(list[3])) > abs(0.5)):
            #print("true")
            tweet[2][3] = 1

    return tweetList
