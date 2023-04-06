import sys
import tracemalloc

def foo():
    open('foo', 'wb')

def hook(unraisable):
    orig_unraisablehook(unraisable)
    if unraisable.object is not None:
        tb = tracemalloc.get_object_traceback(unraisable.object)
        if tb:
            print("Object allocated at:")
            for line in tb:
                print(line)


orig_unraisablehook = sys.unraisablehook
sys.unraisablehook = hook
tracemalloc.start(5)

foo()