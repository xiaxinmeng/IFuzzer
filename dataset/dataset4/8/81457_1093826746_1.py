import time, concurrent.futures

def call():
    while True:
        time.sleep(1)


if __name__ == "__main__":
    with concurrent.futures.ProcessPoolExecutor(max_workers=2) as executor:
        futures = [executor.submit(call) for _ in range(8)]
        time.sleep(2)

        for future in futures:
            print(future.running())