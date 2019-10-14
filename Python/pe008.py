# -*- coding: utf-8 -*-
"""
Created on Sat Oct 12 23:37:08 2019

@author: TrevorMorrisey
"""

def largestProductInSeries(numberString, digits):
    highestSum = 0
    for i in range(len(numberString) - digits):
        currentSum = 1
        for j in range(digits):
            currentSum *= int(numberString[i + j])
        if currentSum > highestSum:
            highestSum = currentSum
    return highestSum