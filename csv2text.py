#!/usr/bin/python
#coding:utf-8
'''
Created on June 22, 2016

@author: jason
'''
import os
import pandas as pd
import glob
import re
import json as js
import csv
from string import punctuation


#readFile = r"/home/jason/Documents/data/NonLabels/"
readFile = r"/home/jason/Documents/data/12classes/"
writeDir = r"/home/jason/Documents/PythonCodes/cnn-patent-classification-tf-master/data/"


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
    #column = ['title', 'abstract']
    list_ = []
    for file_ in allFiles:
        print file_
        df = pd.read_csv(file_, index_col=None, names=column)
        list_.append(df)
    frame = pd.concat(list_)
    return frame


def getFileNamme(destDir):
    #Get all files
    names = [name for name in os.listdir(destDir)
        if name.endswith('.json')]
        #if os.path.isfile(os.path.join(destDir, name))]
    return names

def writeText(fileName, row):
    with open(fileName, 'a+') as textWriter:
        textWriter.write(str(row))
    textWriter.close()


def main():
    #readCSV
    datasetDf = getDataFrame(readFile)
    abstract_list = datasetDf['abstract'].tolist()
    title_list = datasetDf['title'].tolist()
    i = 0
    for item in abstract_list:
        patent_text = str(title_list[i]) + str(item)
        writeText(writeDir + "/12_classes_Text.txt", patent_text)
        i += 1

if __name__ == '__main__':
    main()




