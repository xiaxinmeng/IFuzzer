from multiprocessing import Queue, Process

def getLongString():
	s = ""
	for i in range(1, 65524):
		s += "1"
	return s

def p1(q):
	print('START')
	q.put(getLongString())
	print('END')

q = Queue()

prs1 = Process(target=p1, args=(q,))
prs1.start()
prs1.join()

print('FINISH')