#!/usr/bin/env python
# -*-conding:utf-8-*-
try:
    f = open('test_dict.py', 'r')
    a = f.read()
    print(a)
finally:
    if f:
        f.close()
