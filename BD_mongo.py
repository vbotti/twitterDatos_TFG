import pymongo
import utils
import LDA
import Sqlite
""""miMongo = pymongo.MongoClient("mongodb://localhost:27017/")      #
mydb = miMongo["TwitterDataSets"]                                # Base de Datos donde se van a copiar los datos
mycol = mydb["tweets_Completo"]                                  #

tweet = mycol.find_one({}, {'text': 1, '_id': 0})

x = utils.clean_data_from_json("/Users/victorbotti/Desktop/BD_mongo/tweetsParaLimpiar.json")"""""
lista_tweets = []
dTweetsSql = Sqlite.sqliteFuncionListas("Select id, text from collector_tweet")
for tweet in dTweetsSql:
    texto = tweet[1]
    lista_tweets.append(texto)

x = utils.clean_data_from_list(lista_tweets)
LDA.lda(x)



