def foo():
    try:
        yield
    except:
        print("ERROR")

for x in foo():
    print(1)