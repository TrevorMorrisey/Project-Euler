# -*- coding: utf-8 -*-
"""
Created on Sat Oct 12 21:46:40 2019

@author: TrevorMorrisey
"""

def smallestMultiple(highestFactor):
    counter = highestFactor
    while True:
        divisible = True
        for i in range(1, highestFactor + 1):
            if counter % i != 0:
                divisible = False
        if divisible:
            return counter
        else:
            counter += 1