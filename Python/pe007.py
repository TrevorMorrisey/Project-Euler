# -*- coding: utf-8 -*-
"""
Created on Sat Oct 12 23:28:55 2019

@author: TrevorMorrisey
"""

def getPrimeNumer(index):
    primes = 0
    counter = 2
    while True:
        if len(getFactors(counter)) == 0:
            primes += 1
            if primes == index:
                return counter
        counter += 1

def getFactors(number):
    upperBound = number - 1
    index = 2
    factors = []
    
    while index <= upperBound:
        if number % index == 0:
            factors.append(index)
            upperBound = number / index
        index += 1
    
    return factors