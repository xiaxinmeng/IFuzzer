
from concurrent.futures import ProcessPoolExecutor
import time

t = ProcessPoolExecutor(max_workers=3)
t.map(time.sleep, [1,2,3])
t.shutdown(wait=False)
