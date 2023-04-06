n=1
def f(n=2):
    class A: n=n
    return A
print(f().n)