# -*- coding: utf-8 -*-
"""
Created on Sat Nov  9 13:27:58 2019

@author: TrevorMorrisey
"""

import peUtilities

def disproveGoldbachs():
    # Cycle through odd composite numbers
    for composite in yieldOddComposite():
        # Cycle through prime numbers lower than the composite number
        for prime in peUtilities.yieldPrime():
            # If no solution has been found when the prime reaches the composite, this number disproves conjecture
            if prime >= composite:
                return composite
            
            # For each prime, get the remainder of the composite number minus the prime
            remainder = composite - prime
            
            # Halve that number
            remainder = remainder / 2
            
            # If result is square, this number follows conjecture
            if peUtilities.isSquare(remainder):
                break
    
def yieldOddComposite():
    counter = 3
    while True:
        if not peUtilities.isPrime(counter):
            yield counter
        counter += 2