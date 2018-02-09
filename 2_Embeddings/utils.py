import os
import glob
import string

import numpy as np

def read_imdb_data(input_dir='../data/aclImdb/train'):
    translator = str.maketrans(' ', ' ', string.punctuation)

    def _read(directory, label):
        X, y = [], []
        for f in glob.glob(directory):
            with open(f) as fp:
                line = fp.read()
                line = line.lower()
                line = line.translate(translator)
                X.append(line)
                y.append(label)
        return X, y
    
    negative = os.path.join(input_dir, 'neg', '*.txt')
    positive = os.path.join(input_dir, 'pos', '*.txt')
    
    Xn, yn = _read(negative, 0)
    Xp, yp = _read(positive, 1)
    return Xn + Xp, np.array(yn + yp)

def read_embeddings(input_file='../data/glove.6B.50d.txt', length=50):
    vectors, word_to_ix, ix_to_word = [], {}, []
    with open(input_file) as fp:
        for line in fp:
            # get the word and the vector
            word, *vector = line.split()
            vector = [float(i) for i in vector]
            # ensure that the vector is the correct length
            if len(vector) != length: continue
            word_to_ix[word] = len(ix_to_word) 
            ix_to_word.append(word)
            vectors.append(vector)
    return np.array(vectors), word_to_ix, ix_to_word

def read_stop_words(input_file='../data/stopwords.txt'):
    with open(input_file) as fp:
        stopwords = [l.strip().lower() for l in fp]
    return stopwords

stop_words = read_stop_words()
