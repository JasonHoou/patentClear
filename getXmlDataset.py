#!/usr/bin/python
#coding:utf-8
'''
Created on Mar 2, 2016

@author: jason
'''


import zipfile
import os
#import patentDataClean as pdc
import shutil


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


def getFileNamme(destDir,extName):

    #Get all files
    names = [name for name in os.listdir(destDir)
        if name.endswith(extName)]
        #if os.path.isfile(os.path.join(destDir, name))]
    return names

def getDirName(dest):

    # Get all dirs
    dirnames = [name for name in os.listdir(dest)
        if os.path.isdir(os.path.join(dest, name))]
    return dirnames

def un_zip(file_name):
    """unzip zip file"""
    zip_file = zipfile.ZipFile(file_name)
    if os.path.isdir(file_name + "_files"):
        pass
    else:
        os.mkdir(file_name + "_files")
    for names in zip_file.namelist():
        zip_file.extract(names, file_name + "_files")
    zip_file.close()
    xmlDir = file_name + "_files/"
    return xmlDir



def main():
    destDir = "/home/jason/Documents/data/PatentsFullText/2014/"
    #filename = dest + "/patentsInfo1.json"
    fileNames = getFileNamme(destDir, '.zip')

    for fileName in fileNames:
        fileName = destDir + fileName
        savDir = "/home/jason/Documents/data/2014/"
        directory = un_zip(fileName)

        #os.system("rm -rf " + directory)
        #os.removedirs(directory)

        for xmlFile in getFileNamme(directory, '.xml'):
            print xmlFile
            openFileHandle = open(directory + xmlFile, 'r')
            text = openFileHandle.readlines()
            clear_data(text, savDir)
            openFileHandle.close()

            shutil.rmtree(directory) #delete the file after use
        #writeFileHandle.close()
    # os.remove('filename')
    # os.rename('Temp','filename')
        print "All Done!"

if __name__ == "__main__":
    main()

