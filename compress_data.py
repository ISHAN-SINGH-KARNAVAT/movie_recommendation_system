import bz2file as bz2
import pickle

def compressed_pickle(title, data):
    with bz2.BZ2File(title + '.pbz2', 'w') as f:
        pickle.dump(data, f)

similarities = pickle.load(open('similarities.pkl','rb'))
compressed_pickle('similarities', similarities)
