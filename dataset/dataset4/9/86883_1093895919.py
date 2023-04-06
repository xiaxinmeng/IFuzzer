import sys,time, threading

class test:
    def test(self):
        pass


class test1:
    def run(self):
        for i in range(0,10000000):
            connection = test()
            sys.stderr.write(' =_= ')


def testrun():
    client = test1()
    thread = threading.Thread(target=client.run, args=())
    thread.setDaemon(True)
    thread.start()

    time.sleep(0.1)

testrun()