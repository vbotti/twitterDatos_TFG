import pymongo
import json

miMongo = pymongo.MongoClient("mongodb://localhost:27017/")      #
mydb = miMongo["TwitterDataSets"]                                # Base de Datos donde se van a copiar los datos
mycol = mydb["tweets_Completo"]                                   #

tweets = mycol.find({},{'_id':0})

with open("/Users/victorbotti/Desktop/BD_mongo/tweetsParaLimpiar.json", "w") as outfile:
    json.dump(list(tweets), outfile)



