for n in iter(d.popleft, None, IndexError):
        print(n, len(d))
        if n < 5:
            d.extend((n+1, n+2))