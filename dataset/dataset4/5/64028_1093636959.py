import io
import os

class MyFile(io.FileIO):
    def close(self):
        os.close(self.fileno())

f = MyFile('/etc/issue')
f = None