import re
import unidecode
from string import punctuation
from nltk.corpus import stopwords
from nltk.tokenize import TweetTokenizer
import pandas as pd

cache_english_stopwords = stopwords.words('english')
cache_spanish_stopwords = stopwords.words('spanish')
def remove_emoji(string):
    emoji_pattern = re.compile("["
                               u"\U000000A9-\U0001F9FF" 
                               "]+", flags=re.UNICODE)
    return emoji_pattern.sub(r'', string)

def tweet_clean(tweet):
    #print('Original tweet:', tweet, '\n')
    # Remove HTML special entities (e.g. &amp;)
    tweet_no_special_entities = re.sub(r'\&\w*;', '', tweet)
    #print('No special entitites:', tweet_no_special_entities, '\n')
    # Remove tickers
    tweet_no_tickers = re.sub(r'\$\w*', '', tweet_no_special_entities)
    #print('No tickers:', tweet_no_tickers, '\n')
    # Remove hyperlinks
    tweet_no_hyperlinks = re.sub(r'https?:\/\/.*\/\w*', '', tweet_no_tickers)
    #print('No hyperlinks:', tweet_no_hyperlinks, '\n')
    # Remove Users
    tweet_no_users = re.sub(r'@\w*', '', tweet_no_hyperlinks)
    #print('No users:', tweet_no_users, '\n')
    # Remove hashtags
    tweet_no_hashtags = re.sub(r'#\w*', '', tweet_no_users)
    #print('No hashtags:', tweet_no_hashtags, '\n')
    tweet_no_punctuation = re.sub(r'[' + punctuation.replace('@', '') + ']+', ' ', tweet_no_hashtags)
    tweet_no_punctuation1 = re.sub(r'…\w*', '', tweet_no_punctuation)
    tweet_no_punctuation2 = re.sub(r'[^\w]', ' ', tweet_no_punctuation1)

    #print('No punctuation:', tweet_no_punctuation2, '\n')
    # Remove https
    tweet_no_https = re.sub(r'https', '', tweet_no_punctuation2)
    tweet_no_https = re.sub(r'http', '', tweet_no_punctuation2)
    #print('No https:', tweet_no_https, '\n')
    # Remove words with 2 or fewer letters
    tweet_no_small_words = re.sub(r'\b\w{1,2}\b', '', tweet_no_https)
    #print('No small words:', tweet_no_small_words, '\n')
    # Remove whitespace (including new line characters)
    tweet_no_whitespace = re.sub(r'\s\s+', ' ', tweet_no_small_words) 
    tweet_no_whitespace = tweet_no_whitespace.lstrip(' ') # Remove single space remaining at the front of the tweet.
    #print('No whitespace:', tweet_no_whitespace, '\n')
    #Añadido quitar acentos
    unaccented_string = unidecode.unidecode(tweet_no_whitespace)
    #print('No accents:', unaccented_string, '\n')
    # Añadido quitar mas emojis
	# Remove characters beyond Basic Multilingual Plane (BMP) of Unicode:
    # tweet_no_emojis = ''.join(c for c in tweet_no_whitespace if c <= '\uFFFF') # Apart from emojis (plane 1), this also removes historic scripts and mathematical alphanumerics (also plane 1), ideographs (plane 2) and more.
    tweet_no_emojis = remove_emoji(unaccented_string)
    #print('No emojis:', tweet_no_emojis, '\n')

    # Tokenize: Change to lowercase, reduce length and remove handles
    tknzr = TweetTokenizer(preserve_case=False, reduce_len=True, strip_handles=True) # reduce_len changes, for example, waaaaaayyyy to waaayyy.
    tw_list = tknzr.tokenize(tweet_no_emojis)
    #print('Tweet tokenize:', tw_list, '\n')
    # Remove stopwords
    list_no_stopwords = [i for i in tw_list if i not in cache_english_stopwords]
    #print('No stop words:', list_no_stopwords, '\n')
    list_no_stopwords = [i for i in list_no_stopwords if i not in cache_spanish_stopwords]
    #print('No stop words:', list_no_stopwords, '\n')
    # Final filtered tweet
    tweet_filtered =' '.join(list_no_stopwords)
    #print('Final tweet:', tweet_filtered)

    #Devuelvo los tweets en listas
    return(list_no_stopwords)

def clean_data_from_json(file):
    # Load the first sheet of the JSON file into a data frame
    df = pd.read_json(file, orient='columns')

    print(list(df.columns.values))
    #['_id', 'created_at', 'entities', 'extended_entities', 'favorite_count', 'favorited', 'id', 'id_str',
    # 'in_reply_to_screen_name', 'in_reply_to_user_id', 'in_reply_to_user_id_str', 'is_quote_status', 'lang', 'metadata',
    # 'possibly_sensitive', 'quoted_status', 'quoted_status_id', 'quoted_status_id_str', 'retweet_count', 'retweeted',
    # 'retweeted_status', 'source', 'text', 'truncated', 'user']

    data = df['text'].tolist()
    print(data)
    l = []
    for tweet in data:
        s = tweet_clean(tweet)
        print(s)
        l.append(s)

    print(l)
    return(l)



