import time
import threading

def count_smth(seconds: int) -> int:
    time.sleep(seconds)
    return seconds * 3

def small_job(d: dict, key: str, seconds: int) -> None:
    d[key] += count_smth(seconds)  # <-- strange happens here

def main() -> None:
    d = dict(key=0)
    t1 = threading.Thread(target=small_job, args=(d, 'key', 1))
    t2 = threading.Thread(target=small_job, args=(d, 'key', 2))
    t1.start()
    t2.start()
    t1.join()
    t2.join()
    print(d['key'])  # expected: 0 + 1 * 3 + 2 * 3 = 9, actual: 6

main()