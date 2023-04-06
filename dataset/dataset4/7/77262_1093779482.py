import multiprocessing
import os
import threading

os.system('lsof -p {} | grep -v txt'.format(os.getpid()))
q = multiprocessing.Queue()
q.put(1)
q.get()
threading.enumerate()
os.system('lsof -p {} | grep -v txt'.format(os.getpid()))
q.close()
threading.enumerate()
os.system('lsof -p {} | grep -v txt'.format(os.getpid()))