import sys
import inspect

def case1():
    class C:
        def __init__(self):
            pass
    c = C()

def case2():
    a = 1
    class C:
        def __init__(self):
            pass
    c = C()

def case3():
    def fn():
        pass
    class C:
        def __init__(self):
            pass
    c = C()

def trace(frame,event,arg):
    code = frame.f_code
    print('name:',code.co_name)
    print('source:\n',inspect.getsource(code),'\n')

for case in ('case1','case2','case3'):
    print('#####',case)
    call = getattr(sys.modules[__name__],case)
    sys.settrace(trace)
    try:
        call()
    finally:
        sys.settrace(None)