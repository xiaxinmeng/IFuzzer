
# 0x0D, 13 = /r
# 0x0A, 10 = /n

print('test "\\r\\n"')
print('-------------')
b = bytes([0x41, 0x0D, 0x0A])
print("bytes: %s" % b)
print("string: %s" % b.decode('utf8'), end='')
# expected string: "A\r\n"
# ressult string: "A\r\r\n"

print('test "\\n"')
print('----------')
b = bytes([0x41, 0x0A])
print("bytes: %s" % b)
print("string: %s" % b.decode('utf8'), end='')
# expected string: "A\n"
# ressult string: "A\r\n"
