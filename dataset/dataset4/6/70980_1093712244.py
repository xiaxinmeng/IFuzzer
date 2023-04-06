import os, threading, time

t = threading.Thread(target=time.sleep, args=(3.0,))
t.start()

print("First process", threading.enumerate())

pid = os.fork()
if pid != 0:
    os.waitpid(pid, 0)
else:
    print("Child process", threading.enumerate())