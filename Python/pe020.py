#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Nov 20 18:31:46 2019

@author: trevor
"""

import peUtilities

def factorialDigitSum(number):
    total = 1
    for i in range(number, 0, -1):
        total *= i
    numList = peUtilities.integerToList(total)
    digitSum = 0
    for j in range(len(numList)):
        digitSum += numList[j]
    return digitSum