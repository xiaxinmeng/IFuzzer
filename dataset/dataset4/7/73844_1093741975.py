import sys
import threading
import multiprocessing

mpl = multiprocessing.log_to_stderr()
mpl.setLevel(1)


class A(threading.Thread):
    def __init__(self):
        super(A, self).__init__()

    def run(self):
        print(self.name, 'RUN')

        for line in sys.stdin: #increases probability of hanging
            pass

        print(self.name, 'STOP')


class B(multiprocessing.Process):
    def __init__(self):
        super(B, self).__init__()

    def run(self):
        print(self.name, 'RUN')


a = A()
a.start()

b = B()
b.start()
print('B started', b, b.is_alive(), b.pid)
print('A', a)

a.join()
b.join()

print('FINISHED')