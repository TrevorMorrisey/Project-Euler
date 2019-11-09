# -*- coding: utf-8 -*-
"""
Created on Sat Nov  9 16:52:43 2019

@author: TrevorMorrisey
"""

import peUtilities

def pentagonNumbers():
    # Cycle through all pentagonal numbers while saving each one
    pentagonNums = []
    for num in peUtilities.yieldPentagonNum():
        # Check if pentagonal number can be made by subtracting any existing value from each new number
        for prevNum in pentagonNums:
            if (num - prevNum) in pentagonNums:
                # If so, check if sum if also pentagonal
                if peUtilities.isPentagonal(num + prevNum):
                    return (num, prevNum)
        pentagonNums.append(num)
    