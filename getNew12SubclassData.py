#!/usr/bin/python
#coding:utf-8
'''
Created on May 24, 2016

@author: jason
'''
import pandas as pd
import glob
import csv
import os


readFile = r"/home/jason/Documents/data/NonLabels/"
writeDir = r"/home/jason/Documents/data/tensorFlowData/"

# def writeCSV(fileName, row):
#     with open(fileName, 'a+') as csvfile:
#         csv_writer = csv.writer(csvfile, quoting=csv.QUOTE_ALL)
#         csv_writer.writerow(row)

def getDataFrame(fileDir):

    column = ['section', 'title', 'abstract']
    frame = pd.DataFrame()
    list_ = []

    #frame.reindex(columns=['section', 'title', 'abstract'])
    frame = pd.concat(list_)
    #frame.reindex(columns=['section', 'title', 'abstract'])
    #print frame.groupby(['section']).agg(['count'])
    return frame

def writeCSV(df, fileName):
    df.to_csv(fileName, index=False, header=False, quoting=csv.QUOTE_ALL)


def main():
    #readCSV(readFile)

    fileNames = glob.glob(readFile + "/*.csv")


    charList = [chr(c) for c in range(65, 73)]
    charList.reverse()

    for file in fileNames:
        dir, fileName = os.path.split(file)
        print dir, fileName
        df = pd.read_csv(file, index_col=None)
        train = df.head(int(50000))
        writeCSV(train, writeDir + fileName)

        #print writeDir + charList.pop() +'.csv'
    #print grouped.get_group(1)
    # train_list = map(lambda x:x.lower(),[train_list])
    # test_list = map(lambda x:x.lower(),[test_list])
if __name__ == '__main__':
    main()


'''
The total rows of  1 class is : 331615
The total rows of  2 class is : 295085
The total rows of  3 class is : 279302
The total rows of  4 class is : 12950
The total rows of  5 class is : 43831
The total rows of  6 class is : 132144
The total rows of  7 class is : 696570
The total rows of  8 class is : 625299
'''