
import os

class MyPath(str):
    def __fspath__(self):
        print("Returns a pure string")
        return str(self)

os.fspath(MyPath())  # Prints nothing
