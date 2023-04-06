import gc
class MyBuf(bytes): pass

def f():
    buf = MyBuf(b'abc')
    m = memoryview(buf)
    buf.m = m
    gc.collect();gc.collect();gc.collect()