#!/usr/bin/python
#coding:utf-8
'''
Created on May 30, 2016

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
    charList = [chr(c) for c in range(65, 73)]
    for item in data:
        if item['Title'] is not None and item['Abstract'] is not None and item['Section'] in charList:
            title = str(item['Title'].strip().replace('\n', '').encode('utf-8')).lower()
            #title = ''' + title + '''
            abstract = str(item['Abstract'].strip().replace('\n', '').encode('utf-8')).lower()
            label = str(item['Section']) + '-' + str(item['Mianclass'])
            writeCSV(savDir + "2006_2014Classes.csv", [label, title, abstract])

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
