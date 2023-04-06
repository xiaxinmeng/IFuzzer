class WarnOnDel(object):
    def __del__(self):
        warnings.warn("oh no something went wrong", UserWarning)

def do_work():
    while True:
        w = WarnOnDel()

for i in range(10):
    t = threading.Thread(target=do_work)
    t.setDaemon(1)
    t.start()