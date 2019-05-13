import pymongo
import tweepy

miMongo = pymongo.MongoClient("mongodb://localhost:27017/")      #
mydb = miMongo["TwitterDataSets"]                                # Base de Datos donde se van a copiar los datos
mycol = mydb["tweetsFiltrados"]                                  #

consumer_key = 'hSpg4TO7O54gOWzpgAX1WR8gJ'
consumer_secret = 'qWq8azeSlUjw8wMoqjcNgfXVty7CUMuIdfLTr12aODBpOMYb73'
oauth_token = '1449380540-7dAqZl6lfAgKQN9URfSt5DWeovktqDJkz6rycys'
oauth_token_secret = 'PBMdujMHolRSifaJbb1qiSLAEbl3FpAtBV2yDPxoaZELs'

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(oauth_token, oauth_token_secret)

api = tweepy.API(auth, wait_on_rate_limit=True)

x = mycol.find({}, {'_id':0})
for i in x:
    if "…" in i['text']:
        try:
            print('#########################')
            tweet = api.get_status(i['id'], tweet_mode='extended')
            if tweet.retweeted_status:
                texto = tweet._json['retweeted_status']['full_text']
                print(texto)
            else:
                print(tweet.full_text)
                print(i['id'])
        except:
            print('Error en el tweet con id: ' + i['id_str'])