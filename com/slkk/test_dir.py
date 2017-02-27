import os

print(os.name)
print(os.environ)
a = os.path.abspath('.')
b = os.path.join(a, 'tssst')
os.rmdir(b)
os.mkdir(b)
