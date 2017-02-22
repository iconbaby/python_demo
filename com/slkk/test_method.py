# -*-coding:utf-8-*-

n1 = 255
n2 = 1000
print(1 + 0x12)


# def my_method(x):
#     return x * x
#
# print(my_method(3))

def my_abs(x):
    if not isinstance(x, (int, float)):
        raise TypeError('bad operand type')
    if x >= 0:
        return x
    else:
        return -x
