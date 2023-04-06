a = []
for i in range(22):
    a = [a, a]

b = plistlib.dumps(a, fmt=plistlib.FMT_BINARY)