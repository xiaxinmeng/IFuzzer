import threading
import subprocess

def B():
    while True:
        break
    cmd="ps -ef | grep 'shell' | awk '{print $2}' | xargs kill -9"
    subprocess.call(cmd, shell=True)


def A():
    th = threading.Thread(target=B)
    th.start()