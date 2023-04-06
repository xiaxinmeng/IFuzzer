from concurrent.futures import ProcessPoolExecutor

class A:
    def f(self):
        print("called")

class B(A):
    def f(self):
        executor = ProcessPoolExecutor(max_workers=2)
        print(executor.submit(super().f).exception())

if __name__ == "__main__":
    B().f()