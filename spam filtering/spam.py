# -*- coding: utf-8 -*-
"""
Created on Fri May 25 21:50:42 2018

@author: Amit
"""

import os
import re
import string
import math

DATA_DIR = 'F:\tutorials\python\learning\spam filtering'
target_names = [ ' ham' , ' spam' ]
def get_data(DATA_DIR):
    subfolders = [ ' enron%d' % i for i in range(1, 7) ]
    data = [ ]
    target = [ ]
    for subfolder in subfolders:
    # spam
        spam_files = os.listdir(os.path.join(DATA_DIR, subfolder,' spam' ) )
        for spam_file in spam_files:
            with open(os.path.join(DATA_DIR, subfolder, ' spam' , spam_file) , encoding="latin-1") as f:
                data.append(f.read())
                target.append(1)
    # ham
        ham_files = os.listdir(os.path.join(DATA_DIR, subfolder,' ham' ) )
        for ham_file in ham_files:
            with open(os.path.join(DATA_DIR, subfolder, ' ham' ,ham_file) , encoding="latin-1") as f:
                data.append(f.read() )
                target.append(0)
                print(data)
    return data, target

class SpamDetector(object) :
    #Implementation of Naive Bayes for binary classification
    def clean(self, s):
        translator = str.maketrans("", "", string.punctuation)
        return s.translate(translator)

    def tokenize(self, text):
        text = self.clean(text).lower()
        return re.split("\W+", text)

    def get_word_counts(self, words):
        word_counts = {}
        for word in words:
            word_counts[word] = word_counts.get(word, 0.0) + 1.0
        return word_counts
    
def fit(self, X, Y):
    self.log_class_priors = {}
    self.word_counts = {}
    self.vocab = set()
    n = len(X)
    self.log_class_priors[ ' spam' ] = math.log(sum(1 for label in Y if label== 1) / n)
    self.log_class_priors[ ' ham' ] = math.log(sum(1 for label in Y if label== 0) / n)
    self.word_counts[ ' spam' ] = {}
    self.word_counts[ ' ham' ] = {}
    for x, y in zip(X, Y) :
        c = ' spam' if y == 1 else ' ham'
        counts = self.get_word_counts(self.tokenize(x))
        for word, count in counts.items() :
            if word not in self.vocab:
                self.vocab.add(word)
            if word not in self.word_counts[c] :
                self.word_counts[c] [word] = 0.0
        self.word_counts[c][word] += count

def predict(self, X) :
    result = [ ]
    for x in X:
        counts = self.get_word_counts(self.tokenize(x))
        spam_score = 0
        ham_score = 0
        for word, _ in counts.items() :
            if word not in self.vocab: continue
                # add Laplace smoothing
            log_w_given_spam = math.log((self.word_counts[ ' spam' ].get(word, 0.0) + 1) /(sum(self.word_counts[ ' spam' ].values()) + len(self.vocab)))
            log_w_given_ham = math.log((self. word_counts[ ' ham' ].get(word,0.0) + 1) / (sum(self.word_counts[ ' ham' ].values()) + len(self.vocab)))
            spam_score += log_w_given_spam
            ham_score += log_w_given_ham
        spam_score += self.log_class_priors[ ' spam' ]
        ham_score += self.log_class_priors[ ' ham' ]
        if spam_score > ham_score:
            result.append(1)
        else:
            result.append(0)
    return result
                
if __name__ == ' __main__':
    X, y = get_data(DATA_DIR)
    MNB = SpamDetector()
    MNB.fit(X[100:] , y[100:])
    pred = MNB.predict(X[:100])
    true = y[:100]
    accuracy = sum(1 for i in range(len(pred)) if pred[i] == true[i])/float(len(pred) )
    print("{0:.4f}".format(accuracy))