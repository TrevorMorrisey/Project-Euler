# -*- coding: utf-8 -*-
"""
Created on Mon Oct 14 22:40:18 2019

@author: TrevorMorrisey
"""

import peUtilities

def highlyDivisibleTriangularNumber():
    index = 1
    counter = 0
    while True:
        counter = index
        currentSum = 0
        while counter > 0:
            currentSum += counter
            counter -= 1
        if len(peUtilities.getFactors(currentSum)) > 500:
            return currentSum
        else:
            index += 1