#!/usr/bin/python
#coding:utf-8
'''
Created on Mar 3, 2016

@author: jason
'''
import json as js
import os
import xml.dom.minidom
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

    DOMTree = xml.dom.minidom.parse(fileName)
    patent = DOMTree.documentElement

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

    #Get Patent Classification
    try:
        patentSection = patent.getElementsByTagName("section")[0]
        patentClass = patent.getElementsByTagName("class")[0]
        patentSubclass = patent.getElementsByTagName("subclass")[0]
        patentMainGroup = patent.getElementsByTagName("main-group")[0]
        patentSubgroup = patent.getElementsByTagName("subgroup")[0]
        section = patentSection.childNodes[0].data
        mianclass = patentClass.childNodes[0].data
        subclass = patentSubclass.childNodes[0].data
        maingroup = patentMainGroup.childNodes[0].data
        subgroup = patentSubgroup.childNodes[0].data
    except IndexError:
        section = ''
        mianclass = None
        subclass = None
        maingroup = None
        subgroup = None
        print "----error! No classification Info!----"

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

    return patentNo, type, title, section, mianclass, subclass, maingroup, subgroup, abstract, orgname, country, city

def convertToJSON(fileDir):
    patentNo, type, title, section, mianclass, subclass, maingroup, subgroup, abstract, orgname, country, city = getXmlInfo(fileDir)
    #print len(section), len(abstract), (len(section)!=0), (len(abstract)!=0)

    if (len(section) != 0) & (len(abstract) != 0):
        patentInfo.append(
                {'No.': patentNo, 'Title': title, 'Type': type, 'Section': section, 'Mianclass': mianclass,
                           'Subclass':subclass,'Maingroup':maingroup, 'Subgroup':subgroup, 'Abstract': abstract,
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
    dest = "/home/jason/Documents/data/2008/"
    filename = "/home/jason/Documents/2008patentsInfo.json"
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