
import multiprocessing as mp


class A(object):
    def process(self):
        print("method of A")


class B(A):
    def foo(self):
        mp.Process(target=super().process).run()  # "method of A" is printed
        mp.Process(target=super().process).start()  # "method of B" is printed

    def process(self):
        print("method of B")


if __name__ == "__main__":
    b = B()
    b.foo()
