# -*- coding: utf-8 -*-
"""
Created on Mon Jun 04 11:02:01 2018

@author: evin
"""

def constructProjectionFileds(projectionFields, getID = False):
    """
    Constructs queryable projected fields dictionary for inputting find statement's project for mongodb 
    """
    fields = { }
    if not getID:
        fields["_id"] = 0
        
    for field in projectionFields:
        fields[field] = 1
        
    return fields

def constructQuery(userNames, sessions, relativeTime):
    """
    Constructs mongodb query dictionary for inputting find statement's query for mongodb
    @userNames : an array of usernames
    @sessions : an array of sessionIDs
    @relativeTime: an array of length two which indicates relative time interval (start, stop)
    """
    query = { }
    
    if userNames:
        query["userName"] = { "$in": userNames }
        
    if sessions:
        query["sessionID"] = { "$in": sessions }
        
    if relativeTime:
        query["relativeTime"] = { "$gt": relativeTime[0], "$lt": relativeTime[1] }
        
    #print query
    
    return query

def createUsersDict(userNameVariable, userNames, projectionFields, resultList):
    users = { }
    for userName in userNames:
        users[userName] = { }
        for field in projectionFields:
            if field != userNameVariable:
                users[userName][field] = [info[field] for info in resultList if info[userNameVariable] == userName]
    
    return users