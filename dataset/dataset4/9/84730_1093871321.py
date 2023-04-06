
import threading
import subprocess
import multiprocessing

proc = subprocess.Popen(["sh", "-c", "exit 0"])

q = multiprocessing.Queue()

def communicate_thread(proc):
    proc.communicate()

t = threading.Thread(target=communicate_thread, args=(proc,))
t.start()

proc.terminate()

t.join()
