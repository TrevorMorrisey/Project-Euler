# -*- coding: utf-8 -*-
"""
Created on Sat Oct 12 23:22:51 2019

@author: TrevorMorrisey
"""

def sumSquareDifference(number):
    sumOfSquares = 0
    sums = 0
    for index in range(1, number + 1):
        sumOfSquares += index**2
        sums += index
    
    squareOfSums = sums**2
    return squareOfSums - sumOfSquares
        
    
        