#!/usr/bin/python
#coding:utf-8
'''
Created on June 2, 2016

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
            if item['Section'] == 'G' and item['Mianclass'] == '06' and item['Subclass'] == 'F':
                writeCSV(savDir + "G_06_F.csv", [ title, abstract])

            elif item['Section'] == 'H' and item['Mianclass'] == '01' and item['Subclass'] == 'L':
                writeCSV(savDir + "H_01_L.csv", [title, abstract])

            elif item['Section'] == 'A' and item['Mianclass'] == '61' and item['Subclass'] == 'K':
                writeCSV(savDir + "A_61_K.csv", [title, abstract])

            elif item['Section'] == 'H' and item['Mianclass'] == '04' and item['Subclass'] == 'N':
                writeCSV(savDir + "H_04_N.csv", [title, abstract])

            elif item['Section'] == 'H' and item['Mianclass'] == '04' and item['Subclass'] == 'L':
                writeCSV(savDir + "H_04_L.csv", [title, abstract])

            elif item['Section'] == 'A' and item['Mianclass'] == '61' and item['Subclass'] == 'B':
                writeCSV(savDir + "A_61_B.csv", [title, abstract])

            elif item['Section'] == 'G' and item['Mianclass'] == '06' and item['Subclass'] == 'K':
                writeCSV(savDir + "G_06_K.csv", [title, abstract])

            elif item['Section'] == 'H' and item['Mianclass'] == '04' and item['Subclass'] == 'B':
                writeCSV(savDir + "H_04_B.csv", [title, abstract])

            elif item['Section'] == 'C' and item['Mianclass'] == '07' and item['Subclass'] == 'D':
                writeCSV(savDir + "C_07_D.csv", [title, abstract])

            elif item['Section'] == 'G' and item['Mianclass'] == '01' and item['Subclass'] == 'N':
                writeCSV(savDir + "G_01_N.csv", [title, abstract])

            elif item['Section'] == 'C' and item['Mianclass'] == '12' and item['Subclass'] == 'N':
                writeCSV(savDir + "C_12_N.csv", [title, abstract])

            elif item['Section'] == 'G' and item['Mianclass'] == '02' and item['Subclass'] == 'B':
                writeCSV(savDir + "G_02_B.csv", [title, abstract])

            # else:
            #     csv_file.writerow(['0', item['Title'].encode('utf-8'), item['Abstract'].encode('utf-8')])

def main():
    dest = "/home/jason/Documents/"
    savDir = "/home/jason/Documents/data/NonLabels"
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

