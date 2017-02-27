import json


class Student(object):
    def __init__(self, name, score):
        self._name = name
        self._score = score


def student2dict(std):
    return {
        'name': std._name,
        'score': std._score
    }


student = Student('bob', 23)
print(json.dumps(student, default=student2dict))
