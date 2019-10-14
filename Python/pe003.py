# -*- coding: utf-8 -*-
"""
Created on Sat Oct 12 20:22:48 2019

@author: TrevorMorrisey
"""

def largestPrimeFactor(number):
    factors = getFactors(number)
    currentHighestPrime = 0
    for num in factors:
        if (len(getFactors(num)) == 0):
            if num > currentHighestPrime:
                currentHighestPrime = num
    
    # If the function returns 0, there are no prime factors
    return currentHighestPrime

def getFactors(number):
    upperBound = number
    index = 2
    factors = []
    
    while index < upperBound:
        if number % index == 0:
            factors.append(index)
            upperBound = number / index
        index += 1
    
    return factors