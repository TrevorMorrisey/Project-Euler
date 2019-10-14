# -*- coding: utf-8 -*-
"""
Created on Sat Oct 12 23:46:17 2019

@author: TrevorMorrisey
"""
import math

def pythagoreanTriplet():
    for i in range(1, 500):
        for j in range(1, 500):
            root = math.sqrt((i**2) + (j**2))
            if (root + i + j) == 1000:
                print('a: ' + str(i))
                print('b: ' + str(j))
                print('c: ' + str(root))
                return root * i * j
    print('Failed to find triplet')