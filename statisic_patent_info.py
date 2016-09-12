#!/usr/bin/python
#coding:utf-8
'''
Created on July 5, 2016

@author: jason
'''
import pandas as pd
import glob
import numpy as np
import re
import itertools
import pandas as pd
import glob
from collections import Counter
from time import time
from tempfile import TemporaryFile
from string import punctuation

def clean_str(string):
    """
    Tokenization/string cleaning for all datasets except for SST.
    Original taken from https://github.com/yoonkim/CNN_sentence/blob/master/process_data.py
    """
    string = re.sub(r"[^a-z0-9(),!?\'\`]", " ", string)
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
    return string.strip().lower()


def getDataFrame(fileDir):
    allFiles = glob.glob(fileDir + "/*.csv")
    frame = pd.DataFrame()
    column = ['section', 'title', 'abstract']
    list_ = []
    for file_ in allFiles:
        print file_
        df = pd.read_csv(file_, index_col=None, names=column)
        list_.append(df)
    frame = pd.concat(list_)
    return frame

def strip_punctuation(s):
    return ''.join(c for c in s if c not in punctuation)


def load_data_and_labels():
    """
    Loads MR polarity data from files, splits the data into words and generates labels.
    Returns split sentences and labels.
    """
    # Load data from files
    #fileDir = "/Users/Jason/Documents/workstation/Documents/Crepe-master/data/dbpedia_csv/patentDataset"
    fileDir = "/home/jason/Documents/data/12classes/"
    #fileDir = "/home/jason/Documents/data/subclassLabel/"
    datasetDf = getDataFrame(fileDir)

    labels = datasetDf['section'].tolist()
    abstract_list = datasetDf['abstract'].tolist()
    title_list = datasetDf['title'].tolist()
    abstract_list = map(str, abstract_list)#convert Unicode to utf-8
    i = 0
    patent_text = []
    maxLength = 0
    minLength = 1000
    averageLength = 0
    length = 0
    sumLength = 0
    for item in abstract_list:
        text = str(title_list[i]) + str(item)
        text.split()
        i += 1
        length = len(text.split())
        if maxLength <= length:
            maxLength = length
        elif minLength >= length:
            minLength = length
        elif length <= 10 or length > 300:
            print text

        sumLength += length
    averageLength = sumLength/(i+1)
    print 'The total documents is: ', i+1
    print 'The longest sentence is: ', maxLength
    print 'The shortest sentence is: ', minLength
    print 'The average length of the document is: ', averageLength
    # x_text = [s.split(" ") for s in x_text]


load_data_and_labels()