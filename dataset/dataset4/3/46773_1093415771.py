import io, gc
def f():
   class C: pass
   c=C()
   assert isinstance(c, io.StringIO) is False
   gc.collect();gc.collect();gc.collect()