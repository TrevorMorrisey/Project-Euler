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
    index = 1
    factors = []
    
    while index <= math.sqrt(number):
        if number % index == 0:
            factors.append(index)
            #factors.append(number // index)
            if (number // index) != index:
                factors.append(number // index)
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

def yieldPrime():
    counter = 2
    while True:
        if isPrime(counter):
            yield counter
        counter += 1

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
        
def integerToList(number):
    numList = []
    numString = str(number)
    for digit in numString:
        numList.append(int(digit))
    return numList

def isPermutation(number1, number2):
    list1 = integerToList(number1)
    list2 = integerToList(number2)
    
    if len(list1) != len(list2):
        return False
    
    list1.sort()
    list2.sort()
    
    for i in range(len(list1)):
        if list1[i] != list2[i]:
            return False
    
    return True

def isSquare(number):
    root = math.sqrt(number)
    return root == int(root)

def isTriangular(number):
    for triangle in yieldTriangleNum():
        if triangle > number:
            return False
        if triangle == number:
            return True
        
def isPentagonal(number):
    for pentagon in yieldPentagonNum():
        if pentagon > number:
            return False
        if pentagon == number:
            return True

def isHexagonal(number):
    for hexagon in yieldHexagonNum():
        if hexagon > number:
            return False
        if hexagon == number:
            return True
    
def yieldTriangleNum():
    counter = 0
    while True:
        counter += 1
        triangle = counter + 1
        triangle *= counter
        triangle /= 2
        yield int(triangle)

def yieldPentagonNum():
    counter = 0
    while True:
        counter += 1
        pentagon = 3 * counter
        pentagon -= 1
        pentagon *= counter
        pentagon /= 2
        yield int(pentagon)
        
def yieldHexagonNum():
    counter = 0
    while True:
        counter += 1
        hexagon = 2 * counter
        hexagon -= 1
        hexagon *= counter
        yield int(hexagon)       
        
        





    
    