import platform
import threading

def test():
    for x in range(100):
        p = platform._syscmd_uname('-p')

threads = [threading.Thread(target=test) for n in range(100)]
for thread in threads:
    thread.start()
for thread in threads:
    thread.join()