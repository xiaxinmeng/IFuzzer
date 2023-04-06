import concurrent.futures
import time

with concurrent.futures.ThreadPoolExecutor() as executor:
    future1 = executor.submit(time.sleep, 29)
    future2 = executor.submit(time.sleep, 30)
    list(concurrent.futures.as_completed([future1, future2], timeout=3000))