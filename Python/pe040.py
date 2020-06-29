#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Nov 20 19:02:25 2019

@author: trevor
"""

import peUtilities

def getMultiple():
    champernownesString = getChampernownes(1000000)
    mult = int(champernownesString[1]) * int(champernownesString[10]) * int(champernownesString[100]) * int(champernownesString[1000]) * int(champernownesString[10000]) * int(champernownesString[100000]) * int(champernownesString[1000000])
    return mult

def getChampernownes(digit):
    counter = 0
    number = 1
    string = '0'
    while counter < digit:
        string += str(number)
        counter += len(peUtilities.integerToList(number))
        number += 1
    return string