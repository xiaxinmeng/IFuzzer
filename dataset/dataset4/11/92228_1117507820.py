
import sys

def fun():
    a = 1  # <---- jump location

    try:
        b = 1 / 0
    except ZeroDivisionError as e:
        pass

    c = 3  # current location


def trace(frame, event, arg):
    if event == "line" and frame.f_lineno == 11:
        frame.f_lineno = 4

    return trace


sys.settrace(trace)

if __name__ == "__main__":
    fun()
