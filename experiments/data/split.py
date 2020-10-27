from sklearn.model_selection import train_test_split
import pandas as pd
import re
# import nu,py as np
X = []
with open("../../dataset/en-hi.txt/OpenSubtitles.en-hi.en") as f:
    for line in f:
        line = line.strip()
        # split each column on whitespace
        # columns = re.split('\s+', line, maxsplit=1)

        X.append(line)

print(len(X))
y = []
with open("../../dataset/en-hi.txt/OpenSubtitles.en-hi.hi") as f:
    for line in f:
        line = line.strip()
        # split each column on whitespace
        # columns = re.split('\s+', line, maxsplit=1)

        y.append(line)

print(len(y))
X = pd.DataFrame(X)
y = pd.DataFrame(y)

X_train, X_test, y_train, y_test = train_test_split( X, y, test_size=0.3, random_state=42)
X_val, X_test, y_val, y_test = train_test_split( X_test, y_test, test_size=0.2,  random_state=42)
X_train.to_csv('src-train.txt', header=None, index=None, sep=' ', mode='a')
y_train.to_csv('tgt-train.txt', header=None, index=None, sep=' ', mode='a')
X_val.to_csv('src-val.txt', header=None, index=None, sep=' ', mode='a')
y_val.to_csv('tgt-val.txt', header=None, index=None, sep=' ', mode='a')
X_test.to_csv('src-test.txt', header=None, index=None, sep=' ', mode='a')
y_test.to_csv('tgt-test.txt', header=None, index=None, sep=' ', mode='a')

# print(X_val)
# print(y_val)