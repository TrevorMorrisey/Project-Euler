# -*- coding: utf-8 -*-
"""
Created on Sun Oct 13 00:01:14 2019

@author: TrevorMorrisey
"""

def sumOfPrimes(upperBound):
    total = 0
    for i in range(2, upperBound):
        print(i)
        if isPrime(i):
            total += i
    return total

def isPrime(number):
#    if number == 1:
#        return False
    #upperBound = number - 1
    index = 2
    #factors = []
    
    while index < number:
        if number % index == 0:
            return False
            #factors.append(index)
            #upperBound = number / index
        index += 1
    
    return True