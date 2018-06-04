# -*- coding: utf-8 -*-
"""
Created on Mon Jun 04 10:35:26 2018

@author: evin
"""
import os

def getAbsPath(fileName):
    """
    returns absolute path of a given fileName
    """
    APP_FOLDER = os.getcwd()#path.dirname(os.path.realpath(sys.argv[0]))
    filePath = os.path.join(APP_FOLDER, fileName)
    return filePath

def traceToFile(traceEnabled, traceFileName, inputString):
    """
    Writes inputString to the file named traceFileName if trace is Enabled,
    prints the inputString to the shell otherwise    
    """
    if traceEnabled:
        traceFileName.write("{}".format(inputString))
    else:
        print "{}".format(inputString)
        
def traceToFileEOL(traceEnabled, traceFileName, inputString):
    """
    Writes inputString followed by a new line to the file named traceFileName
    if trace is enabled, prints the inputString to the shell otherwise    
    """
    if traceEnabled:
        traceFileName.write("{}".format(inputString) + "\n")
    else:
        print "{}".format(inputString) + "\n"

def traceToFileLists(traceEnabled, traceFileName, itemList, listName, itemName):
    """
    Writes the elements of itemList with the itemListName followed by each
    element with the itemName tag, provided that it is not empty
    """
    if itemList:
        traceToFileEOL(traceEnabled, traceFileName, listName)
        for item in itemList:
            traceToFileEOL(traceEnabled, traceFileName, itemName + str(item))
        traceToFileEOL(traceEnabled, traceFileName, "")
        
def tracetoUsersExpDesVariables(traceEnabled, traceFileName, userName):
    """
    Writes given parameters associated with userName to the file
    """
    traceToFileEOL(traceEnabled, traceFileName, userName) 
    traceToFileEOL(traceEnabled, traceFileName, "")