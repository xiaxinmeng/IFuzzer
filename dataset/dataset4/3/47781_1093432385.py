BLOCKSIZE = 10*1024*1024

f=open("empty.txt", "w")
f.close()

f=open("empty.txt")
data = []
for i in range(10000):
    s = f.read(BLOCKSIZE)
    assert len(s) == 0
    data.append(s)