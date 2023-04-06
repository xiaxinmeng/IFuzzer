import io
import marshal



hex_string = "FBE901000000DA0136E90209000072010000007203000000DA0168A90372010000007205000000DA026161DA026A6A7BDA0278785B020000007201000000DA01353030DA0170E7E10B930189E4414130"
myb = bytes.fromhex(hex_string)
f = io.BytesIO(myb)
print(f)
data = marshal.load(f)
print(data)
print('We have segfault but we cannot see!')