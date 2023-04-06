import shelve
import material
data = shelve.open("test3", flag="c",writeback=True)

def test_shelve(data):
    for k,v in data.items():
        pass

print("start")
test_shelve(data)