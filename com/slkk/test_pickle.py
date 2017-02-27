import pickle

d = dict(name='bob', age=20, score=88)
with open('dump.text', 'wb') as f:
    pickle.dump(d, f)

with open('dump.text', 'rb') as f:
    d = pickle.load(f)
    print(d)
