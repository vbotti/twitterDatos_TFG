# Funcionalidad: Copiar todos los tweets de una base de datos a otra
import pymongo
import Sqlite

mongoJose = pymongo.MongoClient("gtirouter.dsic.upv.es:27047") #
mydbJose = mongoJose["twdb_vaal"]                           # Base de datos de donde se obtienen los datos
mycolJose = mydbJose["posts"]                                    #

print("Conexion DB josé realizada")

miMongo = pymongo.MongoClient("mongodb://localhost:27017/")      #
mydb = miMongo["TwitterDataSets"]                                # Base de Datos donde se van a copiar los datos
mycol = mydb["tweets_Completo"]                                      #

print("Conexion DB nueva realizada")

idTweetsSql = Sqlite.sqliteFuncion("Select tweet_id From tagger_tweettag")

tweetsMongo = mycolJose.find({}, {'_id': 0})  # Obtenemos los datos sin el ObjectID
for tweet in tweetsMongo:
    if tweet['id_str'] in idTweetsSql:  # Buscar aquellos Tweets que hayan sido etiquetadoss
        mycol.insert_one(tweet)
