import lzma
count = 0
f = lzma.LZMAFile('bigfile.xz' ,'r')
for line in f:
    count += 1
print(count)