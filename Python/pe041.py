# -*- coding: utf-8 -*-
"""
Created on Mon Jun 29 13:53:20 2020

@author: TrevorMorrisey
"""

import peUtilities

def getPandigitalPrime():
    for prime in peUtilities.yieldPrime():
        if isPandigital(prime):
            print(prime)
        
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