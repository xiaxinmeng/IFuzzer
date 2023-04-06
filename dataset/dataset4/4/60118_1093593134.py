import threading, os

def foo():
    print("Trying import")
    import sys
    print("Import successful")

pid = os.fork()
if pid == 0:
    try:
        t = threading.Thread(target=foo)
        t.start()
        t.join()
    finally:
        os._exit(0)

os.waitpid(pid, 0)
print("create.py complete")