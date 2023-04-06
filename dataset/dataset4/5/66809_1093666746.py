import sys

def a():
    b()

def b():
    c()

def c():
    d()

def d():
    def e():
        print_stack(limit=2) # Last 2 entries
        ''' Output:
            File "file", line 331, in d                                                                                                                                                                                       
              e()                                                                                                                                                                                                                         
            File "file", line 328, in e
              print_stack(limit=2) # Last 2 entries '''
        raise Exception
    e()
    
try:
    a()
except Exception:
    print_exc(limit=2) # 2 entries from the caller
    ''' Output:
        Traceback (most recent call last):
          File "file", line 336, in <module>
            a()
          File "file", line 318, in a
            b()
        Exception '''