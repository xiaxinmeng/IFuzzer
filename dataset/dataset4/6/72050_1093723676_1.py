import _elementtree as et

class X(str):
    def __del__(self):
        print(elem.text)

b = et.TreeBuilder()
b.start("test")
b.data(["AAAA", X("BBBB")])
b.start("test2")

elem = b.close()
print(elem.text)