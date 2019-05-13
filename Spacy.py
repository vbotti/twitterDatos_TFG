import spacy
import re
from string import punctuation


# from googletrans import Translator

# translator = Translator()


def getAll():
    nlp = spacy.load('es_core_news_sm')
    with open("/Users/victorbotti/Desktop/BD_sqlite/categorias/TweetsCategoria0.json", 'r') as fichero:
        cont = fichero.read()
        arr = eval(cont)
        listaTweets = arr
    for tweett in listaTweets:
        tweet = re.sub(r'@\w*', '', tweett[1])
        tweet = re.sub(r'RT\w*', '', tweet)
        tweet = re.sub(r'#\w*', '', tweet)
        tweet = re.sub(r'[' + punctuation.replace('@', '') + ']+', ' ', tweet)
        tweet = re.sub(r'…\w*', '', tweet)
        tweet = re.sub(r'[^\w]', ' ', tweet)
        tweet = re.sub(r'https', '', tweet)
        tweet = re.sub(r'http', '', tweet)
        # tweet = translator.translate(tweet).text
        doc = nlp(tweet)
        tags = {}
        print("////////////////////")
        print(tweett)
        for ent in doc.ents:
            print(ent.text, ent.start_char, ent.end_char, ent.label_)
            term = ' '.join(t.orth_ for t in ent)
            if ' '.join(term) not in tags:
                tags[term] = [(ent.label, ent.label_)]
            else:
                tags[term].append((ent.label, ent.label_))


def getLocations(tweetList):

    nlp = spacy.load('es')

    for tweet in tweetList:

        tweetText = re.sub(r'@\w*', '', tweet[1])
        tweetText = re.sub(r'#\w*', '', tweetText)
        tweetText = re.sub(r'RT\w*', '', tweetText)
        tweetText = re.sub(r'#\w*', '', tweetText)
        tweetText = re.sub(r'[' + punctuation.replace('@', '') + ']+', ' ', tweetText)
        tweetText = re.sub(r'…\w*', '', tweetText)
        tweetText = re.sub(r'[^\w]', ' ', tweetText)

        doc = nlp(tweetText)
        tags = {}

        for ent in doc.ents:
            if ent.label_ == 'LOC' or ent.label_ == 'GPE':
                tweet[2][0] = 1
                continue

    return tweetList
