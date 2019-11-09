# -*- coding: utf-8 -*-
"""
Created on Thu Nov  7 20:19:12 2019

@author: TrevorMorrisey
"""

import peUtilities

#def consecutivePrimeSum(cap):
#    primes = []
#    primeSums = []
#    total = 0
#    index = 0
#    for i in peUtilities.yieldPrime():
#        if (i < cap):
#            primes.append(i)
#        total += i
#        if total < cap:
#            primeSums.append(total)
#        else:
#            if (i < cap):
#                while total >= cap:
#                    if (index < len(primes)):
#                        #print("Reducing total by: " + str(primes[index]))
#                        total -= primes[index]
#                        index += 1
#                    else:
#                        break
#                primeSums.append(total)
#            else:
#                break
#    
#    primeSums.sort()
#    primeSums.reverse()
#    for number in primeSums:
#        print("Checking: " + str(number))
#        if peUtilities.isPrime(number):
#            return number

#def consecutivePrimeSum(cap):
#    primesBelowCap = []
#    for i in peUtilities.yieldPrime():
#        if i < cap:
#            primesBelowCap.append(i)
#        else:
#            break
#    #return primesBelowCap
#    primeSums = []
#    for i in range(len(primesBelowCap)):
#        currentSum = 0
#        for j in range(i, len(primesBelowCap)):
#            currentSum += primesBelowCap[j]
#            if currentSum < cap:
#                primeSums.append(currentSum)
#            else:
#                break
#            #currentSum += primesBelowCap[j]
#    primeSums.sort()
#    return primeSums

#def consecutivePrimeSum(cap):
#    total = 0
#    primes = []
#    sums = []
#    for i in peUtilities.yieldPrime():
#        primes.append(i)
#        if total + i < cap:
#            total += i
#            sums.append(total)
#        else:
#            break
#            #return total
#    #return sums
#    return primes

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