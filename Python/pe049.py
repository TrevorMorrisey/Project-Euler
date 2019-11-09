# -*- coding: utf-8 -*-
"""
Created on Sat Nov  9 11:43:11 2019

@author: TrevorMorrisey
"""

import peUtilities

def primePermutations():
#    primes = []
#    for i in peUtilities.yieldPrime():
#        if i >= 1000:
#            if i < 10000:
#                primes.append(i)
#            else:
#                break
            
#    sequences = []
#    for i in range(0, len(primes) - 2):
#        for j in range(i + 1, len(primes) - 2):
#            for k in range(j + 1, len(primes) - 1):
#                number1 = primes[i]
#                number2 = primes[j]
#                number3 = primes[k]
#                if peUtilities.isPermutation(number1, number2) and peUtilities.isPermutation(number1, number3):
#                    #return (number1, number2, number3)
#                    sequences.append((number1, number2, number3))
#    
#    return sequences
    sequences = []
    for i in range(0, 3341):
        if peUtilities.isPrime(i):
            if peUtilities.isPrime(i + 3330):
                if peUtilities.isPrime(i + 6660):
                    if peUtilities.isPermutation(i, (i + 3330)) and peUtilities.isPermutation(i, (i + 6660)):
                        sequences.append((i, (i + 3330), (i + 6660)))
                        
    return sequences