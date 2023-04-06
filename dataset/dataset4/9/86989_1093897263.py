import sys

def print_line():
    print(sys._getframe(1).f_lineno)

def test():
    print_line()
    sys._getframe(0).f_trace = True
    print_line()
    print_line()

test()