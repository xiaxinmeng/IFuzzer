import concurrent.futures
import time

with concurrent.futures.ThreadPoolExecutor() as executor:
    list(executor.map(time.sleep, [29, 30], timeout=3000))