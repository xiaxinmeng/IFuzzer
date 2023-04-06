def f(x):
    if x:
        A+=4,
    else:
        A=[3]
    print("f",x,A)
def g(x):
    if not x:
        A=[3]
    else:
        A+=4,
    print("g",x,A)