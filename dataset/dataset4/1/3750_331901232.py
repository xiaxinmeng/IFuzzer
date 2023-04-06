
class BadStructRusage(tuple):
    n_fields = -1
    n_sequence_fields = 16
    n_unnamed_fields = 0

import os
import time
import resource
new_pid = os.fork()
if new_pid == 0:
    time.sleep(0.5)
else:
    resource.struct_rusage = BadStructRusage
    os.wait3(0)
