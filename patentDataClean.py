#!/usr/bin/python
#coding:utf-8
'''
Created on Mar 2, 2016

@author: jason
'''
import os
from multiprocessing import Pool
from multiprocessing.dummy import Pool as ThreadPool

startTag = '<us-patent-grant lang="EN"'
endTag = '</us-patent-grant>'

SAVLIST = (('<application-reference', '</application-reference>'), ('<classification-ipcr>', '</classification-ipcr>'),
           ('<invention-title', '</invention-title>'), ('<assignee>', '</assignee>'),
           ('<abstract', '</abstract>'))

# for (start, end) in SAVLIST:
#     print start,end
def clear_data(text, directory):
    for line in text:
        flag = False
        flag0 = False
        flag1 = False
        flag2 = False
        flag3 = False
        flag4 = False

        if startTag in line:
            if not os.path.exists(directory):
                os.makedirs(directory)
            fileName = line[63:73]
            writeFileHandle = open(directory + fileName + '.xml', 'w+')
            writeFileHandle.write(line)

        if SAVLIST[0][0] in line:
            for content in text:
                if id(content) == id(line):#content与line指向的内存空间相同时
                    flag = True
                    flag0 = True
                    writeFileHandle.write(content)

                elif flag & ((SAVLIST[4][1] in content) | (endTag in content)):#判断当前处理的行是否为需要提取信息的最后一行
                    flag = False
                    last = content
                    break

                elif flag | flag4:
                    if flag0:
                        writeLine ='%s'%content
                        #print content
                        writeFileHandle.write(writeLine)
                        if SAVLIST[0][1] in content:
                            #writeFileHandle.write(content)
                            flag0 = False

                    if SAVLIST[1][0] in content:
                        flag1 = True
                    if flag1:
                        writeLine ='%s'%content
                        #print "找到:", content
                        writeFileHandle.write(writeLine)
                        if SAVLIST[1][1] in content:
                            #writeFileHandle.write(content)
                            flag1 = False

                    elif SAVLIST[2][0] in content:
                        flag2 = True
                        #writeFileHandle.write(content)
                    if flag2:
                        writeFileHandle.write(content)
                        if SAVLIST[2][1] in content:
                            flag2 = False
                    #     writeLine ='%s'%content
                    #     #print "找到:", content
                    #     writeFileHandle.write(writeLine)
                    #     if SAVLIST[2][1] in content:
                    #         #writeFileHandle.write(content)
                    #         flag2 = False

                    elif SAVLIST[3][0] in content:
                        flag3 = True
                        #writeFileHandle.write(content)
                    if flag3:
                        writeFileHandle.write(content)
                        if SAVLIST[3][1] in content:
                            #writeFileHandle.write(content)
                            flag3 = False
                    #
                    elif SAVLIST[4][0] in content:
                        flag4 = True
                        #writeFileHandle.write(content)
                    if flag4:
                        writeLine ='%s'%content
                        #print "找到:", content
                        writeFileHandle.write(writeLine)
                        if SAVLIST[4][1] in content:
                            #writeFileHandle.write(last)
                            flag4 = False
                            break
            if flag4:
                writeFileHandle.write(last)

        if endTag in line:
            #writeFileHandle.write(SAVLIST[4][1]+'\n')
            writeFileHandle.write(line)
            print fileName + '.xml has been saved!'

    # elif line != '':
    #     writeLine ='%s'%line
    #     writeFileHandle.write(writeLine)
    # else:
    #     print "匹配%d行失败，文件已到末尾"
    #     break
'''
if __name__ == '__main__':

    openFileHandle = open('Dataset/Temp.xml', 'r')
    directory = "Dataset/test/"
    text = openFileHandle.readlines()
    clear_data(text, directory)
    openFileHandle.close()
    #writeFileHandle.close()
# os.remove('filename')
# os.rename('Temp','filename')
    print "All Done!"

'''
