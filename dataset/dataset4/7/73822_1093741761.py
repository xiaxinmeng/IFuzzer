import json
obj = [1, 2]

print('--indent=4')
print(json.dumps(obj, indent=4))

print('--no-indent')
print(json.dumps(obj, indent=None))

print('--compact')
print(json.dumps(obj, separators=(',', ':')))