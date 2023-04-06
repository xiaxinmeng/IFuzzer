import os
import time
import resource
new_pid = os.fork()
if new_pid == 0:
    time.sleep(0.5)
else:
    resource.struct_rusage = BadStructRusage
    os.wait3(0)