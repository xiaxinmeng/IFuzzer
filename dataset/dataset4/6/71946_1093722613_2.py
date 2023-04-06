import selectors
import tempfile
import traceback

sel = selectors.KqueueSelector()

f = tempfile.TemporaryFile()
filedescriptor = f.fileno()
f.close()