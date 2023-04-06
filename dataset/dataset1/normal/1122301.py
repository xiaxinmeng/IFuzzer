import marshal

data = marshal.dumps((1, 2, 3, "hello", 4, 5, 6))

for i in range(len(data), -1, -1):
    try:
        print(marshal.loads(data[:i]))
    except EOFError:
        print("EOFError")
    except ValueError:
        print("ValueError")


