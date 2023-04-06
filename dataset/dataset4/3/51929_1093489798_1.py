class MyThread (threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)
        
    def run(self):
        f = open('I am alive', 'w')
        f.write('hello, dude!\n')
        f.close()
        
t = MyThread()
t.start()