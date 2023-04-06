import gc

class A:
    def __del__(self):
        print("__del__")

def f():
    a = A()
    def g():
        a
        g()

def main():
    for _ in range(3):
        f()
#       gc.collect()
        print("out of function")

if __name__ == '__main__':
    main()