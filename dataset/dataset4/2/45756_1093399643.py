class NullWriter:
    def write(self, data):
        pass

if sys.stdout is None:
    sys.stdout = NullWriter()