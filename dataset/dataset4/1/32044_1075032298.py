import sys
import inspect

def demo():
    for i in range(1):
        if i >= 0:
            pass


class Tracer:
    def __init__(self):
        self.events = []

    def trace(self, frame, event, arg):
        inspect.getframeinfo(frame)
        frame.f_trace_lines = True
        frame.f_trace_opcodes = True
        return self.trace

def main():
    t = Tracer()
    old_trace = sys.gettrace()
    try:
        sys.settrace(t.trace)
        demo()
    finally:
        sys.settrace(old_trace)


if __name__ == "__main__":
    sys.exit(main())