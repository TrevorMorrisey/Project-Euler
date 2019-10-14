# -*- coding: utf-8 -*-
"""
Created on Sat Oct 12 21:27:46 2019

@author: TrevorMorrisey
"""

def isPalindrome(string):
    if len(string) == 1 or len(string) == 0:
        return True
    elif len(string) == 2:
        return string[0] == string[1]
    else:
        if string[0] != string[len(string) - 1]:
            return False
        else:
            return isPalindrome(string[1:len(string) - 1])
    
def largestPalindromeProduct(maxFactor):
    highestSum = 0
    for i in range(maxFactor + 1):
        for j in range(maxFactor + 1):
            currentSum = i * j
            if isPalindrome(str(currentSum)):
                if currentSum > highestSum:
                    #print('New highest sum:' + str(currentSum))
                    highestSum = currentSum
    return highestSum
        