
import shelve
import material
data = shelve.open("test3", flag="c",writeback=True)

def test_shelve(data):
    for k,v in data.items():
        pass

print("start")
test_shelve(data)

#data.close() #fixes SIGSEGV at shutdown
#actually problem is in c pickle module; when Python pickle module is used it works

print("end")
#after this it is crash