def clean_data_from_json_filter(file, filter):
    # Load the first sheet of the JSON file into a data frame
    df = pd.read_json(file, orient='columns')
    if(filter == 'en'):
        filterdf = df[(df['lang'] == 'en')]
    else:
        filterdf =df[(df['lang'] == 'es')]



    data = filterdf.text.tolist()
    print(data)
    l = []
    for tweet in data:
        s = tweet_clean(tweet)
        print(s)
        l.append(s)

    print(l)
    return(l)

def tweet_clean_with_emojis(tweet):
    #print('Original tweet:', tweet, '\n')
    # Remove HTML special entities (e.g. &amp;)
    tweet_no_special_entities = re.sub(r'\&\w*;', '', tweet)
    #print('No special entitites:', tweet_no_special_entities, '\n')
    # Remove tickers
    tweet_no_tickers = re.sub(r'\$\w*', '', tweet_no_special_entities)
    #print('No tickers:', tweet_no_tickers, '\n')
    # Remove hyperlinks
    tweet_no_hyperlinks = re.sub(r'https?:\/\/.*\/\w*', '', tweet_no_tickers)
    #print('No hyperlinks:', tweet_no_hyperlinks, '\n')
    # Remove Users
    tweet_no_users = re.sub(r'@\w*', '', tweet_no_hyperlinks)
    #print('No users:', tweet_no_users, '\n')
    # Remove hashtags
    tweet_no_hashtags = re.sub(r'#\w*', '', tweet_no_users)
    #print('No hashtags:', tweet_no_hashtags, '\n')
    tweet_no_punctuation = re.sub(r'[' + punctuation.replace('@', '') + ']+', ' ', tweet_no_hashtags)
    tweet_no_punctuation1 = re.sub(r'…\w*', '', tweet_no_punctuation)
    tweet_no_punctuation2 = re.sub(r'[^\w]', ' ', tweet_no_punctuation1)

    #print('No punctuation:', tweet_no_punctuation2, '\n')
    # Remove https
    tweet_no_https = re.sub(r'https', '', tweet_no_punctuation2)
    tweet_no_https = re.sub(r'http', '', tweet_no_punctuation2)
    #print('No https:', tweet_no_https, '\n')
    # Remove words with 2 or fewer letters
    tweet_no_small_words = re.sub(r'\b\w{1,2}\b', '', tweet_no_https)
    #print('No small words:', tweet_no_small_words, '\n')
    # Remove whitespace (including new line characters)
    tweet_no_whitespace = re.sub(r'\s\s+', ' ', tweet_no_small_words)
    tweet_no_whitespace = tweet_no_whitespace.lstrip(' ') # Remove single space remaining at the front of the tweet.
    #print('No whitespace:', tweet_no_whitespace, '\n')
    #Añadido quitar acentos
    unaccented_string = unidecode.unidecode(tweet_no_whitespace)
    #print('No accents:', unaccented_string, '\n')
    # Añadido quitar mas emojis
	# Remove characters beyond Basic Multilingual Plane (BMP) of Unicode:
    # tweet_no_emojis = ''.join(c for c in tweet_no_whitespace if c <= '\uFFFF') # Apart from emojis (plane 1), this also removes historic scripts and mathematical alphanumerics (also plane 1), ideographs (plane 2) and more.
    # Tokenize: Change to lowercase, reduce length and remove handles
    tknzr = TweetTokenizer(preserve_case=False, reduce_len=True, strip_handles=True) # reduce_len changes, for example, waaaaaayyyy to waaayyy.
    tw_list = tknzr.tokenize(unaccented_string)
    #print('Tweet tokenize:', tw_list, '\n')
    # Remove stopwords
    list_no_stopwords = [i for i in tw_list if i not in cache_english_stopwords]
    #print('No stop words:', list_no_stopwords, '\n')
    list_no_stopwords = [i for i in list_no_stopwords if i not in cache_spanish_stopwords]
    #print('No stop words:', list_no_stopwords, '\n')
    # Final filtered tweet
    tweet_filtered =' '.join(list_no_stopwords)
    #print('Final tweet:', tweet_filtered)

    #Devuelvo los tweets en listas
    return(list_no_stopwords)

def clean_data_from_list(list):
    # Load the first sheet of the JSON file into a data frame
    #['_id', 'created_at', 'entities', 'extended_entities', 'favorite_count', 'favorited', 'id', 'id_str',
    # 'in_reply_to_screen_name', 'in_reply_to_user_id', 'in_reply_to_user_id_str', 'is_quote_status', 'lang', 'metadata',
    # 'possibly_sensitive', 'quoted_status', 'quoted_status_id', 'quoted_status_id_str', 'retweet_count', 'retweeted',
    # 'retweeted_status', 'source', 'text', 'truncated', 'user']
    print(list)
    l = []
    for tweet in list:
        s = tweet_clean(tweet)
        print(s)
        l.append(s)

    print(l)
    return(l)