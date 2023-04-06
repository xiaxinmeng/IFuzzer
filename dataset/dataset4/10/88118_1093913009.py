
from multiprocessing import connection
import threading
key=b"1"

def run():
    c=connection.Client("/tmp/xxx", authkey=key)
    c.send("data")

l=connection.Listener("/tmp/xxx", authkey=key)
threading.Thread(target=run).start()
c=l.accept()
print("receive", c.recv())
