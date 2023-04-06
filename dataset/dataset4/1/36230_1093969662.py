from os import getcwd, chdir, system, popen3

from threading import Thread

class NonBlockingReader(Thread):

    def __init__(self,file):
        Thread.__init__(self)
        self.file = file
        
    def run(self):
        self.result = self.file.read()

    def read(self):
        return self.result
    
dir=getcwd()
chdir('E:\ZopeTests\sandbox\Zope3')
(i,c,e) = popen3('c:\python22\python test.py')
chdir(dir)