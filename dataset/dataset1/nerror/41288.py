import io
import pickle


hex_string = "8004952A000000000000008C086461746574696D65948C086461746574696D65949388430A07B2010100000000000092059452942E"
myb = bytes.fromhex(hex_string)
f = io.BytesIO(myb)
print(f)
data = pickle.load(f)
print(data)
print('We have segfault but we cannot see!')
