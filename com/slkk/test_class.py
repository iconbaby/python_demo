#!/usr/bin/env python2
# -*-coding:utf-8-*-


class Student(object):
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def print(self):
        print('%s:%s' % (self.name, self.age))


a = Student('hee', 32)
a.print()
