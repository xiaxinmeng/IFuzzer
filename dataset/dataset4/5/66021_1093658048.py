import threading
import time


def f():
    while True:
        print("processing")
        time.sleep(1)


if __name__ == "__main__":
    try:
        thread = threading.Thread(target=f)
        thread.start()
        thread.join()
    except KeyboardInterrupt:
        print("interrupted")