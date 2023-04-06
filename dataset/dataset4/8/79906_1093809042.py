gen = f()
for x in gen:
    print(x, "outer loop")
    for y in gen:
        print(y, "inner loop")