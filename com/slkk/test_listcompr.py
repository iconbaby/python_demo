import os

print([x for x in os.listdir('.')])
print('afaf' + 'adfa')
a = {'a': 1, 'b': 2, 'c': 3}
for k, v in a.items():
    print(k, '=', v)

L = ['HELLO', 'WOKRD']
print([s.lower() for s in L])
l = ['Hello', 'World', 18, 'Apple', None]
print([s.lower() if isinstance(s, str) else s for s in l])
