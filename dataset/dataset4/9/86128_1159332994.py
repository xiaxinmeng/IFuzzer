import atexit
import concurrent.futures
import time


stop_signal = False

def waiter():
    while not stop_signal:
        time.sleep(1)
        print('.', end="")
        import sys; sys.stdout.flush()


def stop_workers():
    global stop_signal
    print("called!")
    stop_signal = True


atexit.register(stop_workers)


if __name__ == "__main__":
    executor = concurrent.futures.ThreadPoolExecutor(max_workers=1)
    executor.submit(waiter)
    assert False