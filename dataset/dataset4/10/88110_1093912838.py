from multiprocessing import Process
from concurrent.futures import ThreadPoolExecutor


def some_task():
    pass


def execute_error():
    p = Process(target=some_task)
    p.start()
    p.join()
    print(p.exitcode)  # This is always 1 on a ThreadPoolExecutor!!!


executor = ThreadPoolExecutor(max_workers=4)
executor.submit(execute_error)
# execute_error()  # IMPORTANT: this works correctly (exit 0)