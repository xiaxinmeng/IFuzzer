import json

data = {"a": "original data"}
indent = '"b": "injected data",\n'
json_string = json.dumps(data, indent=indent)
print(json_string)