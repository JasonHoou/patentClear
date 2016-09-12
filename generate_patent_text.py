#!/usr/bin/python
#coding:utf-8
'''
Created on June 22, 2016

@author: jason
'''
import os
import json as js
import re

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

def json2txt(savDir, data):
    for item in data:
        if item['Title'] is not None and item['Abstract'] is not None:
            title = str(item['Title'].strip().replace('\n', '').encode('utf-8')).lower()
            #title = ''' + title + '''
            abstract = str(item['Abstract'].strip().replace('\n', '').encode('utf-8')).lower()
            text = re.sub(r'[^\w\s]','',title) + re.sub(r'[^\w\s]','',abstract)
            writeText(savDir + "/patentText.txt", text)


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
            json2txt(savDir, data)
            #print fileNames
    print  "#### Well Done! ####"

if __name__ == "__main__":
    main()

