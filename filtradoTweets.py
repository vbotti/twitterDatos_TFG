# Funcionalidad: Filtrar los tweets para tener solamente los tweets que han sido etiquetados y que aparecen en SQLite3
import pymongo
import Sqlite
import json
import os
from bson import ObjectId
from bson.json_util import loads
from pprint import pprint
import json

idTweetsSql = Sqlite.sqliteFuncion("Select tweet_id From tagger_tweettag")

myclient = pymongo.MongoClient("mongodb://localhost:27017/") # Mi mongoDB
mydb = myclient["TwitterDataSets"]  # Nombre de la base de datos
mycol = mydb[""]  # Base de datos de donde se sacan los Tweets
mycol2 = mydb[""]   # Base de datos donde se copian los Tweets

tweetsMongo = mycol.find({}, {'_id':0})  #Obtener los tweets sin el parameto {'_id': ObjectID('')}

for tweet in tweetsMongo:
    if tweet['id_str'] in idTweetsSql:  # Buscar aquellos Tweets que hayan sido etiquetadoss
        try:
            mycol2.insert_one(tweet)  # insertar
        except:
            print(tweet)
            print(type(tweet))
            break


