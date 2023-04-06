def upto(first, last):
        x=first
        while x<=last:
                yield x
                x=x+1

x=upto(1, 10)