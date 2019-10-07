import pandas as pd
import re
from library.Sastrawi.StopWordRemover.StopWordRemoverFactory import StopWordRemoverFactory
from library.Sastrawi.Stemmer.StemmerFactory import StemmerFactory
import nltk
from nltk.tokenize.treebank import TreebankWordDetokenizer as Detok
from sklearn import preprocessing
from sklearn.svm import SVC

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

#KLASIFIKASI SVM
clf = SVC(gamma='auto')
#clf.fit(X_train, Y_train)

import pickle
with open("clf-totality.pickle", "rb") as f:
    clf = pickle.load(f)
    vectorizer = pickle.load(f)
    tfidf_transformer = pickle.load(f)
f.close()

#run(pd.Series(["Hello Doni"]))

def run(temp):
#    df = pd.DataFrame([tmp])
    temp = pd.Series([temp])
    temp = temp.apply(lambda x: preprocessing(x))
#    temp[0][0] = preprocessing(temp[0][0])
#    temp = preprocessing(temp)
    temp = vectorizer.transform(temp)
    temp = tfidf_transformer.transform(temp)
    temp = temp.toarray()
    
    pred = clf.predict(temp)
    return pred[0]
