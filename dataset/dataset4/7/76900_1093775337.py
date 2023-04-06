import threading

def func():
	while True:
		print(1,2,3,4,5,6,7,8,9,10) 

t1 = threading.Thread(target=func)
t2 = threading.Thread(target=func)
t1.start()
t2.start()