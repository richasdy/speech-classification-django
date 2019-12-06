import pandas as pd
import numpy as np
import math
import os
import re
from library.Sastrawi.StopWordRemover.StopWordRemoverFactory import StopWordRemoverFactory
from library.Sastrawi.Stemmer.StemmerFactory import StemmerFactory
from nltk import word_tokenize
from nltk.tokenize import RegexpTokenizer
from nltk.tag import CRFTagger
from sklearn.model_selection import train_test_split
import nltk
from nltk.tokenize.treebank import TreebankWordDetokenizer as Detok
from sklearn import preprocessing
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction.text import TfidfTransformer
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import GaussianNB
from sklearn.metrics import accuracy_score
from sklearn.svm import SVC
from sklearn import svm
from sklearn.model_selection import GridSearchCV
from sklearn.svm import SVR
from sklearn.kernel_ridge import KernelRidge

#PREPROCESSING
factory = StemmerFactory()
stemmer = factory.create_stemmer()
factory = StopWordRemoverFactory()
stopwords = factory.get_stop_words()
detokenizer = Detok()

def preprocessing(tmp):
    tmp = tmp.lower()
    tmp = re.sub("[^a-zA-Z]", " ", tmp)
    tmp =  nltk.tokenize.word_tokenize(tmp)
    tmp = [item for item in tmp if item not in stopwords]
    tmp = [stemmer.stem(y) for y in tmp]
    tmp = detokenizer.detokenize(tmp)
    return tmp

import pickle
with open("grade/model-ml/clf-solid.pickle", "rb") as f:
    grid_search = pickle.load(f)
    vectorizer = pickle.load(f)
    tfidf_transformer = pickle.load(f)
f.close()

def run(temp):
#    df = pd.DataFrame([tmp])
    temp = pd.Series([temp])
    temp = temp.apply(lambda x: preprocessing(x))
#    temp[0][0] = preprocessing(temp[0][0])
#    temp = preprocessing(temp)
    temp = vectorizer.transform(temp)
    temp = tfidf_transformer.transform(temp)
    temp = temp.toarray()
    
    pred = grid_search.predict(temp)
    return pred[0]