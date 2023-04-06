import multiprocessing

def f(m):
	print(m)

p = multiprocessing.Process(target=f, args=('pouet',))
p.start()
# 