# -*- coding: utf-8 -*-
"""
Created on Fri Oct  5 12:31:28 2018
@author: hbui
"""

from nltk.corpus import wordnet as wn

def myDict(foo):
    syn = wn.synsets(foo)
    for i in range(len(syn)):
        temp = syn[i].definition()
        print('Definition '+str(i+1)+': '+str(temp))
    print('Examples: ',syn[0].examples())
    syno = []
    anto = []
    for i in wn.synsets(foo):
        for j in i.lemmas():
            syno.append(j.name())
            if j.antonyms():
                anto.append(j.antonyms()[0].name())
    str1='Synonyms: '
    for i in set(syno):
        str1=str1+i+'| '
    str2 ='Antonyms: '
    for i in set(anto):
        str2=str2+i+'| '
    print(str1 + '\n' + str2)

from sys import argv
foo = argv[1]
myDict(foo)