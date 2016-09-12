#!/usr/bin/python
#coding:utf-8
'''
Created on May 24, 2016

@author: jason
'''
import pandas as pd
import glob
import csv


readFile = r"/home/jason/Documents/data/12classes/"
writeDir = r"/home/jason/Documents/data/"

# def writeCSV(fileName, row):
#     with open(fileName, 'a+') as csvfile:
#         csv_writer = csv.writer(csvfile, quoting=csv.QUOTE_ALL)
#         csv_writer.writerow(row)

def getDataFrame(fileDir):
    allFiles = glob.glob(fileDir + "/*.csv")
    column = ['section', 'title', 'abstract']
    frame = pd.DataFrame()
    list_ = []
    for file_ in allFiles:
        df = pd.read_csv(file_, index_col=None, names=column)
        print df.columns
        list_.append(df)
    #frame.reindex(columns=['section', 'title', 'abstract'])
    frame = pd.concat(list_)
    #frame.reindex(columns=['section', 'title', 'abstract'])
    #print frame.groupby(['section']).agg(['count'])
    return frame

def writeCSV(df, fileName):
    df.to_csv(fileName, index=False, header=False, quoting=csv.QUOTE_ALL)


def main():
    #readCSV(readFile)
    df = getDataFrame(readFile)
    grouped = df.groupby(['section'])
    charList = [chr(c) for c in range(65, 73)]
    charList.reverse()
    train_list = []
    test_list = []
    for i in range(12):
        temp = grouped.get_group(i + 1)
        total_row = temp.shape[0]
        print "The total rows of ", i+1, "class is :", total_row
        test_part = temp.head(int(0.1 * 49743))
        train_part = temp.tail(int(0.9 * 50000))
        # test_part = temp.head(int(0.1 * total_row))
        # train_part = temp.tail(int(0.9 * total_row))
        train_list.append(train_part)
        test_list.append(test_part)
        #print writeDir + charList.pop() +'.csv'
    #print grouped.get_group(1)
    # train_list = map(lambda x:x.lower(),[train_list])
    # test_list = map(lambda x:x.lower(),[test_list])
    train = pd.concat(train_list)
    test = pd.concat(test_list)
    writeCSV(train, writeDir + '12classes_90_train.csv')
    writeCSV(test, writeDir + '12classes_10_test.csv')

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