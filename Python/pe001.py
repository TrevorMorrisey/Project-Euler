# -*- coding: utf-8 -*-
"""
Created on Sat Oct 12 19:54:01 2019

@author: TrevorMorrisey
"""

def multiplesOfThreeAndFive(bound):
    sum = 0
    for num in range(1, bound):
        if (num % 3 == 0) or (num % 5 == 0):
            sum += num
    return sum