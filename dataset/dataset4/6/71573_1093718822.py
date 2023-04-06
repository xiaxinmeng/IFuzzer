data = await stream.read_exactly(4)
(len,) = unpack(">I", data)
command = await stream.read_exactly(len)