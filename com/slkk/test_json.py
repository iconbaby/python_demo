import json

d = dict(name='bob', age=20, score=34)
json.dumps(d)
print(d)
jsonstring = "{'age': 20, 'score': 34, 'name': 'bob'}"
json.loads(jsonstring)
