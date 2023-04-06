data1 = "aa\nbb\ncc\n"
data2 = "xx\n"

with open("data.txt","w") as f:
    f.write(data1)

with open("data.txt","r+") as f:
    f.write(data2)
#   f.tell()
    print("Line:",repr(f.readline()))

with open("data.txt") as f:
    print("All:",repr(f.read()))