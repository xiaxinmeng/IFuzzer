import json
d1 = {1: "fromstring", "1": "fromnumber"}
string = json.dumps(d1)
print(string)
d2 = json.loads(string)
print(d2)