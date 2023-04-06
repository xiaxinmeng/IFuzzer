__ltrace__ = 1

def gen():
    yield 10
    yield 20

def main():
    for x in gen():
        x = x * x
        print(x)

main()