# -*- coding: utf-8 -*-
"""
Created on Thu Nov  7 20:19:12 2019

@author: TrevorMorrisey
"""

import peUtilities

def consecutivePrimeSum(cap):
    primes = []
    for i in peUtilities.yieldPrime():
        if i < cap:
            primes.append(i)
        else:
            break

    sumsDict = {}
    for i in range(len(primes)):
        total = 0
        count = 0
        for j in range(i, len(primes)):
            total += primes[j]
            count += 1
            if total > cap:
                break
            elif peUtilities.isPrime(total):
                if total not in sumsDict:
                    sumsDict[total] = count

    streaks = []
    for num in sumsDict.values():
        streaks.append(num)
    streaks.sort()
    highestStreak = streaks[len(streaks) - 1]
    
    for key in sumsDict.keys():
        if sumsDict[key] == highestStreak:
            return key