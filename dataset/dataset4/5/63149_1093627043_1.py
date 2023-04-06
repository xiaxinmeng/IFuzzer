for line in source.split("\n"):
    line = line.strip()
    if line and line[0] != '#':
        break               # Leave it alone
else:
    if symbol != "eval":
        source = "pass"   