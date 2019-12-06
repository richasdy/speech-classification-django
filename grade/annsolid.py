import pandas as pd
import pickle
from keras.preprocessing.sequence import pad_sequences
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
from nltk.tokenize.treebank import TreebankWordDetokenizer
import re
import string
import numpy as np
from keras.models import load_model


def text_normalization(text):
    # lower case
    text = text.lower()
    # remove number
    text = re.sub(r'\d+','',text)
    # remove the punctuation
    text = text.translate(str.maketrans("","",string.punctuation))
    # remove white space
    text = re.sub(' +',' ', text)
    # tokenization
    tokenized_text = word_tokenize(text)
    # stop words removal
    stop_words = list(stopwords.words("english"))
    tokenized_text = [word for word in tokenized_text if word not in stop_words]
    # lemmatization
    lemmatizer = WordNetLemmatizer()
    lemm_text = [lemmatizer.lemmatize(txt) for txt in tokenized_text]
    # detokenization
    output = TreebankWordDetokenizer().detokenize(lemm_text)
    return output



import pickle
with open("grade/model-ml/token.pickle", "rb") as f:
    tokenizer = pickle.load(f)          
f.close()

model = load_model('grade/model-ml/annsolid.h5')

#run(pd.Series(["Hello Doni"]))

def run(temp):
#    df = pd.DataFrame([tmp])
    temp = pd.Series([temp])
    temp = temp.apply(lambda x: text_normalization(x))
#    temp[0][0] = preprocessing(temp[0][0])
#    temp = preprocessing(temp)
    temp = tokenizer.texts_to_sequences(temp) 
    maxlen = 100
    temp = pad_sequences(temp, padding='post', maxlen=maxlen)
    pred = model.predict(temp)
    pred = np.argmax(pred)+1
    return pred