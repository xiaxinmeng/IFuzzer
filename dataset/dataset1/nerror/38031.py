import _io
_io.FileIO("foobar", opener=lambda name, flags: 1000000)
