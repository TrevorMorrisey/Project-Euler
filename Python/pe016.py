#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Nov 11 16:46:48 2019

@author: trevor
"""

import peUtilities

def powerDigitSum(power):
    number = 2**power
    numList = peUtilities.integerToList(number)
    digitSum = 0
    for digit in numList:
        digitSum += digit
    return digitSum