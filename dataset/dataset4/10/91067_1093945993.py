# encodings.py
import sys

class FullCoverageTracer:
    def __init__(self):
        self.traces = []

    def fullcoverage_trace(self, *args):
        frame, event, arg = args
        if frame.f_lineno is None:
            self.traces.append((frame.f_code.co_name, frame.f_code.co_filename))
        return self.fullcoverage_trace