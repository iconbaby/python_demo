#!/usr/bin/env python3
#-*-coding:utf-8-*-
def sum(x):
    def subsum():
        sum =0
        for a in x:
            sum +=a
        return sum
    return subsum;

a = sum([1,2,4])

print(a.__name__)


