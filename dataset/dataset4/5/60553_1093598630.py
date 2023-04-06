HSF_VOL_DESC = Struct("< B 5s B")

# Python 3.2.3's "Struct.format" is actually a byte string
NSR_DESC = Struct(HSF_VOL_DESC.format.decode() + "B")