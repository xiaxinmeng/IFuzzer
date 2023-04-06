import sys
def tracing_func(frame, event, arg):
    print(frame.f_code.co_filename, frame.f_code.co_name)
    return tracing_func
sys.settrace(tracing_func)


def call_1():
    pass

call_1()

print('here')
sys.settrace(None)

#After executing everything, the interpreter will not exit.
