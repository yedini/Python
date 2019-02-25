# -*- coding: utf-8 -*-
"""
Created on Mon Feb 25 17:20:21 2019
adder: 두 정수 사이의 합 구하기

@author: dcng
"""

def adder(a,b):
    if a>b:
        a,b=b,a
    return sum(range(a,b+1))


print(adder(2,7))
print(adder(4,4))
print(adder(6,3))
