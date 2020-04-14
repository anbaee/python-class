# -*- coding: utf-8 -*-
"""
Created on Tue Apr 14 00:56:27 2020

@author: Novin
"""

thistuple = ("apple", "banana", "cherry")




print(thistuple)
print(thistuple[1])
print(thistuple[-1])
print(thistuple[1:3])
print('cherry' in thistuple)

# tuple items ara not changeable , following line return error
thistuple[-1] = 3