# -*- coding: utf-8 -*-
"""
Created on Mon Oct 14 22:33:28 2019

@author: TrevorMorrisey
"""

import math

def getFibNumber(index, fibDict):
    #fibDict = {0:1, 1:2}
    if index in fibDict:
        return fibDict[index]
    else:
        fibDict[index] = getFibNumber(index - 1, fibDict) + getFibNumber(index - 2, fibDict)
        return fibDict[index]
    
def getFactors(number):
    #upperBound = number - 1
    index = 1
    factors = []
    
    while index <= math.sqrt(number):
        if number % index == 0:
            factors.append(index)
            factors.append(number // index)
            #upperBound = number / index
        index += 1
    
    return factors

def isPrime(number):
    if number == 1:
        return False
    elif number == 2:
        return True
    elif number % 2 == 0:
        return False
    
    index = 3
    while index <= math.sqrt(number):
        if number % index == 0:
            return False
        index += 2
    
    return True

def convertNumStringToList(string):
    numList = string.split(' ')

    for i in range(len(numList)):
        numList[i] = int(numList[i])
    
    return numList

def isPalindrome(string):
    if len(string) == 1 or len(string) == 0:
        return True
    elif len(string) == 2:
        return string[0] == string[1]
    else:
        if string[0] != string[len(string) - 1]:
            return False
        else:
            return isPalindrome(string[1:len(string) - 1])
        
