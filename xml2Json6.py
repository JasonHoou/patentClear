#!/usr/bin/python
#coding:utf-8
'''
Created on May 23, 2016

@author: jason
'''
import json as js
import os
import xml.dom.minidom
import xml.etree.ElementTree as ET

patentInfo = []

def getFileNamme(destDir):

    #Get all files
    names = [name for name in os.listdir(destDir)
        if name.endswith('.xml')]
        #if os.path.isfile(os.path.join(destDir, name))]
    return names

def getDirName(dest):

    # Get all dirs
    dirnames = [name for name in os.listdir(dest)
        if os.path.isdir(os.path.join(dest, name))]
    return dirnames

def getXmlInfo(fileName):
    classificationList = []
    DOMTree = xml.dom.minidom.parse(fileName)
    patent = DOMTree.documentElement

    tree = ET.parse(fileName)
    root = tree.getroot()

    #Get Patent Classification
    try:
        for classification in root.findall('./classifications-ipcr/classification-ipcr'):
            section = classification.find('section').text
            mainclass = classification.find('class').text
            subclass = classification.find('subclass').text
            main_group = classification.find('main-group').text
            subgroup = classification.find('subgroup').text

            #print section, p_class, subclass, main_group, subgroup
            classificationList.append([section, mainclass, subclass, main_group, subgroup])
            #print classificationList
    except IndexError:
        section = ''
        mianclass = None
        subclass = None
        main_group = None
        subgroup = None
        print "----error! No classification Info!----"

    # Get Patent Number
    if patent.hasAttribute("file"):
        patentNo = patent.getAttribute("file")[0:10]
        print patentNo
    else:
        patentNo = None

    #Get Patent Type
    patentRef = patent.getElementsByTagName("application-reference")[0]
    if patentRef.hasAttribute("appl-type"):
        type = patentRef.getAttribute("appl-type")
    else:
        type = None

    # #Get Patent Classification
    # try:
    #     patentSection = patent.getElementsByTagName("section")[0]
    #     patentClass = patent.getElementsByTagName("class")[0]
    #     patentSubclass = patent.getElementsByTagName("subclass")[0]
    #     patentMainGroup = patent.getElementsByTagName("main-group")[0]
    #     patentSubgroup = patent.getElementsByTagName("subgroup")[0]
    #     section = patentSection.childNodes[0].data
    #     mianclass = patentClass.childNodes[0].data
    #     subclass = patentSubclass.childNodes[0].data
    #     maingroup = patentMainGroup.childNodes[0].data
    #     subgroup = patentSubgroup.childNodes[0].data
    # except IndexError:
    #     section = ''
    #     mianclass = None
    #     subclass = None
    #     maingroup = None
    #     subgroup = None
    #     print "----error! No classification Info!----"

    #Get Patent Title
    try:
        patentTitle = patent.getElementsByTagName("invention-title")[0]
        title = patentTitle.childNodes[0].data
    except AttributeError:
        title = None
        print "----error! No patentTitle Info!----"

    #Get Patent Assignee
    try:
        patentOrgname = patent.getElementsByTagName("orgname")[0]
        patentCountry = patent.getElementsByTagName("country")[0]
        patentCity = patent.getElementsByTagName("city")[0]
        orgname = patentOrgname.childNodes[0].data
        country = patentCountry.childNodes[0].data
        city = patentCity.childNodes[0].data
    except IndexError:
        orgname = None
        country = None
        city = None
        print "----error! No assignee Info!----"

    #Get Patent Abstract
    try:
        patentAbs = patent.getElementsByTagName("p")[0]
        abstract = ''
        # patentAbs.removeChild("b")
        # patentAbs.removeChild("i")
        #print patentAbs.normalize()
        x = patentAbs.childNodes
        for i in x:
            if i.nodeType == 3:
                abstract += i.data
    except IndexError:
        abstract = ''
        print "----error! No Abstract Info!----"

    return patentNo, type, title, classificationList, abstract, orgname, country, city

def convertToJSON(fileDir):
    patentNo, type, title, classificationList, abstract, orgname, country, city = getXmlInfo(fileDir)
    #print len(section), len(abstract), (len(section)!=0), (len(abstract)!=0)

    if (len(classificationList) != 0) & (len(abstract) != 0):
        for item in classificationList:
            patentInfo.append(
                    {'No.': patentNo, 'Title': title, 'Type': type, 'Section': item[0], 'Mianclass': item[1],
                               'Subclass':item[2],'Maingroup':item[3], 'Subgroup':item[4], 'Abstract': abstract,
                               'Orgname':orgname, 'Country':country, 'City':city}
            )
    #print js.dumps(patentInfo, indent=4)
    #file.write(js.dumps(posts_list, indent=4))
    return patentInfo

def writeToJSONFile(fileName,patentInfo):
    with open(fileName, 'w') as file:
        file.write(js.dumps(patentInfo, indent=4))
    #print json.dumps({'poster':item[0], 'time':item[1],'ID':item[2], 'message':clean_list}, file, indent=4)

def main():
    #dest = "testDataset/"
    #filename = "test.json"
    dest = "/home/jason/Documents/data/2005/"
    filename = "/home/jason/Documents/2005patentsInfo.json"
    #dirnames = getDirName(dest)
    #print destDir
    fileNames = getFileNamme(dest)

    for fileName in fileNames:
        fileDir = dest + fileName
        #getXmlInfo(fileDir)
        convertToJSON(fileDir)
        if fileName == fileNames[-1]:
            writeToJSONFile(filename, convertToJSON(fileDir))
        #print fileNames
    print  "#### Well Done! ####"


if __name__ == "__main__":
    main()
