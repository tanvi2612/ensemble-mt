#!/usr/bin/python3

import spacy

def hindi_tok(data_dir, prefix):
    nlp = spacy.load("xx_ent_wiki_sm")
    tok_hi = []

    hi = open(data_dir+'/'+prefix+'.txt')
    hi = hi.readlines()

    for string in hi:
        if type(string)==str:
            doc = nlp(string)
            tok_hi.append(' '.join([token.text for token in doc]))

    hi = open(data_dir+'/'+prefix+'.tok.txt', "w+")
    tok_hi = ''.join(tok_hi)
    hi.write(tok_hi)

def preprocess(path, hi=True):
    fp = open(path)
    sentences = fp.readlines()

    tmp = []
    for sent in sentences:
        tmp.append(sent.lstrip("\"").rstrip("\"\n")+"\n")

    tmp = ''.join(tmp)
    fp = open(path, "w+")
    fp.write(tmp)

"""
preprocess('../experiments/data/src-train.txt')
preprocess('../experiments/data/src-val.txt')

preprocess('../experiments/data/tgt-test.txt')
preprocess('../experiments/data/tgt-train.txt')
preprocess('../experiments/data/tgt-val.txt')
hindi_tok('../experiments/data', 'tgt-test')
hindi_tok('../experiments/data', 'tgt-train')
hindi_tok('../experiments/data', 'tgt-val')
"""
preprocess('../experiments/results/predicted_test.txt')
