import multiprocessing
from multiprocessing import managers
import pickle

class MyManager(managers.SyncManager):
    pass

def client():
    mgr = MyManager(address=("localhost",2288),authkey="12345")
    mgr.connect()
    l = mgr.list()
    multiprocessing.current_process().authkey = "12345"    # <--- HERE
    l = pickle.loads(pickle.dumps(l))

def server():
    mgr = MyManager(address=("",2288),authkey="12345")
    mgr.get_server().serve_forever()

server = multiprocessing.Process(target=server)
client = multiprocessing.Process(target=client)
server.start()
client.start()
client.join()
server.terminate()
server.join()