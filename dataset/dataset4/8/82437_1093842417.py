import binascii, zlib
bigdata=memoryview(bytearray((1<<32) + 100))

print(binascii.crc32(bigdata))
crc = binascii.crc32(bigdata[:1000])
crc = binascii.crc32(bigdata[1000:], crc)
print(crc)

print(zlib.crc32(bigdata))
crc = zlib.crc32(bigdata[:1000])
crc = zlib.crc32(bigdata[1000:], crc)
print(crc)