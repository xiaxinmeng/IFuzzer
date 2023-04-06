import io

class F(object):
    def readable(self): return True
    def writable(self): return True
    def seekable(self): return True


try:
    t = io.TextIOWrapper(F(), encoding='utf-8')
except: pass

try:
    t = io.TextIOWrapper(F(), encoding='utf-8')
except: pass

print("1")
F.tell = lambda x: 0
print("2")
t = io.TextIOWrapper(F(), encoding='utf-8')
print("3")
