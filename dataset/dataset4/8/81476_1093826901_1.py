def factorial_odd_part(n):
    f = math.factorial(n)
    return f // (f & -f)

F = [factorial_odd_part(n) % 2**64 for n in range(Nmax+1)]
Finv = [pow(f, -1, 2**64) for f in F]
PC = [n.bit_count() for n in range(Nmax+1)]