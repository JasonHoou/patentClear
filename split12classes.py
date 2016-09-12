#!/usr/bin/python
#coding:utf-8
'''
Created on July 4, 2016

@author: jason
'''
import sys
reload(sys)
sys.setdefaultencoding('utf-8')
import os
import json as js
import csv
import re
from string import punctuation

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

def getFileNamme(destDir):
    #Get all files
    names = [name for name in os.listdir(destDir)
        if name.endswith('.json')]
        #if os.path.isfile(os.path.join(destDir, name))]
    return names

def writeCSV(fileName, row):
    with open(fileName, 'a+') as csvfile:
        csv_writer = csv.writer(csvfile, delimiter=',', quotechar='"', quoting=csv.QUOTE_ALL, lineterminator='\n')
        csv_writer.writerow(row)
    csvfile.close()


def json2CSV(savDir, data):
    for item in data:

        title = str(item['Title']).strip().replace('\n', '').encode('utf-8').lower()
        abstract = str(item['Abstract']).strip().replace('\n', '').encode('utf-8').lower()
        if len(title.split()) > 3 and len(abstract.split()) > 5:

            title = clean_str(title)
            abstract = clean_str(abstract)

            if item['Section'] == 'G' and item['Mianclass'] == '06':
                writeCSV(savDir + "G_06.csv", ["1", title, abstract])

            elif item['Section'] == 'H' and item['Mianclass'] == '04':
                writeCSV(savDir + "H_04.csv", ["2", title, abstract])

            elif item['Section'] == 'H' and item['Mianclass'] == '01':
                writeCSV(savDir + "H_01.csv", ["3", title, abstract])

            elif item['Section'] == 'A' and item['Mianclass'] == '61':
                writeCSV(savDir + "A_61.csv", ["4", title, abstract])

            elif item['Section'] == 'C' and item['Mianclass'] == '07':
                writeCSV(savDir + "C_07.csv", ["5", title, abstract])

            elif item['Section'] == 'C' and item['Mianclass'] == '12':
                writeCSV(savDir + "C_12.csv", ["6", title, abstract])

            elif item['Section'] == 'G' and item['Mianclass'] == '02':
                writeCSV(savDir + "G_02.csv", ["7", title, abstract])

            elif item['Section'] == 'G' and item['Mianclass'] == '11':
                writeCSV(savDir + "G_11.csv", ["8", title, abstract])

            elif item['Section'] == 'G' and item['Mianclass'] == '03':
                writeCSV(savDir + "G_03.csv", ["9", title, abstract])

            elif item['Section'] == 'A' and item['Mianclass'] == '01':
                writeCSV(savDir + "A_01.csv", ["10", title, abstract])

            elif item['Section'] == 'C' and item['Mianclass'] == '08':
                writeCSV(savDir + "C_08.csv", ["11", title, abstract])

            elif item['Section'] == 'H' and item['Mianclass'] == '03':
                writeCSV(savDir + "H_03.csv", ["12", title, abstract])


            # else:
            #     csv_file.writerow(['0', item['Title'].encode('utf-8'), item['Abstract'].encode('utf-8')])

def main():
    dest = "/home/jason/Documents/"
    savDir = "/home/jason/Documents/data/12classes/"
    #dirnames = getDirName(dest)
    #print destDir
    fileNames = getFileNamme(dest)

    for fileName in fileNames:
        fileDir = os.path.abspath(dest + fileName)
        print fileDir
        with open(fileDir, 'r') as jsonFile:
            #getXmlInfo(fileDir)
            data = js.load(jsonFile)
            json2CSV(savDir, data)
            #print fileNames
    print  "#### Well Done! ####"

if __name__ == "__main__":
    main()

