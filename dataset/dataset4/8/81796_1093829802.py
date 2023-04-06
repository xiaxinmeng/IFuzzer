
with open(filename) as f:
    o = json.load(f)
...
with open(filename, 'w') as f:
    json.dump(o, f)
