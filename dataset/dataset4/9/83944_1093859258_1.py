import os
from concurrent.futures import ThreadPoolExecutor

def new_process(arg):
    pid = os.fork()
    if pid == 0:
        print("Child", os.getpid())
        ## os.execl("/usr/bin/true", "/usr/bin/true")
    else:
        print("Parent", pid)
        pid, status = os.waitpid(pid, 0)
        print("Done", pid, os.getpid())

executor = ThreadPoolExecutor(max_workers=4)
futures = [executor.submit(new_process, None)
           for i in range(0, 4)]
for fut in futures:
    fut.result()