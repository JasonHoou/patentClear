'''
created on Apr 20, 2016
@author: jason
'''

import nltk
from nltk.tree import *
from nltk import RegexpParser
import nltk
import re
import string
import csv


# Tree manipulation

# Extract phrases from a parsed (chunked) tree
# Phrase = tag for the string phrase (sub-tree) to extract
# Returns: List of deep copies;  Recursive
def ExtractPhrases( myTree, phrase):
    myPhrases = []
    if (myTree.label() == phrase):
        myPhrases.append(myTree.copy(True))
    for child in myTree:
        #print child,type(child)
        if (type(child) is Tree):
            print child
            #ExtractPhrases(child, phrase)
            #list_of_phrases = ExtractPhrases(child, phrase)
        elif(child[1] == phrase):
            myPhrases.append(child[0])
    return myPhrases

def GetPhrases(sentences, phrase):
    myPhrase = []
    for sentence in sentences:
        for item in sentence:
            if phrase in item[1]:
                myPhrase.append(item[0])
            else:
                pass
    return myPhrase


def ie_preprocess(document):
    document = document.decode('utf-8')
    sentences = nltk.sent_tokenize(document)
    sentences = [nltk.word_tokenize(sent) for sent in sentences]
    sentences = [nltk.pos_tag(sent) for sent in sentences]
    return sentences

def main():
    #with open('/Users/Jason/Documents/deeplearningNLP/dataset/CleanDataset/train/90_train.csv', 'rb') as csvfile:
    with open('90_train.csv', 'rb') as csvfile:
        spamreader = csv.reader(csvfile)
        with open('trainNouns.csv', 'a+') as file:
            patentWriter = csv.writer(file, delimiter=',', quotechar='"', quoting=csv.QUOTE_ALL, lineterminator='\n')
            for row in spamreader:
                abstract = row[2]
                #print row[2:-1], '\n', row[2]
                sentences = ie_preprocess(abstract)
                abstNouns = ' '.join(GetPhrases(sentences, 'NN'))
                patentWriter.writerow([row[0], row[1], abstNouns.encode('utf-8')])
                #print abstNouns
            #patentwriter.close()
            print "======covert done!!!========"

if __name__ == '__main__':
    main()
