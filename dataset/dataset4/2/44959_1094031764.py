r = '''
a(b(c[d]))
'''
from threading import Thread
from compiler import parse
Thread(target = parse, args = (r,)).start()