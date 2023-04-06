import sys
import traceback

excs = []
for _ in range(2):
    try:
        1/0
    except:
        excs.append(traceback.TracebackException(*sys.exc_info()))