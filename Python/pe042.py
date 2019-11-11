# -*- coding: utf-8 -*-
"""
Created on Sat Nov  9 17:38:01 2019

@author: TrevorMorrisey
"""

import peUtilities

def countTriangleWords(fileName):
    # Read all strigs from file into a list
    f = open(fileName)
    wordList = []
    for line in f:
        wordList = line.split(',')
    f.close()
    
    # Remove quotation characters from strings and make them lowercase
    for i in range(len(wordList)):
        wordList[i] = wordList[i][1:-1].lower()
    
    #return wordList
    # Get string values and check if each value is a triangle number
    triangleWordCount = 0
    for word in wordList:
        value = peUtilities.getWordValue(word)
        if peUtilities.isTriangular(value):
            triangleWordCount += 1
    
    return triangleWordCount