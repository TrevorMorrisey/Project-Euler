# -*- coding: utf-8 -*-
"""
Created on Mon Jun 29 14:38:25 2020

@author: TrevorMorrisey
"""

import peUtilities

def getPandigitalProduct():
    """
    Get all 9 digit pandigital numbers
    Go through them in descending order
    For each number, for each integer less than 10000, check if integer can be used to create pandigital
    """
    #pandigitals = []
#    for i in range(100000000, 999999999):
    for i in range(987654321, 123456788, -1):
        if isPandigital(i):
            if isConcatination(i):
                return i
            #print(i)
            #pandigitals.append(i)
    #print(len(pandigitals))

def isPandigital(number):
    numList = peUtilities.integerToList(number)
    for i in range(len(numList)):
        if not containsNumber(numList, i + 1):
            return False
    return True

def containsNumber(numList, number):
    for digit in numList:
        if digit == number:
            return True
    return False

def isConcatination(number):
    