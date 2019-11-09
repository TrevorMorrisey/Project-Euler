# -*- coding: utf-8 -*-
"""
Created on Sat Nov  9 12:24:14 2019

@author: TrevorMorrisey
"""

import peUtilities

def distinctPrimeFactors(factorCount):
    counter = 2
    while True:
        factors = peUtilities.getFactors(counter)
        primeFactors = countPrimes(factors)
        if primeFactors >= factorCount:
            allFactor = True
            for i in range(counter, counter + factorCount):
                factors = peUtilities.getFactors(i)
                primeFactors = countPrimes(factors)
                if primeFactors < factorCount:
                    allFactor = False
            if allFactor:
                return counter
        counter += 1
    
def countPrimes(numList):
    count = 0
    for num in numList:
        if peUtilities.isPrime(num):
            count += 1
    return count