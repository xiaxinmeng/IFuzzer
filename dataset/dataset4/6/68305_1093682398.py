u = 'hi~python'
b = u.encode('hz')   # bug in this step, the right sequence should be b"hi~~python"
print(b)    # the output is b"hi~python"

u = b.decode('hz')   # so can't decode, UnicodeDecodeError raised
print(u)