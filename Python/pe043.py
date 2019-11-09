# -*- coding: utf-8 -*-
"""
Created on Sat Nov  9 17:03:27 2019

@author: TrevorMorrisey
"""

def substringDivisibility():
    permutations = []
#    for i in range(1000000000, 10000000000):
#        if peUtilities.isPermutation(i, 1023456789):
#            permutations.append(i)
    
    realOptions1 = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    options1 = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    for digit1 in realOptions1:
        options2 = options1.copy()
        options2.remove(digit1)
        for digit2 in options2:
            options3 = options2.copy()
            options3.remove(digit2)
            for digit3 in options3:
                options4 = options3.copy()
                options4.remove(digit3)
                for digit4 in options4:
                    options5 = options4.copy()
                    options5.remove(digit4)
                    for digit5 in options5:
                        options6 = options5.copy()
                        options6.remove(digit5)
                        for digit6 in options6:
                            options7 = options6.copy()
                            options7.remove(digit6)
                            for digit7 in options7:
                                options8 = options7.copy()
                                options8.remove(digit7)
                                for digit8 in options8:
                                    options9 = options8.copy()
                                    options9.remove(digit8)
                                    for digit9 in options9:
                                        options10 = options9.copy()
                                        options10.remove(digit9)
                                        for digit10 in options10:
                                            number = digit10 + digit9 * 10 + digit8 * 100 + digit7 * 1000 + digit6 * 10000 + digit5 * 100000 + digit4 * 1000000 + digit3 * 10000000 + digit2 * 100000000 + digit1 * 1000000000
                                            #permutations.append(number)
                                            if (testSubstrings(number)):
                                                permutations.append(number)
                    
                    
    return permutations

def testSubstrings(number):
    string = str(number)
    substring1 = string[1:4]
    substring2 = string[2:5]
    substring3 = string[3:6]
    substring4 = string[4:7]
    substring5 = string[5:8]
    substring6 = string[6:9]
    substring7 = string[7:10]
    
    substring1 = int(substring1)
    substring2 = int(substring2)
    substring3 = int(substring3)
    substring4 = int(substring4)
    substring5 = int(substring5)
    substring6 = int(substring6)
    substring7 = int(substring7)
    
    if substring1 % 2 != 0:
        return False
    
    if substring2 % 3 != 0:
        return False
    
    if substring3 % 5 != 0:
        return False
    
    if substring4 % 7 != 0:
        return False
    
    if substring5 % 11 != 0:
        return False
    
    if substring6 % 13 != 0:
        return False
    
    if substring7 % 17 != 0:
        return False
    
    return True