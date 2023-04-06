def ipow(y, n):
    x = 1.0
    while n > 0:
        if n % 2 == 1:
            x *= y
        n //= 2
        y *= y
    return x