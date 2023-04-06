import array
import tempfile

testarray = array.array('B')
testarray.fromstring("\x00\x00\x00")
f = tempfile.TemporaryFile()
testarray.tofile(f)