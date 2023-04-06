
from concurrent.futures import ProcessPoolExecutor

e = ProcessPoolExecutor()
e.submit(id)
e.shutdown(wait=False)
