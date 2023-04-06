class Bdb:

    def trace_dispatch(self, frame, event, arg):
        self.set_continue()
        if sys.gettrace():
            return self.trace_dispatch

    def set_trace(self, frame):
        self.botframe = frame
        frame.f_trace = self.trace_dispatch
        sys.settrace(self.trace_dispatch)

    def set_continue(self):
        sys.settrace(None)
        del self.botframe.f_trace

frame = sys._getframe()
d = Bdb()
d.set_trace(frame)

y = "line of code not triggering an error"
x = 1
assert x != 1