dd = {'a': 1, 'b': 2, '3': 3}
if 'a' in dd:
    print(dd['a'])
    print(dd.get('4'))

dd.pop('a')
print(dd.get('a'))
a = set(['a', 'b', 'c', 'd'])
a.add('bbbb')
a.remove('a')
print (a)

