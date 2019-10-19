# -*- coding: utf-8 -*-
"""
Created on Fri Oct 18 22:49:39 2019

@author: TrevorMorrisey
"""

import peUtilities

def getFibNumWithDigits(digitCount):
    index = 2
    fibDict = { 0:1, 1:1 }
    while True:
        currentNum = peUtilities.getFibNumber(index, fibDict)
        if len(str(currentNum)) >= digitCount:
            return index
        else:
            index += 1