import concurrent.futures
import time

with concurrent.futures.ThreadPoolExecutor() as ex:
	futures = [
		ex.submit(time.sleep, 30),
		ex.submit(print, 'test'),
	]
	for future in concurrent.futures.as_completed(futures, timeout=1):
		_ = future.result()