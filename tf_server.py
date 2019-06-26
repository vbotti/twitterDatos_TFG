
from http.server import BaseHTTPRequestHandler, HTTPServer
import re
import time

import urllib
import json
import os
import pickle
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from keras.models import model_from_json
from keras.preprocessing.sequence import pad_sequences

#matplotlib inline

from keras.layers import Dense, Activation, Dropout, Input, LSTM, Reshape, Lambda, RepeatVector, Concatenate
from keras.initializers import glorot_uniform
from keras.utils import to_categorical
from keras.models import Model
from keras.optimizers import Adam
from string import punctuation

def sentimentAnalysis(tweetList):
    for tweet in tweetList:
        tweetText = re.sub(r'@\w*', '', tweet[1])
        tweetText = re.sub(r'#\w*', '', tweetText)
        tweetText = re.sub(r'RT\w*', '', tweetText)
        tweetText = re.sub(r'#\w*', '', tweetText)
        tweetText = re.sub(r'[' + punctuation.replace('@', '') + ']+', ' ', tweetText)
        tweetText = re.sub(r'…\w*', '', tweetText)
        tweetText = re.sub(r'[^\w]', ' ', tweetText)
        tweetText = re.sub(r'https', '', tweetText)
        tweetText = re.sub(r'http', '', tweetText)
        msg_extracted = tweetText
        #print('This is the message extracted: ' + msg_extracted + '\n')
        tweet[2][3] = loaded_model_sent.predict_classes(pad_sequences(tokenizer_sent.texts_to_sequences([msg_extracted]), maxlen=100, padding='post'))[0][0]
    return tweetList



# Tokenizers

with open('./models_for_embeddings/tokenizer_sent.pcl', 'rb') as handle:#./models_for_embeddings/tokenizer_sent.pcl
	tokenizer_sent = pickle.load(handle)

with open('./models_for_embeddings/tokenizer_str.pcl', 'rb') as handle:
	tokenizer_str = pickle.load(handle)

# Text embedding ANN

opt = Adam(lr=0.01, beta_1=0.9, beta_2=0.999, decay=0.01)

# load json and create model
json_file = open('./models_for_embeddings/embeddings_forward_sentiment.json', 'r')#./models_for_embeddings/embeddings_forward_sentiment.json
loaded_model_json = json_file.read()
json_file.close()
loaded_model_sent = model_from_json(loaded_model_json)
# load weights into new model
loaded_model_sent.load_weights("./models_for_embeddings/embeddings_forward_sentiment.h5")#./models_for_embeddings/embeddings_forward_sentiment.h5
print("Loaded sentiment text model from disk")

loaded_model_sent.compile(optimizer='adam', loss='binary_crossentropy', metrics=['acc'])#'categorical_crossentropy', metrics=['accuracy'])

# load json and create model
json_file = open('./models_for_embeddings/embeddings_forward.json', 'r')
loaded_model_json = json_file.read()
json_file.close()
loaded_model_str = model_from_json(loaded_model_json)
# load weights into new model
loaded_model_str.load_weights("./models_for_embeddings/embeddings_forward.h5")
print("Loaded stress text model from disk")

loaded_model_str.compile(optimizer='adam', loss='binary_crossentropy', metrics=['acc'])#'categorical_crossentropy', metrics=['accuracy'])

# Load KSD models

# load json and create model
json_file = open('./models_for_embeddings/ksd_forward_sen.json', 'r')#./models_for_embeddings/notrain/
loaded_model_json = json_file.read()
json_file.close()
loaded_model_sent_KSD = model_from_json(loaded_model_json)
# load weights into new model
loaded_model_sent_KSD.load_weights("./models_for_embeddings/ksd_forward_sen.h5")
print("Loaded sentiment KSD model from disk")

loaded_model_sent_KSD.compile(optimizer='adam', loss='binary_crossentropy', metrics=['acc'])#'categorical_crossentropy', metrics=['accuracy'])

# load json and create model
json_file = open('./models_for_embeddings/ksd_forward_str.json', 'r')
loaded_model_json = json_file.read()
json_file.close()
loaded_model_str_KSD = model_from_json(loaded_model_json)
# load weights into new model
loaded_model_str_KSD.load_weights("./models_for_embeddings/ksd_forward_str.h5")
print("Loaded stress KSD model from disk")

loaded_model_str_KSD.compile(optimizer='adam', loss='binary_crossentropy', metrics=['acc'])#'categorical_crossentropy', metrics=['accuracy'])


#print(sentimentAnalysis([[123456, '@lisetluque @NaiDelysM3 @ExploCreativa finooooo a las cinco y media', [0, 0, 0, 0, 0, 0, 0]]]))