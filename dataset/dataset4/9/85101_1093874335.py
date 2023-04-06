from concurrent.futures.process import ProcessPoolExecutor
from concurrent.futures import as_completed
class Hello:
    _instance = None
    def __init__(self):
        print("Creating instance of Hello ", self)
        Hello._instance = self
def worker():
    return Hello._instance
def main():
    hello = Hello()
    with ProcessPoolExecutor(max_workers=2) as pool:
        futures = []
        for _ in range(4):
            futures.append(pool.submit(worker))

        for future in as_completed(futures):
            print(future.result())
if __name__ == "__main__":
    main()