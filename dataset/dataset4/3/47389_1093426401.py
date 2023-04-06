import sys, io, threading
stdout2 = io.open(sys.stdout.fileno(), mode="w")
def f(i):
    for i in range(10):
        stdout2.write(unicode((x, i)) + '\n')
for x in range(10):
    t = threading.Thread(target=f, args=(x,))
    t.start()