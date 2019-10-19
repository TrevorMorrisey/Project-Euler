# -*- coding: utf-8 -*-
"""
Created on Fri Oct 18 19:19:32 2019

@author: TrevorMorrisey
"""

def maximumPathSum(lists):
    currentValues = []
    previousValues = lists[len(lists) - 1]
    for i in range(len(lists) - 1, 0, -1):
        currentValues = lists[i - 1]
        for j in range(len(currentValues)):
            if previousValues[j] >= previousValues[j + 1]:
                currentValues[j] += previousValues[j]
            else:
                currentValues[j] += previousValues[j + 1]
        previousValues = currentValues;
    return previousValues