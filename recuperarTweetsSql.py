import Sqlite
import json

def seleccionarPorEtiquetas(): #Obtiene todos los tweets que tengan una cierta etiqueta
    idTweetsSql = Sqlite.sqliteFuncionListas("Select id, text from collector_tweet")
    tags = Sqlite.sqliteFuncion("Select tweet_id from tagger_tweettag where tags like '%9%'")
    l = []
    for tweet in idTweetsSql:
        if str(tweet[0]) in tags:
            l.append(tweet)
    f = open ("/Users/victorbotti/Desktop/BD_mongo/categorias_texto/9_tweetsNeutral.json",'w')
    f.write(str(l))
    f.close()

def getAllTweets():
    idTweetsSql = Sqlite.sqliteFuncionListas("Select id, text from collector_tweet")
    l = []
    for tweet in idTweetsSql:
        l.append(tweet)
    f = open ("/Users/victorbotti/Desktop/BD_sqlite/allTweets.json",'w')
    f.write(str(l))
    f.close()

def filtradoPorEtiquetas(): #Se le pasan todos los tweets, y los guarda en ficheros según su etiquetas. Debe de estar etiquetado 3+ para guardarse
    idTweetsSql = Sqlite.sqliteFuncionListas("Select id, text from collector_tweet")
    listaCat0=[]
    listaCat1=[]
    listaCat2=[]
    listaCat3=[]
    listaCat4=[]
    listaCat5=[]
    listaCat6=[]
    listaCat7=[]
    listaCat8=[]
    listaCat9=[]

    devuelveLista = {
        0: listaCat0,
        1: listaCat1,
        2: listaCat2,
        3: listaCat3,
        4: listaCat4,
        5: listaCat5,
        6: listaCat6,
        7: listaCat7,
        8: listaCat8,
        9: listaCat9
    }


    for tweet in idTweetsSql: #tweet[0] --> id, tweet[1] --> texto

        id = str(tweet[0])
        etiquetas = Sqlite.recuperarEtiquetas(id)
        etiquetastotal = []
        etiquetastotalnorep=[]
        listaTuplas = []
        for tag in etiquetas:
            if '' == tag:
                continue
            if "," in str(tag):
                x = tag.split(",")
                for num in x:
                    etiquetastotal.append(int(num))
            else:
                etiquetastotal.append(int(tag))
        if(len(etiquetastotal) == 0): continue
        etiquetastotalnorep = set(etiquetastotal)
        for tag in etiquetastotalnorep:
            cont = etiquetastotal.count(tag)
            cat = tag
            t = (cat, cont)
            listaTuplas.append(t)

        for tupla in listaTuplas:
            if tupla[1] >= 3:
                tweetinsertar = [id, str(tweet[1])]
                l = devuelveLista.get(tupla[0])
                l.append(tweetinsertar)

    f = open("/Users/victorbotti/Desktop/BD_sqlite/categorias/TweetsCategoria0.json", 'a')
    f.write(str(listaCat0))
    f.close()
    f = open("/Users/victorbotti/Desktop/BD_sqlite/categorias/TweetsCategoria1.json", 'a')
    f.write(str(listaCat1))
    f.close()
    f = open("/Users/victorbotti/Desktop/BD_sqlite/categorias/TweetsCategoria2.json", 'a')
    f.write(str(listaCat2))
    f.close()
    f = open("/Users/victorbotti/Desktop/BD_sqlite/categorias/TweetsCategoria3.json", 'a')
    f.write(str(listaCat3))
    f.close()
    f = open("/Users/victorbotti/Desktop/BD_sqlite/categorias/TweetsCategoria4.json", 'a')
    f.write(str(listaCat4))
    f.close()
    f = open("/Users/victorbotti/Desktop/BD_sqlite/categorias/TweetsCategoria5.json", 'a')
    f.write(str(listaCat5))
    f.close()
    f = open("/Users/victorbotti/Desktop/BD_sqlite/categorias/TweetsCategoria6.json", 'a')
    f.write(str(listaCat6))
    f.close()
    f = open("/Users/victorbotti/Desktop/BD_sqlite/categorias/TweetsCategoria7.json", 'a')
    f.write(str(listaCat7))
    f.close()
    f = open("/Users/victorbotti/Desktop/BD_sqlite/categorias/TweetsCategoria8.json", 'a')
    f.write(str(listaCat8))
    f.close()
    f = open("/Users/victorbotti/Desktop/BD_sqlite/categorias/TweetsCategoria9.json", 'a')
    f.write(str(listaCat9))
    f.close()


#filtradoPorEtiquetas()
getAllTweets()



"""miMongo = pymongo.MongoClient("mongodb://localhost:27017/")      #
mydb = miMongo["TwitterDataSets"]                                # Base de Datos donde se van a copiar los datos
mycol = mydb["tweets_Completo"]

tweetsMongo = mycol.find({}, {'_id': 0})
l = []
listaIds=[]
for tweet in tweetsMongo:
    if tweet['id_str'] in idTweetsSql:
        if tweet['id_str'] not in listaIds:
            l.append(tweet)
            listaIds.append(tweet['id_str'])
            
with open("/Users/victorbotti/Desktop/BD_mongo/categorias_texto/1_tweetsSalud.json", "w") as outfile:
    json.dump(l, outfile)
"""""

