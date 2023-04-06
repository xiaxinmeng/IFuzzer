def length(x):
    try:
        return sum(length(i) for i in x)
    except Exception:
        return 1


a = [[1, 2, 3], [4, 5, 6]]
a.append(a)
length(a)