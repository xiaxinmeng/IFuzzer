import sys
import multiprocessing.queues
del sys.modules['multiprocessing']
import multiprocessing
import multiprocessing.connection
from multiprocessing.connection import wait
connection = multiprocessing.connection   # AttributeError here