#!/usr/bin/env python3
# -*-coding:utf-8-*-
from functools import reduce


def f(x):
    return x * x


a = list(range(10))

# print(list(map(f,a)))
for x in map(f, a):
    print(x)


def add(x, y):
    return x + y


print(reduce(add, [1, 2, 3, 4, 5, 6]))


def name(s):
    if isinstance(s, str):
        return s[:1].upper() + s[1:].lower()


print(list(map(name, ['hello', 'woRld', 'JAK'])))


def fun(x, y):
    return x * y


def prod(n):
    if isinstance(n, list):
        return reduce(fun, n)


print(prod([1, 2, 3, 4]))


def str2num(x):
    return {'1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9, '0': 0, '.': None}[x]


def str2float(x, y):
    if isinstance(x, int) & isinstance(y, int):

        return x * 10 + y
    else:
        return '.'


print(reduce(str2float, list(map(str2num, '102.34'))))
