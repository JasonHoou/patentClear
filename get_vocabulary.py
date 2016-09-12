#!/usr/bin/python
#coding:utf-8
'''
Created on July 15, 2016

@author: jason
'''
import os
import pandas as pd
import glob
import re
import json as js
import csv
from string import punctuation
from collections import Counter
import csv
import json
import itertools

# Load data

def clean_str(string):
    """
    Tokenization/string cleaning for all datasets except for SST.
    Original taken from https://github.com/yoonkim/CNN_sentence/blob/master/process_data.py
    """
    string = re.sub(r"\'s", " \'s", string)
    string = re.sub(r"\'ve", " \'ve", string)
    string = re.sub(r"n\'t", " n\'t", string)
    string = re.sub(r"\'re", " \'re", string)
    string = re.sub(r"\'d", " \'d", string)
    string = re.sub(r"\'ll", " \'ll", string)
    string = re.sub(r",", " , ", string)
    string = re.sub(r"!", " ! ", string)
    string = re.sub(r"\(", " \( ", string)
    string = re.sub(r"\)", " \) ", string)
    string = re.sub(r"\?", " \? ", string)
    string = re.sub(r"\s{2,}", " ", string)
    string = re.sub(r"[^a-z0-9(),!?\'\`]", " ", string)
    string = strip_punctuation(string)
    return string.strip().lower()

def strip_punctuation(string):
    return ''.join(c for c in string if c not in punctuation)

def getDataFrame(fileDir):
    allFiles = glob.glob(fileDir + "/*.csv")
    frame = pd.DataFrame()
    column = ['section','title', 'abstract']
    list_ = []
    for file_ in allFiles:
        print file_
        df = pd.read_csv(file_, index_col=None, names=column)
        list_.append(df)
    frame = pd.concat(list_)
    return frame

def writeText(fileName, row):
    print "Writing file..."
    with open(fileName, 'w') as file:
        file.write(json.dumps(row, indent=4))

def build_vocab(text):
    """
    Builds a vocabulary mapping from word to index based on the sentences.
    Returns vocabulary mapping and inverse vocabulary mapping.
    """
    # Build vocabulary
    word_counts = Counter(text.split())
    print "word_counts", len(word_counts)
    # Mapping from index to word
    vocabulary_inv = [x[0] for x in word_counts.most_common()]
    #vocabulary_inv = list(sorted(vocabulary_inv))
    # Mapping from word to index
    vocabulary = {x: i for i, x in enumerate(vocabulary_inv)}
    return vocabulary


def main():
    #readCSV
    readDir = r"/home/jason/Documents/data/12classes/"
    writeDir = r"/home/jason/Documents/data/vocab.json"

    datasetDf = getDataFrame(readDir)
    abstract_list = datasetDf['abstract'].tolist()
    title_list = datasetDf['title'].tolist()
    i = 0
    text = "UNK "*200000
    for item in abstract_list:
        patent_text = str(title_list[i]) + str(item)
        text += patent_text
        i += 1
    vocabulary = build_vocab(text)
    print len(vocabulary)
    writeText(writeDir, vocabulary)

if __name__ == '__main__':
    main()
