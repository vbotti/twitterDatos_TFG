import googletrans
import nltk
from nltk.sentiment.vader import SentimentIntensityAnalyzer

def translate(texto):
    gs = googletrans.Translator()
    return gs.translate(texto, "en")



'''sid = SentimentIntensityAnalyzer()

lista = ["Esto es lo mejor que me ha pasado nunca", "Que maravilla", "Esto es horroroso", "mañana no puedo ir"]
list = []
for text in lista:
    text = translate(text)
    print(text.text)

    ss = sid.polarity_scores(text.text)
    list = []
    for k in ss:
        list.append('{1}'.format(k, ss[k]))
    print(str(list))

    if(abs(float(list[3])) > abs(0.5)):
        print("true")
    else:
        print("false")'''