import os, tempfile
a, b = tempfile.mkstemp()
f = os.fdopen(a, "wb")
f = os.fdopen(a, "wb")
f.write("beer")
f.close()