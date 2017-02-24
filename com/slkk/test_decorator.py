#!/usr/bin/env python3
#-*-coding:utf-8-*-

import os

def log(func):
    def wrap(*args,**argss):
        print('heew')
        return func(*args,**argss)
    return wrap
@log
def now():
    print('2012-02-23')
now()

print(os.listdir('.'))
