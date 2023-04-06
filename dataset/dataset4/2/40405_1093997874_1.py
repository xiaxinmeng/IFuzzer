import sys

class NullStream:
    """
    A file like class that writes nothing
    """
    def close(self): pass
    def flush(self): pass
    def write(self, str): pass
    def writelines(self, sequence): pass

if not isrealfile(sys.__stdout__): 
   sys.stdout = NullStream()

if not isrealfile(sys.__stderr__):
   sys.stderr = NullStream()