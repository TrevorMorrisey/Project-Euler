# -*- coding: utf-8 -*-
"""
Created on Sat Oct 12 20:01:37 2019

@author: TrevorMorrisey
"""

def evenFibonacciNumbers(upperBound):
    fibDict = {0:1, 1:2}
    
    def getFibNumber(index):
        if index in fibDict:
            return fibDict[index]
        else:
            fibDict[index] = getFibNumber(index - 1) + getFibNumber(index - 2)
            return fibDict[index]
            
    sum = 0
    currentFibNum = 0
    index = 0
    while True:
        currentFibNum = getFibNumber(index)
        if currentFibNum > upperBound:
            break
        elif currentFibNum % 2 == 0:
            sum += currentFibNum
        index += 1

    return sum