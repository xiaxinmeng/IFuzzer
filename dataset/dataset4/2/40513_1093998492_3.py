# specify buffer and ushort
buf = array.array('c', [' ' for x in range(0, 1023)])
dummy_func("text", buffer=buf, ushort=10)