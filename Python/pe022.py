# -*- coding: utf-8 -*-
"""
Created on Fri Oct 18 21:50:19 2019

@author: TrevorMorrisey
"""

def readNames(fileName, letterValues):
    f = open(fileName)
    nameList = []
    for line in f:
        nameList = line.split(',')
    f.close()
    for i in range(len(nameList)):
        nameList[i] = nameList[i][1:-1]
    nameList.sort()
    #return nameList
    totalScore = 0
    for i in range(len(nameList)):
        totalScore += getNameScore(nameList[i].lower(), i + 1, letterValues)
    return totalScore
    
def getNameScore(name, index, letterValues):
    score = 0
    for letter in name:
        score += letterValues[letter]
    score *= index
    return score
    
letterValues = { 'a': 1,
                 'b': 2,
                 'c': 3,
                 'd': 4,
                 'e': 5,
                 'f': 6,
                 'g': 7,
                 'h': 8,
                 'i': 9,
                 'j': 10,
                 'k': 11,
                 'l': 12,
                 'm': 13,
                 'n': 14,
                 'o': 15,
                 'p': 16,
                 'q': 17,
                 'r': 18,
                 's': 19,
                 't': 20,
                 'u': 21,
                 'v': 22,
                 'w': 23,
                 'x': 24,
                 'y': 25,
                 'z': 26,
                 }