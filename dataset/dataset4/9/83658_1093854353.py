import multiprocessing

def f(x):
	return x

if __name__ == '__main__':
	with multiprocessing.Pool(2, maxtasksperchild=0) as pool:
		pool.map(f, range(3))