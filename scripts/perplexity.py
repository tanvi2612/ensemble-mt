import nltk
from nltk.lm import MLE
from nltk.probability import LidstoneProbDist
import matplotlib.pyplot as plt
from collections import defaultdict

words = []
sentences = []
# wlen = defaultdict(int)
# ../dataset/en-hi.txt/OpenSubtitles.en-hi.hi
with open("../dataset/en-hi.txt/OpenSubtitles.en-hi.hi", "r") as f:
    lines = f.readlines()
    for line in lines:
        line = line.strip()
        line = line.split(" ")
        # wlen[len(line)] += 1
        words += line
        x = []
        for l in line:
            temp = tuple(l)
            x.append(temp)
        sentences.append(x)
        # words.append(line)
# plt.plot(x, y, label = 'English')
train = words
fdist = nltk.FreqDist(w for w in train)
vocabulary = list(set(map(lambda x: x[0], filter(lambda x: x[1] >= 2, fdist.items()))))
# print(len(vocabulary))
train = sentences
vocab = []
for v in vocabulary:
    vocab.append([tuple(v)])
# train = map(lambda x: x if x in vocabulary else "*unknown*", train)
words = []
test_sentences = []
with open("results/predicted_test.txt", "r") as f:
    lines = f.readlines()
    for line in lines:
        line = line.strip()
        test_sentences.append(line)
        line = line.split()
        # words += line
        x = []
        for l in line:
            temp = tuple(l)
            x.append(temp)
        words.append(x)
test = words
print("train")
# estimator = lambda fdist, bins: LidstoneProbDist(fdist, 0.2) 
lm = MLE(2)
for i in train:
    lm.fit([i], vocabulary_text=vocabulary)
print("Training done")
perp = []
minp = [["", 100000], ["", 100000]]
maxp = [["", 0], ["", 0]]

tot = len(test_sentences)+1
for i in range(len(test_sentences)):
    p = lm.perplexity(test[i])
    if len(test[i]) > 3:
        if p >= maxp[1][1]:
            maxp[0] = maxp[1]
            maxp[1] = [test_sentences[i], p]
        elif p >= maxp[0][1]:
            maxp[0] = [test_sentences[i], p]
        elif p <= minp[0][1]:
            minp[1] = minp[0]
            minp[0] = [test_sentences[i], p]
        elif p <= minp[1][1]:
            minp[1] = [test_sentences[i], p]

    if p > 2000:
        tot -= 1
        # print(test_sentences[i], p)
    else:
        perp.append(p)
    # print("perplexity(",i,") =", lm.perplexity(test[i]))
x = [i for i in range(1, tot)]
for i in minp:
    for j in i:
        print(j, end=" ")
    print()
for i in maxp:
    for j in i:
        print(j, end=" ")
    print()
        
# plt.plot(x, perp)
# plt.xlabel('Test Sentences Indexing')
# plt.ylabel('Perplexity Score')
# plt.show()