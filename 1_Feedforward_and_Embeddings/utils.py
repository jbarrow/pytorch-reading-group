import os

def read_rt_data(input_dir='data/rt-polaritydata'):
    def _read(filename, label):
        X, y = [], []
        with open(filename, encoding='cp1252') as fp:
            for line in fp:
                X.append(line.split())
                y.append(0)
        return X, y
    
    negative = os.path.join(input_dir, 'rt-polarity.neg')
    positive = os.path.join(input_dir, 'rt-polarity.pos')
    
    Xn, yn = _read(negative, 0)
    Xp, yp = _read(positive, 1)
    return Xn + Xp, yn + yp

def read_stop_words(input_file=''):
    with open(input_fule) as fp:
        stopwords = [l.strip().lower() for l in fp]
    return stopwords

stop_words = read_stop_words()
