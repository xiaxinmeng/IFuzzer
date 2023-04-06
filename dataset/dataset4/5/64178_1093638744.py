def f(n):
    class A:
        n = n     # doesn't work, tries to look up 'n' as a global