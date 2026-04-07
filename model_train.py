import json
import numpy as np
#import tensorflow as tf
#from tensorflow import keras
#from tensorflow.keras.models import Sequential
#from tensorflow.keras.layers import Dense, Embedding, GlobalAveragePoolingID
#from tensorflow.keras.preprocessing.text import Tokenizer
#from tensorflow.keras.preprocessing.sequence import pad_sequence
from sklearn.preprocessing import LabelEncoder


with open("intent.json") as file:
    data = json.load(file)

training_sentences = []
training_labels = []
labels =[]
responses = []

for intent in data['intents']:
    for pattern in intent['patterns']:
        training_sentences.append(pattern)
        training_labels.append(intent['tag'])
    responses.append(intent['responses'])

    if intent['tag'] not in labels:
        labels.append(intent['tag'])

number_of_classes = len(labels)

label_encoder = LabelEncoder()
label_encoder.fit(training_labels)
training_labels=label_encoder.transform(training_labels)

vocab_size = 1000
