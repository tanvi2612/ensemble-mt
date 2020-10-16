#!/usr/bin/python3

from sklearn.model_selection import train_test_split
import spacy

def split(path="../dataset/MKB/", prefix="mkb"):
    en = open(path+prefix+".en")
    hi = open(path+prefix+".hi")

    en = en.readlines()
    hi = hi.readlines()
    assert len(en)==len(hi)

    en_train, en_test, hi_train, hi_test = train_test_split(en, hi, test_size=0.1)

    en_train = ''.join(en_train)
    en_test = ''.join(en_test)
    hi_train = ''.join(hi_train)
    hi_test = ''.join(hi_test)

    fp = open(path+"train.en", "w+")
    fp.write(en_train)
    fp = open(path+"test.en", "w+")
    fp.write(en_test)
    fp = open(path+"train.hi", "w+")
    fp.write(hi_train)
    fp = open(path+"test.hi", "w+")
    fp.write(hi_test)

def hindi_tok(path="../dataset/MKB/", prefix="test.hi"):
    hi = open(path+prefix)
    hi = hi.readlines()

    nlp = spacy.load("xx_ent_wiki_sm")
    tok_hi = []

    for string in hi:
        if type(string)==str:
            doc = nlp(string)
            tok_hi.append(' '.join([token.text for token in doc]))

    hi = open(path+"test.tok.hi", "w+")
    hi.write(''.join(tok_hi))

hindi_tok()
