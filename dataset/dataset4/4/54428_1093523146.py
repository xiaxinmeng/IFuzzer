f = open('foo', 'rb')
print(f.read1(1)) # OK
f.close()
print(f.read1(5)) # expected ValueError("I/O operation on closed file")
print(f.peek())   # expected ValueError("I/O operation on closed file")