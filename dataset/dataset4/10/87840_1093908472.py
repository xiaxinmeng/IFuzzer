def recurse(n):
    print(n)
    try:
        recurse(n+1)
    except RecursionError:
        print("recursion error")
    print(n)