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

def data_batcher(X, y, batches=5):
    indices = np.arange(X.shape[0])
    np.random.shuffle(indices)
    
    for i in range(batches):
        start = int((i * X.shape[0]) / batches)
        end = int(((i + 1) * X.shape[0]) / batches)
        print(start, end)
        yield X[start:end, :], y[start:end]

def read_stop_words(input_file='../data/stopwords.txt'):
    with open(input_file) as fp:
        stopwords = [l.strip().lower() for l in fp]
    return stopwords

stop_words = read_stop_words()
