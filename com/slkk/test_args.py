#!/usr/bin/env python3
# --*--coding:utf-8--*--
def power(x, n=2):
    a = 0;
    sum = 1
    if n > 0:
        while a < n:
            sum = sum * x
            a += 1
    return sum


print(power(4, 2))
print(power(5))


def calc(*num):
    sum = 0;
    for x in num:
        sum += x * x;
    return sum;
print(calc(1,2,3))
a=list([1,2,2,2])
print(calc(*a))

def args(name,age,**args):
    return "你的名字是：%s,年龄是%s,其他是%s"%(name,age,args)
print(args('shenli',23,habbit="adf"))
