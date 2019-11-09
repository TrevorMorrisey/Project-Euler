# -*- coding: utf-8 -*-
"""
Created on Sat Nov  9 13:53:49 2019

@author: TrevorMorrisey
"""

import peUtilities

def findMultiShapeNumber():
    #triangleNums = []
    #pentagonNums = []
    #hexagonNums = []
#    triangleDict = {}
#    pentagonDict = {}
#    heaxgonDict = {}
    
    triangleGenerator = peUtilities.yieldTriangleNum()
    pentagonGenerator = peUtilities.yieldPentagonNum()
    hexagonGenerator = peUtilities.yieldHexagonNum()
    
    #triangleNums.append(next(triangleGenerator))
    #pentagonNums.append(next(pentagonGenerator))
    #hexagonNums.append(next(hexagonGenerator))
#    numsToGenerate = 10000
#    for i in range(numsToGenerate):
#        triangleDict[next(triangleGenerator)] = True
#        pentagonDict[next(pentagonGenerator)] = True
#        heaxgonDict[next(hexagonGenerator)] = True
    
    number = 1
    currentTriangleNum = next(triangleGenerator)
    currentPentagonNum = next(pentagonGenerator)
    currentHexagonNum = next(hexagonGenerator)
    while True:
        #print("Checking " + str(number))
#        if (number > triangleNums[len(triangleNums) - 1]):
#            triangleNums.append(next(triangleGenerator))
#        
#        if (number > pentagonNums[len(pentagonNums) - 1]):
#            pentagonNums.append(next(pentagonGenerator))
#        
#        if (number > hexagonNums[len(hexagonNums) - 1]):
#            hexagonNums.append(next(hexagonGenerator))
    
#        if number in triangleNums and number in pentagonNums and number in hexagonNums:
#            if number != 1 and number != 40755:
#                return number
#            else:
#                number += 1
#        try:
#            if triangleDict[number] and pentagonDict[number] and heaxgonDict[number]:
#                if number != 1 and number != 40755:
#                    return number
#                else:
#                    number += 1
#            else:
#                number += 1
#        except:
#            number += 1
        if number > currentTriangleNum:
            currentTriangleNum = next(triangleGenerator)
        if number > currentPentagonNum:
            currentPentagonNum = next(pentagonGenerator)
        if number > currentHexagonNum:
            currentHexagonNum = next(hexagonGenerator)
            
        if number == currentTriangleNum and number == currentPentagonNum and number == currentHexagonNum:
            if number != 1 and number != 40755:
                return number
        
        number += 1
            
            