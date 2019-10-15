# -*- coding: utf-8 -*-
"""
Created on Mon Oct 14 22:58:31 2019

@author: TrevorMorrisey
"""

def longestCollatzSequence():
    mostIterations = 0
    mostIterationsNum = -1
    counter = 1
    while counter < 1000000:
        currentNum = counter
        iterations = 0
        while currentNum != 1:
            if (currentNum % 2 == 0):
                currentNum = currentNum / 2
            else:
                currentNum = (currentNum * 3) + 1
            iterations += 1
        if iterations > mostIterations:
            mostIterations = iterations
            mostIterationsNum = counter
        counter += 1
    return mostIterationsNum
            