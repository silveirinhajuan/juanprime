import nltk
from nltk.stem.porter import PorterStemmer
import numpy as np
# nltk.download('punkt')  # <- This is to download methods of nltk, if not the lib don't work

stemmer = PorterStemmer()


def tokenize(setence):
    return nltk.word_tokenize(setence)


def stem(word):
    return stemmer.stem(word=word)


def bag_of_words(tokenize_setence, all_words):
    tokenize_setence = [stem(w) for w in all_words if w not in tokenize_setence]

    bag = np.zeros(len(all_words), dtype=np.float32)
    for idx , w in enumerate(all_words):
        if w in tokenize_setence:
            bag[idx] = 1.0

    return bag
