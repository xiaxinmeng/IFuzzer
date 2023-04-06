class StderrHandler(logging.StreamHandler):
    def __init__(self):
        super().__init__()

    def get_stream(self):
        return sys.stderr

    def set_stream(self, _value):
        pass

    stream = property(get_stream, set_stream)