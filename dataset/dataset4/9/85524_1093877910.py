def testReadWithWritingMode(self):
    r, w = os.pipe()
    w = os.fdopen(w, "w")
    w.write("hello")
    w.close()
    with io.FileIO(r, mode="w") as f:
        with self.assertRaises(_io.UnsupportedOperation):
            f.read()

def testReadallWithWritingMode(self):
    r, w = os.pipe()
    w = os.fdopen(w, "w")
    w.write("hello")
    w.close()
    with io.FileIO(r, mode="w") as f:
        with self.assertRaises(_io.UnsupportedOperation):
            f.readall()