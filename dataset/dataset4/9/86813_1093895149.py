
import atexit
import concurrent.futures

def spawn():
    with concurrent.futures.ThreadPoolExecutor() as t:
        pass

atexit.register(spawn)
