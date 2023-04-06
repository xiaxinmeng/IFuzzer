from multiprocessing import Pool, Process

def t2():
	# We expect the pool to handle this
	print('t2: Hello!')

pool = Pool()
def t1():
	# We assign a task to the pool
	pool.apply_async(t2)
	print('t1: Hello!')

if __name__ == '__main__':
	# Process() forks the main process containing the pool
	Process(target=t1).start()