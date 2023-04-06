import math, struct
FullInfinityAsInt = 0x7f800000
ThisFloat = (struct.unpack("f", struct.pack("I", FullInfinityAsInt)))[0]
print("The type is " + str(type(ThisFloat)))
if math.isinf(ThisFloat):
	print("This is an infiniity")
else:
	print("This is not an infinity")