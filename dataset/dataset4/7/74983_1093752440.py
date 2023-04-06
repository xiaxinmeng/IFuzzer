import os
import psutil
import zlib

def test():
	result = []
	for i in range(10000):
		try:
			result.append(zlib.compressobj())
		except:
			print('%d compressobj created!'%(i))
			pid = os.getpid()
			p = psutil.Process(pid)
			print('memory info:', p.memory_info())
			break


if __name__ == '__main__':
	test()