for x in f():
    print(x, "outer loop")
    for y in f():
        print(y, "inner loop")