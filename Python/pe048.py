# -*- coding: utf-8 -*-
"""
Created on Sat Nov  9 12:15:30 2019

@author: TrevorMorrisey
"""

def selfPowers(seriesLength):
    total = 0
    for i in range(1, seriesLength + 1):
        #print(str(i))
        #print(str(i**i))
        total += i**i
    return total