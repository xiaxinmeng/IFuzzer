d = [0]
for n in d:
    print(n, len(d))
    if n < 5:
        d.extend((n+1, n+2))