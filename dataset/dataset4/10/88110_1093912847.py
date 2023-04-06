from multiprocessing import Process
from concurrent.futures import ThreadPoolExecutor


def some_task():
    pass


def execute_error():
    p = Process(target=some_task)
    p.start()
    p.join()
    print(p.exitcode)  # This is always 1 on a ThreadPoolExecutor!!!


# THIS IS THE IMPORTANT CHANGE
with ThreadPoolExecutor(max_workers=4) as executor:
    executor.submit(execute_error)