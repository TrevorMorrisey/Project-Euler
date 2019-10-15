# -*- coding: utf-8 -*-
"""
Created on Mon Oct 14 23:09:53 2019

@author: TrevorMorrisey
"""

def numberLetterCounts(upperBound):
    total = 0
    counter = 1
    while counter <= upperBound:
        total += getNumberLetterCount(counter)
        #print(numberToString(counter))
        counter += 1
    return total

def getNumberLetterCount(number):
    numString = numberToString(number)
    numString = ''.join(numString.split())
    return len(numString)

def numberToString(number):
    numString = ''
    if (number >= 100):
        hundredsPlace = number // 100
        if (hundredsPlace == 9):
            numString = numString + 'Nine hundred'
        elif (hundredsPlace == 8):
            numString = numString + 'Eight hundred'
        elif (hundredsPlace == 7):
            numString = numString + 'Seven hundred'
        elif (hundredsPlace == 6):
            numString = numString + 'Six hundred'
        elif (hundredsPlace == 5):
            numString = numString + 'Five hundred'
        elif (hundredsPlace == 4):
            numString = numString + 'Four hundred'
        elif (hundredsPlace == 3):
            numString = numString + 'Three hundred'
        elif (hundredsPlace == 2):
            numString = numString + 'Two hundred'
        else:
            numString = numString + 'One hundred'
        number = number - (hundredsPlace * 100)
        if (number > 0):
            numString = numString + ' and '
    if (number >= 20):
        tensPlace = number // 10
        if (tensPlace == 9):
            numString = numString + 'ninety'
        elif (tensPlace == 8):
            numString = numString + 'eighty'
        elif (tensPlace == 7):
            numString = numString + 'seventy'
        elif (tensPlace == 6):
            numString = numString + 'sixty'
        elif (tensPlace == 5):
            numString = numString + 'fifty'
        elif (tensPlace == 4):
            numString = numString + 'forty'
        elif (tensPlace == 3):
            numString = numString + 'thirty'
        elif (tensPlace == 2):
            numString = numString + 'twenty'
        numString = numString + ' '
        number = number - (tensPlace * 10)
    if (number >= 10):
        if (number == 19):
            numString = numString + 'nineteen'
        elif (number == 18):
            numString = numString + 'eighteen'
        elif (number == 17):
            numString = numString + 'seventeen'
        elif (number == 16):
            numString = numString + 'sixteen'
        elif (number == 15):
            numString = numString + 'fifteen'
        elif (number == 14):
            numString = numString + 'fourteen'
        elif (number == 13):
            numString = numString + 'thirteen'
        elif (number == 12):
            numString = numString + 'twelve'
        elif (number == 11):
            numString = numString + 'eleven'
        else:
            numString = numString + 'ten'
    else:
        if (number == 9):
            numString = numString + 'nine'
        elif (number == 8):
            numString = numString + 'eight'
        elif (number == 7):
            numString = numString + 'seven'
        elif (number == 6):
            numString = numString + 'six'
        elif (number == 5):
            numString = numString + 'five'
        elif (number == 4):
            numString = numString + 'four'
        elif (number == 3):
            numString = numString + 'three'
        elif (number == 2):
            numString = numString + 'two'
        elif (number == 1):
            numString = numString + 'one'
    return numString