import io
import weakref

fn = "file.txt"
w = io.FileIO(fn, "w")
r = io.FileIO(fn, "r")
brw = io.BufferedRWPair(r,w)
ref = weakref.ref(brw)
del brw
del ref
