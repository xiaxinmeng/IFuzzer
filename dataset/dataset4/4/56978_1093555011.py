buffer=ctypes.create_string_buffer(4)
buffer.value='a\0bc'
print("buffer.value=%r" % buffer.value)
print("buffer.raw=%r" % buffer.raw)