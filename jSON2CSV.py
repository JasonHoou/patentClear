#!/usr/bin/python
#coding:utf-8
'''
Created on May 24, 2016

@author: jason
'''
import os
import json as js
import csv

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
        if item['Title'] is not None and item['Abstract'] is not None:
            title = str(item['Title'].strip().replace('\n', '').encode('utf-8')).lower()
            #title = ''' + title + '''
            abstract = str(item['Abstract'].strip().replace('\n', '').encode('utf-8')).lower()
            if item['Section'] == 'A':
                writeCSV(savDir + "A.json", ["1", title, abstract])
            elif item['Section'] == 'B':
                writeCSV(savDir + "B.json", ["2", title, abstract])
            elif item['Section'] == 'C':
                writeCSV(savDir + "C.json", ["3", title, abstract])
            elif item['Section'] == 'D':
                writeCSV(savDir + "D.json", ["4", title, abstract])
            elif item['Section'] == 'E':
                writeCSV(savDir + "E.json", ["5", title, abstract])
            elif item['Section'] == 'F':
                writeCSV(savDir + "F.json", ["6", title, abstract])
            elif item['Section'] == 'G':
                writeCSV(savDir + "G.json", ["7", title, abstract])
            elif item['Section'] == 'H':
                writeCSV(savDir + "H.json", ["8", title, abstract])
            # else:
            #     csv_file.writerow(['0', item['Title'].encode('utf-8'), item['Abstract'].encode('utf-8')])

def main():
    dest = "/home/jason/Documents/"
    savDir = "/home/jason/Documents/data/"
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
