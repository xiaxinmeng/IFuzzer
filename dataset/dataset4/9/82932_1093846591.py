import json

foo = {}

for i in range(1000):
    json.dumps(foo)
    print(i)
    foo = {'bar': foo}