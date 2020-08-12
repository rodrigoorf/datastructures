# -*- coding: utf-8 -*-
"""
Created on Thu Sep 21 22:02:40 2017

@author: marcos.o
"""

#file = open ("texto.txt" "r")
#print file.read()


def countLetters(word):
    letterdict = {}
    for letter in word:
        letterdict[letter] = 0
    for letter in word:
        letterdict[letter] += 1
    """auxdic={}
    auxdic = letterdict
    letterdict = sorted(letterdict.items(), key=lambda x,y: cmp(x[1],y[1]))
    #letterdict = sorted(letterdict.values())
    resultdic = {}
    for i in letterdict:
        for item in auxdic:
            if item[i] == i:
                resultdic[item] = i
    print (resultdic)
    return resultdic"""
    print (letterdict)
    return letterdict