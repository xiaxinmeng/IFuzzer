items = (m.groups() for m in re.finditer(r'(\w+):(\w+)', text))
for key,value in items:
    data[key] = value