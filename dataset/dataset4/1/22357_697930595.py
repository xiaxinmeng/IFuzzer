
import threading

class Name:
    def __nonzero__(self):
        return True
    def __str__(self):
        return ''

name = threading.Thread(name=Name()).name
print(repr(name))
