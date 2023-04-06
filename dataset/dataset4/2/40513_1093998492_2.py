# specify buffer
buf = array.array('c', [' ' for x in range(0, 1023)])
dummy_func("text", buffer=buf)