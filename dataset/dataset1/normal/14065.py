from xml.etree.ElementTree import Element
import gc

deleted = False
class ShowGC:
    def __del__(self):
        global deleted
        deleted = True

L = [ShowGC()]
L.append(Element("foo", bar=L))
del L
gc.collect()

assert deleted

