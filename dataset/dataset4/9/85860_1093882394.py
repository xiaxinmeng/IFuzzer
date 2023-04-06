import concurrent.futures
import time

with concurrent.futures.ThreadPoolExecutor() as ex:
	print(time.time())
	futures = [
		ex.submit(time.sleep, 30),
		ex.submit(time.sleep, 30),
		ex.submit(print, 'test'),
	]
	try:
		for future in concurrent.futures.as_completed(
			futures, timeout=1):
			_ = future.result()
	except Exception as e:
		print(time.time())
		raise e